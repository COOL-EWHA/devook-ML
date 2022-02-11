"""
title에서 한국어 고유명사(NNP) & 불용어 제거된 영어 단어 추출 후 csv 파일에 저장
"""
import csv
import pandas as pd

from PyKomoran import *
from nltk.corpus import stopwords

category_list = [
    "General_dev",
    "Web_dev",
    "Javascript",
    "React",
    "Vue.js",
    "Angular",
    "Node.js",
    "Java",
    "Python",
    "PHP",
    "Infra Structure",
    "Database",
    "Android",
    "iOS",
    "Git",
    "Bigdata_AI_ML",
]

stop_words = set(stopwords.words("english"))


def remove_stopwords_using_nltk(words):
    """
    영어 불용어 제거 후 리스트 반환
    """
    result = []
    for word in words:
        if word not in stop_words:
            result.append(word)
    return result


def convert_to_dataframe_and_save(filename):
    """
    DataFrame 형태로 변환 후 csv 파일에 저장
    """
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f)

        csv_list = []
        for line in reader:
            csv_list.append(line)
        f.close()

    data_df = pd.DataFrame(csv_list)
    data_df.to_csv(filename, sep=",", na_rep="0", encoding="utf-8")


def morpheme_tokenization(column):
    """
    형태소/단어 토큰화
    """
    komoran = Komoran("EXP")

    for category in category_list:
        file = pd.read_csv(f"csv_files/{category}.csv", encoding="utf-8")
        values = file[column]

        with open(
            f"{column}_morpheme_tokenization_data/{category}.csv",
            mode="w",
            newline="",
            encoding="utf-8",
        ) as out:
            csv_out = csv.writer(out)
            for val in values:
                try:
                    ko_proper_nouns = komoran.get_morphes_by_tags(val, tag_list=["NNP"])
                    en_words = komoran.get_morphes_by_tags(val, tag_list=["SL"])
                    morpheme_list = ko_proper_nouns + remove_stopwords_using_nltk(
                        words=en_words
                    )
                except IndexError:  # IndexError 예외 처리
                    print(val.index)
                csv_out.writerow(morpheme_list)
        print(f"{category} 첫번째 완료")
        convert_to_dataframe_and_save(
            filename=f"{column}_morpheme_tokenization_data/{category}.csv"
        )
        print(f"{category} 두번째 완료")


if __name__ == "__main__":
    morpheme_tokenization("title")  # title / description
