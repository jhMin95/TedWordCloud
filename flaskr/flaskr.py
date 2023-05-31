# all the imports
from flask import Flask, request, render_template
import requests

# my module import
from morpheme_analyzer import MorphemeAnalyzer

# create our little application :)
app = Flask(__name__)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    # POST 요청으로 전달된 데이터 가져오기
    data = request.form.get('data')

    analyzer = MorphemeAnalyzer();
    morpheme_list = analyzer.analyze(data);


    return render_template('result.html', result=morpheme_list)

if __name__ == '__main__':
    app.run(debug=True)

