from text2speech.Text2SpeechEngine import Text2SpeechEngine
from speech2text.Speech2TextListener import Speech2TextListener

'''
text_2_speech_engine = Text2SpeechEngine("en")
text_2_speech_engine.say("Hi my name is tiki tiki slim shady")
'''


def speak_text(my_text):
    # Initialize the engine
    print("Did you say: ", my_text)
    text_2_speech_engine = Text2SpeechEngine("en")
    text_2_speech_engine.say(my_text)


speech_2_text_listener = Speech2TextListener(speak_text)
speech_2_text_listener.start()
