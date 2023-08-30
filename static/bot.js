// Obtener elementos del DOM
const chatLog = document.getElementById("chat-log");
const userInput = document.getElementById("user-input");

// Función para agregar un mensaje al chat
function addMessage(message, sender) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    messageDiv.textContent = `${sender}: ${message}`;
    chatLog.appendChild(messageDiv);
    chatLog.scrollTop = chatLog.scrollHeight;
}

// Función para enviar el mensaje del usuario y obtener la respuesta del bot
function sendMessage() {
    const userMessage = userInput.value.trim();
    if (userMessage !== "") {
        addMessage(userMessage, "Tú");

        // Enviar la entrada del usuario al servidor
        fetch("/get_response", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: "user_input=" + encodeURIComponent(userMessage)
        })
        .then(response => response.text())
        .then(response => {
            addMessage(response, "Bot");
        })
        .catch(error => {
            console.error("Error al obtener respuesta del bot:", error);
        });

        // Limpiar el campo de entrada del usuario
        userInput.value = "";
    }
}

// Manejar la pulsación de la tecla Enter en el campo de entrada
userInput.addEventListener("keypress", event => {
    if (event.key === "Enter") {
        sendMessage();
    }
});
