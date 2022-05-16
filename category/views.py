import ssl
import fasttext

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from PyKomoran import Komoran
from nltk.corpus import stopwords
import nltk

from category.serializers import CategorySerializer
from category.utils import text_preprocessing, text_classification, category_dict

"""
* 참고 사항 *
아래의 try-except 구문은 Mac에서만 필요할 수 있음
AWS EC2 Ubuntu 서버에서 필요하지 않다면 삭제하기
"""
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("averaged_perceptron_tagger")
nltk.download("stopwords")


class CategoryView(APIView):
    komoran = Komoran("EXP")
    stop_words = set(stopwords.words("english"))
    model = fasttext.load_model("fasttext_model/model_devook_20220516.bin")

    def post(self, request, format=None):
        """
        1. 요청 시 전달된 title 값 전처리
        2. 카테고리 분류 모델(.bin파일)에 입력 값으로 전달 하여 나온 출력 값(category)을 반환
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.data["title"]
            preprocessed_str = text_preprocessing(  # 데이터 전처리
                pykomoran=self.komoran, text=title, stop_words=self.stop_words
            )
            category = category_dict[
                text_classification(model=self.model, text=preprocessed_str)
            ]  # 카테고리 분류 모델의 입력 값으로 전달
            return Response(data={"category": category}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
