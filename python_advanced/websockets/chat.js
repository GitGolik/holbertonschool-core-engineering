const socket = new WebSocket("ws://localhost:8000/ws");

const messages = document.getElementById("messages");
const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");

function addMessage(text, className) {
    const message = document.createElement("div");
    message.className = className;
    message.textContent = text;

    messages.appendChild(message);
    messages.scrollTop = messages.scrollHeight;
}

socket.onopen = () => {
    addMessage("Connected to WebSocket server.", "status");
};

socket.onmessage = (event) => {
    addMessage(event.data, "received");
};

socket.onclose = () => {
    addMessage("Connection closed.", "status");
};

socket.onerror = () => {
    addMessage("Connection error.", "status error");
};

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const text = input.value.trim();

    if (text === "") {
        return;
    }

    socket.send(text);
    addMessage(`You: ${text}`, "sent");

    input.value = "";
    input.focus();
});
