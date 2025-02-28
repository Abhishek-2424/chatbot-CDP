function sendMessage() {
  let userInput = document.getElementById("user-input").value;
  if (userInput.trim() === "") return;

  let chatBox = document.getElementById("chat-box");
  let userMessage = `<div class="message user"><b>You:</b> ${userInput}</div>`;
  chatBox.innerHTML += userMessage;

  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userInput }),
  })
    .then((response) => response.json())
    .then((data) => {
      let botMessage = `<div class="message bot"><b>Bot:</b> ${data.response}</div>`;
      chatBox.innerHTML += botMessage;
      chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch((error) => {
      console.error("Error:", error);
    });

  document.getElementById("user-input").value = "";
  document.getElementById("user-input").focus();
}

function handleKeyPress(event) {
  if (event.key === "Enter") sendMessage();
}

function toggleChat() {
  let chatWidget = document.querySelector(".chat-widget");
  let chatIcon = document.querySelector(".chat-icon");

  if (chatWidget.style.display === "none" || chatWidget.style.display === "") {
    chatWidget.style.display = "flex";
    chatIcon.style.display = "none";
  } else {
    chatWidget.style.display = "none";
    chatIcon.style.display = "flex";
  }
}
