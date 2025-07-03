from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from packaging_engine import suggest_box  

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# ✅ Route to show GIF intro first
@app.route("/")
def intro():
    return render_template("intro.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/suggest_box", methods=["POST"])
def suggest_box_api():
    data = request.get_json()
    items = data.get("items", [])
    if not items:
        return jsonify({"error": "No items provided"}), 400
    try:
        result = suggest_box(items)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/generate_qr", methods=["POST"])
def generate_qr():
    return jsonify({"qr_url": "https://api.qrserver.com/v1/create-qr-code/?data=box123"})

@app.route("/chatbot_reply", methods=["POST"])
def chatbot_reply():
    data = request.get_json()
    message = data.get("message", "")
    return jsonify({"reply": f"You asked: '{message}'. This is a sample reply."})

@app.route("/qr")
def qr_page():
    return render_template("qr.html")

if __name__ == "__main__":
    app.run(debug=True)
