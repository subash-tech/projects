from flask import Flask, request, jsonify, render_template
from googletrans import Translator
from gtts import gTTS
import os
import time

app = Flask(__name__)

# Enable serving HTML files from templates directory
@app.route('/')
def home():
    return render_template('index.html')

translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    english_text = data.get("text", "")

    if not english_text:
        return jsonify({"error": "No text provided"}), 400

    # Translate English to Tamil
    translated_text = translator.translate(english_text, src='en', dest='ta').text

    # Generate a unique filename using timestamp
    audio_filename = f"output_{int(time.time())}.mp3"
    audio_path = os.path.join("static", audio_filename)

    # Convert Tamil text to speech
    tts = gTTS(text=translated_text, lang='ta')
    tts.save(audio_path)

    return jsonify({
        "translated_text": translated_text,
        "audio_url": f"/static/{audio_filename}"
    })

if __name__ == '__main__':
    os.makedirs("static", exist_ok=True)  # Ensure static folder exists
    app.run(debug=True)
