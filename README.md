# Text and Speech Conversion Project

**PROBLEM STATEMENT**

In this project, our goal is to achieve the problem of converting textual data into speech data and speech to text.

**DESCRIPTION OVERVIEW**

As we know, some people have difficulty reading large amounts of text due to dyslexia and other learning disabilities. Some people have basic literary levels. They often get frustrated trying to browse the internet because so much of it is in text form or on other hand some people prefer to listen or watch a news article (or something like this) instead of reading. So, to solve all these problems a concept comes into mind that is "text to speech" and "speech to text".

Text-to-speech (TTS) technology reads aloud digital text. It can take words on computers, smartphones, tablets and convert them into audio. We will be using Google Text to Speech, commonly known as the gTTS API. It is a very easy-to-use library that converts the text entered into an audio file which can be saved as an mp3 file. It supports several languages and the speech can be delivered in any one of the two available audio speeds, fast or slow.

Speech-to-text (STT) technology converts spoken language into written text. We will be using the `speech_recognition` library to achieve this. It allows us to convert audio files into text using Google's speech recognition API.

**PROJECT COMPONENTS**

1. **Text-to-Speech (TTS)**
   - Converts textual data into speech.
   - Uses the gTTS API to generate audio files from text.

2. **Speech-to-Text (STT)**
   - Converts speech data into textual data.
   - Uses the `speech_recognition` library to transcribe audio files or live microphone input into text.

**REQUIREMENTS**

- Python 3.x
- gTTS
- speech_recognition

**INSTALLATION**

1. Install the required libraries:
    ```sh
   pip install -r requirements.txt  
    ```

**USAGE**

1. **Text-to-Speech (TTS)**
   - Run the `textToSpeech.py` script to convert text to speech.

2. **Speech-to-Text (STT)**
   - Run the `speechToText.py` script to convert an audio file to text.
   - Run the `liveSpeechToText.py` script to convert live microphone input to text.
