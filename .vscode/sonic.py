import speech_recognition as aa

listener = aa.Recognizer()

try:
    with aa.Microphone() as origin:
        print("listening")
        speech = listener.listen(origin)
        instruction = listener.recognize_goggle(speech)
        print(instruction)
except:
    pass