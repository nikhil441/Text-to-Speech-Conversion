#import required library
import pyttsx3
test = "Enter any text here"
#initializing engine
engine = pyttsx3.init()
#initializing var voices
voices = engine.getProperty('voices')
#voice_id changes depending on voices preinstalled in system first run above code to list out available voices and its attributes onto screen and then copy desired id as value of voice_id
#for voice in voices:
 #print("Voice:")
 #print(" - Name: %s" % voice.name)
 #print(" - Languages: %s" % voice.languages)
 #print(" - Gender: %s" % voice.gender)
 #print(" - Age: %s" % voice.age)
voice_id = #"Enter voice id here"
engine.setProperty('voice', voice_id)
engine.say(test)
engine.runAndWait()
