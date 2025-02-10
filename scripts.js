function showLoading() {
    document.getElementById('loadingSpinner').style.display = 'block';
}

function hideLoading() {
    document.getElementById('loadingSpinner').style.display = 'none';
}

function appendMessage(text, sender) {
    const chatBox = document.getElementById("chat-box");
    const message = document.createElement("div");
    message.classList.add("chat-message", sender, "fade-in");
    message.innerText = text;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function translateText() {
    const englishText = document.getElementById("english-text").value;

    if (!englishText) {
        alert("Please enter some text!");
        return;
    }

    appendMessage(englishText, "user");
    showLoading();

    fetch('http://127.0.0.1:5000/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: englishText })
    })
    .then(response => response.json())
    .then(data => {
        hideLoading();

        if (data.error) {
            appendMessage("❌ Error: " + data.error, "system");
        } else {
            appendMessage("✅ " + data.translated_text, "system");

            // Smooth Audio Playback Fix
            const audio = new Audio(`${data.audio_url}?t=${new Date().getTime()}`);
            audio.volume = 0.8;
            audio.play();
        }
    })
    .catch(error => {
        hideLoading();
        appendMessage("❌ Error: " + error, "system");
    });
}
