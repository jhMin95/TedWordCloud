import re


def sentence_tokenize(text_list):
    # 문장 단위로 묶을 리스트
    sentences = []

    # 각 텍스트를 문장 단위로 분할하여 sentences 리스트에 추가
    for text in text_list:
        # 문장 분할을 위한 정규 표현식
        pattern = r"[.!?]"

        # 문장 분할
        sentences.extend(re.split(pattern, text))

    # 빈 문자열 요소 제거
    sentences = [sentence for sentence in sentences if sentence]

    return sentences
