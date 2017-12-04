import speech_recognition as sr
while True:
    print("talk")
    r = sr.Recognizer()
    with sr.Microphone() as source:
         audio = r.listen(source)
         c=(r.recognize_google(audio))
         print(c)
         if c=='ok':
             break
