from flask import Flask, request, jsonify, render_template
from translation import translate_text
from speech import speech_to_text, text_to_speech
from ocr import extract_text_from_image
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '')
    target = data.get('target_language', 'en')
    source = data.get('source_language', 'auto')
    result = translate_text(text, target, source)
    return jsonify({'translated_text': result})

@app.route('/speech-to-text', methods=['GET'])
def stt():
    result = speech_to_text()
    return jsonify({'text': result})

@app.route('/text-to-speech', methods=['POST'])
def tts():
    data = request.json
    text = data.get('text', '')
    language = data.get('language', 'en')
    result = text_to_speech(text, language)
    return jsonify({'status': result})

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})
    image = request.files['image']
    image_path = 'uploaded_image.png'
    image.save(image_path)
    text = extract_text_from_image(image_path)
    os.remove(image_path)
    return jsonify({'extracted_text': text})

if __name__ == '__main__':
    app.run(debug=True)