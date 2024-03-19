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
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    generated_text = response.choices[0].text.strip()
    return render_template('index.html', response=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
