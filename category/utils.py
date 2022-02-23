import re
import fasttext

category_dict = {
    "__label__general-dev": "일반 개발",
    "__label__web-dev": "웹 개발",
    "__label__infra-structure": "Infra Structure",
    "__label__javascript": "Javascript",
    "__label__java": "Java",
    "__label__bigdata-ai-ml": "빅데이터·AI·머신러닝",
    "_label__react": "React",
    "__label__database": "Database",
    "__label__android": "Android",
    "__label__node-js": "Node.js",
    "__label__git": "Git",
    "__label__php": "PHP",
    "__label__vue-js": "Vue.js",
    "__label__python": "Python",
    "__label__iOS": "iOS",
    "__label__angular": "Angular",
}


def remove_stopwords_using_nltk(words, stop_words):
    """
    영어 불용어 제거 후 반환
    param: words[list], stop_words[list]
    return: [list]
    """
    result = []
    for word in words:
        if word not in stop_words:
            result.append(word)
    return result


def remove_short_words(text):
    """
    길이가 1~2인 단어들을 정규 표현식을 사용하여 삭제 후 반환
    param: [str]
    return: [str]
    """
    short_word = re.compile(r"\W*\b\w{1,2}\b")
    return short_word.sub("", text)


def convert_list_to_str(val):
    """
    list 타입의 데이터를 str 타입으로 변환 후 반환
    param: [list]
    return: [str]
    """
    return " ".join(val)


def convert_upper_case_to_lower_case(text):
    """
    소문자 변환 후 반환
    param: [str]
    return: [str]
    """
    return text.lower()


def text_preprocessing(pykomoran, text, stop_words):
    """
    전달된 데이터 전처리 수행
    param: pykomoran[Komoran 객체], text[str], stop_words[list]
    return: [string]
    """
    ko_proper_nouns_list = pykomoran.get_morphes_by_tags(
        text, tag_list=["NNP"]
    )  # 고유명사 리스트
    en_words_list = pykomoran.get_morphes_by_tags(text, tag_list=["SL"])  # 영단어 리스트
    en_words_list_remove_stopwords = (
        remove_stopwords_using_nltk(  # 영단어에서 stopwords 제거한 리스트
            words=en_words_list, stop_words=stop_words
        )
    )
    en_words_str_remove_shortwords = remove_short_words(  # 길이가 짧은 영단어 제거한 문자열
        text=convert_list_to_str(val=en_words_list_remove_stopwords)
    )
    en_words_str_lower_case = convert_upper_case_to_lower_case(  # 모두 소문자 변환
        text=en_words_str_remove_shortwords
    )
    ko_proper_nouns_str = convert_list_to_str(val=ko_proper_nouns_list)
    return ko_proper_nouns_str + " " + en_words_str_lower_case


def text_classification(model, text):
    """
    전달된 데이터가 해당되는 카테고리 반환
    param: model[FastText model], text[str]
    return: [str]
    """
    result = model.predict(text)
    return result[0][0]
