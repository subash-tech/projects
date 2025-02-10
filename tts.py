from gtts import gTTS
import os

# Tamil text input
tamil_text = "வணக்கம், இன்று எப்படி இருக்கிறீர்கள்?"

# Convert Tamil text to speech
tts = gTTS(text=tamil_text, lang='ta')

# Save the audio file
tts.save("tamil_speech.mp3")

# Play the saved audio file
os.system("tamil_speech.mp3")  # Works on Windows
# On Mac/Linux, use: os.system("mpg321 tamil_speech.mp3")
