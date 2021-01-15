import logging
import moviepy.editor as mp
import speech_recognition as sr

def convert_mp4_wav(mp4_file):
    filename = mp4_file.split('.mp4')[0]
    clip = mp.VideoFileClip(f"{mp4_file}") 
    clip.audio.write_audiofile(filename + '_converted.wav')


def recordAudio(speech_file=None, export=False):
    """
    """
    r = sr.Recognizer()

    if speech_file:
        if speech_file.endswith(".mp4"):
            movie_file.split(".mp4")[0]

        with sr.AudioFile(speech_file) as source:
            audio = r.record(source) 

    else:
        with sr.Microphone() as source:
            print('Say something')
            r.adjust_for_ambient_noise(source=source)
            audio = r.listen(source)

    try:
        transcript = r.recognize_google(audio)
        if eport:
            # exporting the result 
            with open('recognized.txt',mode ='w') as file: 
                file.write("Recognized Speech:") 
                file.write("\n") 
                file.write(result) 
                print("ready!")

    except sr.UnknownValueError:
        print('Sorry, I did not get that.')
    except sr.RequestError:
        print('Sorry, my speech service is down.')

    return transcript

def activate(phrase='hey bro'):
    """ A keyword phrase to activate the assistant.
    Description:
    Using this trigger to get selective on activating our search function.
    """
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            transcript = r.recognize_google(audio)
            if transcript.lower() == phrase:
                return True
            else:
                return False

"""
A keyword phrase to trigger certain function.
Currently support:
    - Open an application
    - Search a phrase on google
"""

def triggerTime(phrase='check time'):
    """ A keyword phrase to activate the assistant.
    Description:
    Using this trigger to get selective on activating our time report function.
    """
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            transcript = r.recognize_google(audio)
            if transcript.lower() == phrase:
                return True
            else:
                return False


def triggerApps(phrase='open app'):
    """ A keyword phrase to activate the assistant.
    Description:
    Using this trigger to get selective on activating our open app function.
    """
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            transcript = r.recognize_google(audio)
            if transcript.lower() == phrase:
                return True
            else:
                return False


def triggerGglSearch(phrase='search google for'):
    """ A keyword phrase to activate the assistant.
    Description:
    Using this trigger to get selective on activating our search function.
    """
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            transcript = r.recognize_google(audio)
            if transcript.lower() == phrase:
                return True
            else:
                return False


def triggerIntroduce(phrase='your name'):
    """ A keyword phrase to activate the assistant.
    Description:
    Using this trigger to get selective on activating our search function.
    """
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            transcript = r.recognize_google(audio)
            if transcript.lower() == phrase:
                return True
            else:
                return False 
