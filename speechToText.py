import speech_recognition as sr
from os import path
def speech2Text(audio_file_path):
    """
    Converts a given audio file into text.

    Parameters:
    audio_file_path (str): The path to the audio file to be converted into text.

    Returns:
    str: The converted text from the audio file.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

if __name__ == "__main__":
    audio_file_path = "temp_audio.wav"
    print(speech2Text(audio_file_path))