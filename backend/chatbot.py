def get_chatbot_reply(message):
    msg = message.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello! 👋 How can I assist you with SmartPack AI?"
    elif "box" in msg or "suggestion" in msg:
        return "You can enter your item dimensions in the dashboard to get a smart box suggestion."
    elif "qr" in msg or "code" in msg:
        return "Once a box is suggested, click 'Generate QR' to get a downloadable code."
    elif "co2" in msg or "carbon" in msg:
        return "We help reduce CO₂ by optimizing packaging space!"
    else:
        return "I'm here to help! Try asking about box suggestion, QR code, or packaging."

# 🔁 Later you can replace this with OpenAI/Gemini/HuggingFace integration if needed
