# English-to-Tamil Text-to-Speech Translator

## Overview
This project is a web-based English-to-Tamil translator with Text-to-Speech (TTS) functionality. It translates English text into Tamil and provides speech output for the translated text.

## Features
- Translates English text to Tamil using the Google Translate API
- Converts Tamil text to speech using a Text-to-Speech (TTS) engine
- Simple and user-friendly web interface

## Technologies Used
- Python (Flask for backend)
- Google Translate API (for translation)
- gTTS (Google Text-to-Speech for Tamil voice output)
- HTML, CSS, JavaScript (for frontend)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/translator-project.git
   cd translator-project
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask application:
   ```sh
   python app.py
   ```
2. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```
3. Enter English text, click "Translate," and listen to the Tamil audio output.

## Project Structure
```
translator-project/
│── static/
│   ├── styles.css
│   ├── script.js
│── templates/
│   ├── index.html
│── app.py
│── requirements.txt
│── README.md
```

## Future Improvements
- Support for more languages
- Improved Tamil voice synthesis
- Mobile-friendly UI



---
### Contributors
- **Your Name** (subashb0707@gmail.com)

