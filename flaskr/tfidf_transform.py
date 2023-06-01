from sklearn.feature_extraction.text import TfidfVectorizer
import joblib


class TfidfAnalyzer:
    def __init__(self):
        self.vectorizer = None
        self.feature_names = None

    def load_vectorizer(self, vectorizer_path):
        try:
            self.vectorizer = joblib.load(vectorizer_path)
            self.feature_names = self.vectorizer.get_feature_names_out()
        except FileNotFoundError:
            raise Exception(f"No file found at the provided path: {vectorizer_path}")
        except Exception as e:
            raise Exception(f"An error occurred while loading the vectorizer: {e}")

    def analyze_document(self, document):
        if self.vectorizer is None:
            raise Exception("Vectorizer has not been loaded.")

        try:
            # TF-IDF 행렬로 변환
            print(document)
            tfidf_matrix = self.vectorizer.transform([document])
        except Exception as e:
            raise Exception(f"An error occurred while transforming the document: {e}")

        # 분석 결과 딕셔너리 생성
        try:
            tfidf_scores = tfidf_matrix.toarray().flatten()
            tfidf_result = {}
            for idx, score in enumerate(tfidf_scores):
                if score > 0:
                    tfidf_result[self.feature_names[idx]] = score
            sorted_dict = dict(
                sorted(tfidf_result.items(), key=lambda x: x[1], reverse=True)
            )
        except Exception as e:
            raise Exception(
                f"An error occurred while creating the analysis result dictionary: {e}"
            )

        return sorted_dict
