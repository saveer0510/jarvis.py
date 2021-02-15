
import pyttsx3
import speech_recogition as sr
engine=pyttsx3.init('sapi5')


voices =engine.getProperty('voices')

print(voices.id)
