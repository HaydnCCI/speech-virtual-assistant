import os 
from modules.assistantVoice import say
from modules.speechCapture import activate, respond, record_audio
from modules.utils import create_index, search_es
from modules.speechActions import reportTime, openApp, searchGoogle


while True:   
    if activate():
        try:
            say("Hey, are you calling me? How may I assist")
            print('Say Something!')

            if triggerGglSearch():
                transcript = recordAudio()
                say("I got these results for you")
                searchGoogle(transcript)

            elif triggerApps():
                transcript = recordAudio()
                openApp(transcript)

            elif triggerTime():
                reportTime()

            elif triggerIntroduce():
                say("My name is Kindred")

                    

