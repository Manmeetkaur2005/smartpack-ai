const chatDisplay = document.getElementById("chatDisplay");
const userInput = document.getElementById("userInput");

function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  // Display user message
  chatDisplay.innerHTML += `<div class='user-msg'>👤 ${message}</div>`;

  // Call backend
  fetch("http://127.0.0.1:5000/chatbot_reply", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  })
    .then((res) => res.json())
    .then((data) => {
      chatDisplay.innerHTML += `<div class='bot-msg'>🤖 ${data.reply}</div>`;
      chatDisplay.scrollTop = chatDisplay.scrollHeight;
    })
    .catch((err) => {
      chatDisplay.innerHTML += `<div class='bot-msg error'>⚠️ Error getting response</div>`;
      console.error(err);
    });

  userInput.value = "";
}
document.addEventListener("DOMContentLoaded", function () {
  const chatDisplay = document.getElementById("chatDisplay");
  const userInput = document.getElementById("userInput");
  const sendBtn = document.getElementById("sendBtn");

  sendBtn.addEventListener("click", () => {
    const message = userInput.value.trim();
    if (message === "") return;

    appendMessage("You", message);
    userInput.value = "";

    // ✅ Simulated reply (replace with fetch to backend later)
    setTimeout(() => {
      appendMessage("Bot", "Thanks for your message. I’ll get back to you!");
    }, 500);
  });

  function appendMessage(sender, message) {
    const msg = document.createElement("p");
    msg.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatDisplay.appendChild(msg);
    chatDisplay.scrollTop = chatDisplay.scrollHeight;
  }
});
