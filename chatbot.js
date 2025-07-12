function startConversation() {
  const chatlog = document.getElementById("chatlog");
  const optionDiv = document.getElementById("options");
  
  // Clear previous conversation
  chatlog.innerHTML = "";
  optionDiv.innerHTML = "";
  
  // Show loading message
  const loadingMsg = document.createElement("p");
  loadingMsg.innerText = "🤖 Starting conversation...";
  loadingMsg.style.background = "#e3f2fd";
  loadingMsg.style.color = "#1976d2";
  loadingMsg.style.margin = "8px 0";
  loadingMsg.style.padding = "8px 12px";
  loadingMsg.style.borderRadius = "15px";
  loadingMsg.style.maxWidth = "80%";
  chatlog.appendChild(loadingMsg);

  fetch("/get_response", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: "__start__" })
  })
  .then(res => res.json())
  .then(data => {
    // Remove loading message
    chatlog.removeChild(loadingMsg);
    showBotMessage(data.reply, data.options);
  })
  .catch(error => {
    console.error("Error:", error);
    chatlog.removeChild(loadingMsg);
    showBotMessage("Sorry, I'm having trouble connecting. Please try again.", ["Start Chat"]);
  });
}

function showBotMessage(reply, options = []) {
  const chatlog = document.getElementById("chatlog");
  const optionDiv = document.getElementById("options");

  // Show bot reply
  const botMsg = document.createElement("p");
  botMsg.innerText = "🤖 " + reply;
  botMsg.style.background = "#e3f2fd";
  botMsg.style.color = "#1976d2";
  botMsg.style.margin = "8px 0";
  botMsg.style.padding = "8px 12px";
  botMsg.style.borderRadius = "15px";
  botMsg.style.maxWidth = "80%";
  botMsg.style.wordWrap = "break-word";
  chatlog.appendChild(botMsg);

  // Clear old buttons
  optionDiv.innerHTML = "";

  // Create new option buttons
  options.forEach(option => {
    const btn = document.createElement("button");
    btn.innerText = option;
    btn.className = "option-btn";
    btn.style.margin = "5px";
    btn.style.background = "#4caf50";
    btn.style.color = "white";
    btn.style.border = "none";
    btn.style.padding = "8px 16px";
    btn.style.borderRadius = "20px";
    btn.style.cursor = "pointer";
    btn.style.fontSize = "14px";
    btn.style.transition = "background 0.3s";
    btn.onmouseover = () => btn.style.background = "#45a049";
    btn.onmouseout = () => btn.style.background = "#4caf50";
    btn.onclick = () => sendUserInput(option);
    optionDiv.appendChild(btn);
  });

  // Auto scroll to bottom
  chatlog.scrollTop = chatlog.scrollHeight;
}

function sendUserInput(userInput) {
  const chatlog = document.getElementById("chatlog");

  // Show user message
  const userMsg = document.createElement("p");
  userMsg.innerText = "🧑 " + userInput;
  userMsg.style.fontWeight = "bold";
  userMsg.style.background = "#f3e5f5";
  userMsg.style.color = "#7b1fa2";
  userMsg.style.margin = "8px 0 8px auto";
  userMsg.style.padding = "8px 12px";
  userMsg.style.borderRadius = "15px";
  userMsg.style.maxWidth = "80%";
  userMsg.style.textAlign = "right";
  userMsg.style.wordWrap = "break-word";
  chatlog.appendChild(userMsg);

  // Show typing indicator
  const typingMsg = document.createElement("p");
  typingMsg.innerText = "🤖 Typing...";
  typingMsg.style.background = "#e3f2fd";
  typingMsg.style.color = "#1976d2";
  typingMsg.style.margin = "8px 0";
  typingMsg.style.padding = "8px 12px";
  typingMsg.style.borderRadius = "15px";
  typingMsg.style.maxWidth = "80%";
  typingMsg.style.fontStyle = "italic";
  chatlog.appendChild(typingMsg);

  fetch("/get_response", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userInput })
  })
  .then(res => res.json())
  .then(data => {
    // Remove typing indicator
    chatlog.removeChild(typingMsg);
    showBotMessage(data.reply, data.options);
  })
  .catch(error => {
    console.error("Error:", error);
    chatlog.removeChild(typingMsg);
    showBotMessage("Sorry, I'm having trouble connecting. Please try again.", ["Back to Menu"]);
  });
}

// Auto-start conversation when page loads
document.addEventListener('DOMContentLoaded', function() {
  // Don't auto-start, let user click the button
  console.log("Chatbot ready! Click 'Start Chat' to begin.");
});
