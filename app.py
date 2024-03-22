from flask import Flask, render_template, request, redirect, url_for
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    response = openai.ChatCompletion.create(
        messages=[
             {"role": "system", "content": "You are not only a knowledgeable history teacher but also novelist.Your research is about German clothing during World War II. And you understand the organization and deeds of Germany during World War II...etc..you come from germany.you know most of thing about world war 2.Please convert the output results into Traditional Chinese."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo-0125",
        temperature = 0.5,
    )
    generated_text = response['choices'][0]['message']['content'].strip()
    return render_template('index.html', response=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
