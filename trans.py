from googletrans import Translator

# Create a Translator object
translator = Translator()

# Input text in English
english_text = "Hello, how are you?"

# Translate to Tamil
translated_text = translator.translate(english_text, src='en', dest='ta')

# Print the translation
print("English:", english_text)
print("Tamil:", translated_text.text)
