from googletrans import Translator
from gtts import gTTS
import os

# Create translator object
translator = Translator()

# Get English input from the user
english_text = input("Enter text in English: ")

# Translate English to Tamil
translated_text = translator.translate(english_text, src='en', dest='ta').text
print("Tamil Translation:", translated_text)

# Convert Tamil text to speech
tts = gTTS(text=translated_text, lang='ta')

# Save and play the audio
tts.save("output2.mp3")
os.system("output2.mp3")  # Works on Windows
# On Mac/Linux, use: os.system("mpg321 output.mp3")

