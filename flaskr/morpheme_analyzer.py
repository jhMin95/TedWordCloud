from konlpy.tag import Kkma

class MorphemeAnalyzer:
    def __init__(self):
        self.kkma = Kkma()

    def analyze(self, text):

        sentences = self.kkma.sentences(text)
        result = []
        for sentence in sentences:
            pos_tags = self.kkma.pos(sentence)
            result.extend(pos_tags)
        return result
