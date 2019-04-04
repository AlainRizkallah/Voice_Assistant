import speech_recognition as sr
print(sr.__version__)
r = sr.Recognizer()
m = sr.Microphone()


#Using pre recorded .wav files:

#phrase du tuto
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)

Response=r.recognize_google(audio)

#Hello my name is Alan
hello_alain = sr.AudioFile('Hello_alain.wav')
with hello_alain as source:
    audio = r.record(source)

Response=r.recognize_google(audio)


#Using Default Microphone:

mic = sr.Microphone()
#Or use specific device, eg:
#print(sr.Microphone.list_microphone_names())
#mic = sr.Microphone(device_index=1)

with mic as source:
    audio = r.listen(source)

Response=r.recognize_google(audio)

