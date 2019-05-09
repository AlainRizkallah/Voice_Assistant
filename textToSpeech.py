import random
import time
import numpy
import importlib

import weatherAPI
import speech_recognition as sr

Users=[]
UsersAudios=[]
Prenoms=[]
weatherLexicon=["météo","temps","température"]

with open('Prenoms.csv' , 'r') as csvfile:
    csvfile.readline()  # skip the first line(column title)
    for line in csvfile:
        csv_row = line.split(';') # put ; as separator here
        prenom = csv_row[0]#here, get this as integer
        Prenoms.append(prenom)


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio, language='fr-FR')
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"
    if response["success"]:
        comprehend(response["transcription"],audio)
    else:
        return response

    return response

def comprehend(transcription,audio):
    for word in transcription.split():
        word = word.lower()
        print(word)
        if word in Prenoms :
            print("^This is a name!")
            if word not in Users:
                Users.append(word)
                UsersAudios.append([word,audio])
            else:
                for list in UsersAudios:
                    if list[0]==word :
                        list.append(audio)
        if word in weatherLexicon:
            print("il faut donner la température")
            importlib.reload(weatherAPI)
            weatherAPI.printTemp()


