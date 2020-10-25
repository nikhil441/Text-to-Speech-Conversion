import pyttsx3
test = "Hi my name is Nikhil Padman!"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#for voice in voices:
 #print("Voice:")
 #print(" - Name: %s" % voice.name)
 #print(" - Languages: %s" % voice.languages)
 #print(" - Gender: %s" % voice.gender)
 #print(" - Age: %s" % voice.age)
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
engine.setProperty('voice', en_voice_id)
engine.say(test)
engine.runAndWait()
