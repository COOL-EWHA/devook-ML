from rest_framework.test import APITestCase

from category.utils import (
    remove_stopwords_using_nltk,
    remove_short_words,
    text_classification,
    category_dict,
)


class TextClassificationTestCase(APITestCase):
    def test_영어_불용어_제거_성공(self):
        """
        불용어 리스트에 포함된 단어들을 제거한다.
        """
        # given
        words = ["Hello", "the", "is"]
        stop_words = ["the", "is"]
        expected_result = ["Hello"]
        # when
        result = remove_stopwords_using_nltk(words=words, stop_words=stop_words)
        # then
        self.assertEqual(expected_result, result)

    def test_길이가_짧은_단어_삭제_성공(self):
        """
        길이가 1~2인 단어들을 정규 표현식을 사용하여 삭제한다.
        """
        # given
        text = "Hello is a"
        expected_result = "Hello"
        # when
        result = remove_short_words(text=text)
        # then
        self.assertEqual(expected_result, result)

    def test_카테고리_반환_성공(self):
        """
        category_dict에 존재하는 Key 값 중 하나를 반환한다.
        """
        # given
        text = "database"
        # when
        result = text_classification(text=text)
        # then
        self.assertTrue(result in category_dict)
