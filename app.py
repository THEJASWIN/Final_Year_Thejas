import openai
from flask import *

app = Flask(__name__)
openai.api_key = "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"

@app.route('/')
def index():
    return "API is working"

@app.route('/nl2py',methods = ['POST'])
def api_1():
    codePrompt = request.form['input']
    response = openai.Completion.create(
    engine="davinci-codex",
    prompt=codePrompt,
    temperature=0,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )      
    return response.choices[0].text

@app.route('/py2nl',methods = ['POST'])
def api_2():
    codePrompt = request.form['input']
    response = openai.Completion.create(
    engine="davinci-codex",
    prompt=codePrompt,
    temperature=0,
    max_tokens=513,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\"\"\""]
    )
    return response.choices[0].text

if __name__ == '__main__':  
   app.run(debug = True)  