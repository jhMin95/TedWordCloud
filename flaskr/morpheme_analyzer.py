from khaiii import KhaiiiApi


class MorphemeAnalyzer:
    def __init__(self):
        self.khaiii = KhaiiiApi()

    def analyze(self, sentence_list):
        morph_list = []
        try:
            for sentence in sentence_list:
                sentence = sentence.replace("\u200b", "").replace("\u3000", "").strip()
                for word in self.khaiii.analyze(sentence):
                    for morph in word.morphs:
                        morph_list.append(f"{morph.lex}_{morph.tag}")
            # result 를 string 으로 통합
            result = " ".join(morph_list)
            print(result)
        except Exception as e:
            print(f"Error occurred: {e}")
            result = None
        return result
