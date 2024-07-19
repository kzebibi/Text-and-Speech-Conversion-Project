from gtts import gTTS
import base64


def text2Speech(data):
    """
    Converts a given text into speech and returns the speech as a base64 encoded string.

    Parameters:
    data (str): The text to be converted into speech.

    Returns:
    bytes: The speech as a base64 encoded string.
    """
    my_text = data
    tts = gTTS(text=my_text, lang="en", slow=False)
    tts.save("converted-file.mp3")  # save file as ... (here saving as mp3)
    with open("converted-file.mp3", "rb") as file:
        my_string = base64.b64encode(file.read())
    return my_string
