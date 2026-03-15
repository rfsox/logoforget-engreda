import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

# إعداد Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')

        # استخدام موديل Llama 3 القوي والسريع
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192",
        )

        return jsonify({'result': chat_completion.choices[0].message.content})

    except Exception as e:
        return jsonify({'result': f'خطأ من المصدر الجديد: {str(e)}'})

app = app
