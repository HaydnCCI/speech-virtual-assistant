from .assistantVoice import say
from .utils import search_es
import speech_recognition as sr
from time import ctime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def reportTime(voice_data):
    if 'what time is it' in voice_data:
        say(ctime())
        print(ctime())


def openApp(transcript):
    sys_command = search_es(transcript)
    os.system(sys_command)
    say("I opened that application for you")


def searchGoogle(query):
    trigger_phrase = "search google for"
    browser = webdriver.Chrome("config/chromedriver")
    browser.get('http://www.google.com')
    search = browser.find_element_by_name('q')
    search_terms = transcript.lower().split(trigger_phrase)[-1]
    search.send_keys(search_terms)
    search.send_keys(Keys.RETURN)





