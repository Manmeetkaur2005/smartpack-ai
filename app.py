from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    user_input = data.get("message")

    # 🌱 Simulate flow logic:
    if user_input == "__start__":
        return jsonify({
            "reply": "Hi there! 👋 I'm your SmartPack AI assistant. I can help you with packaging optimization, shipment tracking, sustainability tips, and more. What would you like to explore?",
            "options": ["📦 Optimize Packaging", "📍 Track My Shipment", "🌱 Sustainability Tips", "📊 AI Insights", "💰 Pricing Info"]
        })

    elif user_input == "📦 Optimize Packaging":
        return jsonify({
            "reply": "Great choice! Our AI can optimize your packaging in multiple ways. What's your main goal?",
            "options": ["💰 Reduce Costs", "📏 Minimize Size", "♻️ Eco-Friendly Materials", "🚚 Improve Logistics"]
        })

    elif user_input == "📍 Track My Shipment":
        return jsonify({
            "reply": "I can help you track your shipments! What type of tracking do you need?",
            "options": ["📍 Live GPS Tracking", "📋 Delivery Status", "📱 QR Code Scanner", "📧 Email Updates"]
        })

    elif user_input == "🌱 Sustainability Tips":
        return jsonify({
            "reply": "🌱 Here are some eco-friendly packaging tips:\n\n• Use recyclable materials\n• Minimize packaging size\n• Choose biodegradable options\n• Implement digital receipts\n\nWould you like more specific tips?",
            "options": ["🌿 More Green Tips", "📊 Carbon Calculator", "♻️ Recycling Guide", "🔙 Back to Menu"]
        })

    elif user_input == "📊 AI Insights":
        return jsonify({
            "reply": "Our AI provides powerful insights:\n\n• 📈 Demand forecasting\n• 🎯 Cost optimization\n• 📊 Performance analytics\n• 🔮 Predictive maintenance\n\nWhat interests you most?",
            "options": ["📈 Demand Forecast", "🎯 Cost Analysis", "📊 Performance Report", "🔙 Back to Menu"]
        })

    elif user_input == "💰 Pricing Info":
        return jsonify({
            "reply": "Our pricing is flexible and based on your needs:\n\n• 🆓 Free trial available\n• 💰 Pay-per-use options\n• 📦 Enterprise packages\n• 🎯 Custom solutions\n\nWould you like to discuss pricing?",
            "options": ["💬 Talk to Sales", "📋 Get Quote", "🆓 Start Free Trial", "🔙 Back to Menu"]
        })

    elif user_input == "💰 Reduce Costs":
        return jsonify({
            "reply": "Our AI reduces packaging costs by up to 30%! We analyze:\n\n• Material efficiency\n• Labor optimization\n• Shipping costs\n• Waste reduction\n\nWant to see a cost analysis?",
            "options": ["📊 Get Cost Analysis", "💬 Expert Consultation", "🆓 Free Assessment", "🔙 Back to Menu"]
        })

    elif user_input == "📏 Minimize Size":
        return jsonify({
            "reply": "Smart size optimization can save up to 25% on shipping costs! Our AI considers:\n\n• Product dimensions\n• Protection requirements\n• Shipping regulations\n• Customer preferences\n\nReady to optimize?",
            "options": ["📐 Size Calculator", "📦 Package Designer", "💬 Expert Help", "🔙 Back to Menu"]
        })

    elif user_input == "♻️ Eco-Friendly Materials":
        return jsonify({
            "reply": "Go green with our sustainable materials:\n\n• 🌿 Biodegradable plastics\n• 📄 Recycled cardboard\n• 🍃 Plant-based packaging\n• ♻️ Reusable containers\n\nWhich material interests you?",
            "options": ["🌿 Biodegradable", "📄 Recycled", "🍃 Plant-based", "🔙 Back to Menu"]
        })

    elif user_input == "🚚 Improve Logistics":
        return jsonify({
            "reply": "Optimize your logistics with AI:\n\n• 🚛 Route optimization\n• 📦 Load balancing\n• ⏰ Delivery scheduling\n• 📍 Real-time tracking\n\nWhat's your priority?",
            "options": ["🚛 Route Planning", "📦 Load Optimization", "⏰ Schedule Management", "🔙 Back to Menu"]
        })

    elif user_input == "📍 Live GPS Tracking":
        return jsonify({
            "reply": "Track your shipments in real-time! Features include:\n\n• 📍 Live GPS coordinates\n• 🚚 Driver status updates\n• ⏰ Estimated arrival times\n• 📱 Mobile notifications\n\nReady to track?",
            "options": ["📱 Mobile App", "🌐 Web Dashboard", "📧 Email Alerts", "🔙 Back to Menu"]
        })

    elif user_input == "📋 Delivery Status":
        return jsonify({
            "reply": "Check delivery status with:\n\n• 📦 Package location\n• 📅 Delivery timeline\n• ✅ Status updates\n• 📞 Contact information\n\nHow would you like to check?",
            "options": ["🔍 Track by Number", "📱 Scan QR Code", "📧 Email Status", "🔙 Back to Menu"]
        })

    elif user_input == "🌿 More Green Tips":
        return jsonify({
            "reply": "More sustainability tips:\n\n• 🌱 Use local suppliers\n• 📦 Implement return programs\n• 💡 Energy-efficient processes\n• 🌍 Carbon offset programs\n• 📊 Measure your impact\n\nWant to calculate your carbon footprint?",
            "options": ["📊 Carbon Calculator", "🌍 Offset Programs", "📈 Impact Report", "🔙 Back to Menu"]
        })

    elif user_input == "💬 Talk to Sales":
        return jsonify({
            "reply": "Perfect! Our sales team will contact you within 24 hours. They'll discuss:\n\n• 📊 Your current needs\n• 💰 Custom pricing\n• 🎯 Implementation plan\n• 🆓 Demo options\n\nPlease provide your contact info.",
            "options": ["📞 Call Now", "📧 Email Request", "💬 Live Chat", "🔙 Back to Menu"]
        })

    elif user_input == "🔙 Back to Menu":
        return jsonify({
            "reply": "Sure! What would you like to explore next?",
            "options": ["📦 Optimize Packaging", "📍 Track My Shipment", "🌱 Sustainability Tips", "📊 AI Insights", "💰 Pricing Info"]
        })

    else:
        return jsonify({
            "reply": "I'm still learning! Let me take you back to the main menu where I can help you better.",
            "options": ["📦 Optimize Packaging", "📍 Track My Shipment", "🌱 Sustainability Tips", "📊 AI Insights", "💰 Pricing Info"]
        })

# ✅ ADD THIS ROUTE BELOW EVERYTHING BUT ABOVE THE MAIN BLOCK
@app.route("/dashboard")
def dashboard():
    return "<h1>This is your SmartPack AI Dashboard (coming soon!)</h1>"

# 🧠 Main entry point
if __name__ == "__main__":
    app.run(debug=True)
