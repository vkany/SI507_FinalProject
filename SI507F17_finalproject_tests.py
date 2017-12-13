from flask import Flask, request, render_template
import requests

app = Flask(__name__)


def duck_answer_this(question):
    # based on https://duckduckgo.com/api
    response = requests.get('http://api.duckduckgo.com/', params={
        'q': question,
        'format': 'json'
    })
    # print(response.text)
    result = response.json()
    return result


@app.route('/')
def index():
    question = request.args.get('q')
    answer = None
    result = {}

    if question:
        # TODO get result and answer values
        result = duck_answer_this(question)
        answer = result.get('Abstract')

    # always looks for template in 'templates' folder relative to the current folder
    return render_template('index.html', question=question, answer=answer, result=result)

if __name__ == '__main__':
    # auto reloads (mostly) new code and shows exception traceback in the browser
    app.run(use_reloader=True, debug=True)
