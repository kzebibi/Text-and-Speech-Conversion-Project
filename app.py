from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin
from speechToText import speech2Text
from textToSPeech import text2Speech
import os

os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("main.html")


@app.route("/text-to-speech", methods=["POST"])
@cross_origin()
def text_to_speech():
    data = request.json["data"]
    result = text2Speech(data)
    return {"data": result.decode("utf-8")}


@app.route("/speech-to-text", methods=["POST"])
def speech_to_text():
    if 'audioFile' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    audio_file = request.files['audioFile']
    audio_file_path = 'temp_audio.wav'
    audio_file.save(audio_file_path)
    text = speech2Text(audio_file_path)
    return jsonify({'data': text})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
