# all the imports
from flask import Flask, request, render_template
import requests
from wordcloud import WordCloud

# my module import
from crawlted import extract_text_from_url
from morpheme_analyzer import MorphemeAnalyzer
from ted_tokenizer import sentence_tokenize
from tfidf_transform import TfidfAnalyzer

# create our little application :)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    # POST 요청으로 전달된 데이터 가져오기
    input_url = request.form.get("url")

    # 올바른 url 방식인지 확인
    if not input_url.startswith("https://www.ted.com/talks/"):
        return (
            render_template(
                "error.html",
                error="올바른 url 을 입력해주세요. <br> url 형식 : https://www.ted.com/talks/~~",
            ),
            400,
        )

    # url 에서 텍스트 추출
    raw_data = extract_text_from_url(input_url + "/transcript?language=ko")
    if raw_data is None:
        return (
            render_template("error.html", error="데이터를 찾을 수 없습니다. 올바른 url 을 입력해주세요."),
            400,
        )
    sentence_list = sentence_tokenize(raw_data)

    # 텍스트 분석
    analyzer = MorphemeAnalyzer()
    script_str = analyzer.analyze(sentence_list)
    if script_str is None:
        return render_template("error.html", erorr="형태소 분석 중 에러 발생"), 500

    # tf-idf 분석
    try:
        tfidf_analyzer = TfidfAnalyzer()
        tfidf_analyzer.load_vectorizer("tfidf_vectorizer.pkl")
        tfidf_result = tfidf_analyzer.analyze_document(script_str)
    except Exception as e:
        return render_template("error.html", error=f"tf-idf 분석 중 에러 발생: {e}"), 500

    # 정렬된 dictionary 의 상위 20개 추출한 딕셔너리 반환
    result_list = list(tfidf_result.items())[:20]
 # WordCloud 생성 및 저장
    wordcloud = WordCloud(font_path='/goinfre/jimin/TedWordCloud/flaskr/static/D2Coding.ttf', background_color='white')
    wordcloud.generate_from_frequencies(tfidf_result)
    wordcloud_image_path = '/goinfre/jimin/TedWordCloud/flaskr/static/wordcloud.png'  # WordCloud 이미지 저장 경로
    wordcloud.to_file(wordcloud_image_path)

    return render_template('result.html', result=result_list, wordcloud_image=wordcloud_image_path)


if __name__ == "__main__":
    app.run(debug=True)
