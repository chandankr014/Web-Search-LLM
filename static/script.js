function sendMessage() {
    const userMessage = document.getElementById("user-input").value;
    const nOption = document.getElementById("n-option").value;
    const topNOption = document.getElementById("top-n-option").value;
    const modelOption = document.getElementById("model-option").value;
    const headlessMode = document.getElementById("headless-switch").checked;

    // Display the user's message
    appendMessage("User", userMessage);

    // Send message and options to the server
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: userMessage,
            N: nOption,
            TOP_N: topNOption,
            model: modelOption,
            headless_mode: headlessMode
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("LOG: Data loaded Successfully!")
        appendMessage("AI", data);
    })
    .catch(error => console.error("Error:", error));
}

function appendMessage(sender, message) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");
    messageElement.className = "message";
    if (sender === 'AI') {
        messageElement.innerHTML = `<u style="color: black;"><strong>${sender}:</strong></u> ${message} <hr>`;
    } else {
        messageElement.innerHTML = `<u style="color: black;"><strong>${sender}:</strong></u> ${message}`;
    }
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;  // Auto scroll to the latest message
}
