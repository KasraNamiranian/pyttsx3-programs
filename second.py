import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty("rate")
print("rate =",rate)
engine.setProperty("rate",125)


volume = engine.getProperty("volume")
print("volume =",volume)
engine.setProperty("volume",1.0)


voices = engine.getProperty("voices")
print("voice =",voices)
engine.setProperty("voice",voices[1].id)
engine.setProperty("voice","Microsoft Sam")
engine.setProperty("voice","flite-cmu-us-slt")

engine.say("Hello World!")
engine.say("My current speaking rate is"+str(rate))
engine.runAndWait()