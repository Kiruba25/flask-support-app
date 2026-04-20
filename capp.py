from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {}

# Simple auto reply
def bot_reply(msg):
    msg = msg.lower()

    if any(word in msg for word in ["hi", "hello", "hey"]):
        return "👋 Hello! How can I assist you today?"

    elif "order" in msg:
        return "📦 Please provide your Order ID."

    elif "refund" in msg:
        return "💰 Your refund will be processed within 3-5 days."

    elif "delay" in msg:
        return "⏳ Sorry for the delay. We are checking your order status."

    elif "thanks" in msg:
        return "😊 You're welcome!"

    else:
        return "🤖 I didn’t understand. Our support team will contact you."

# Login page
@app.route('/')
def login():
    return render_template("login.html")

# Signup
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == "POST":
        users[request.form['username']] = request.form['password']
        return redirect(url_for('login'))
    return render_template("signup.html")

# Support page
@app.route('/support', methods=['POST'])
def support():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return render_template("support.html")
    return "Invalid Login"

# Chat API
@app.route('/chat', methods=['POST'])
def chat():
    msg = request.form['message']
    return bot_reply(msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)