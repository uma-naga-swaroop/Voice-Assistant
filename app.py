import webbrowser
from flask import Flask, render_template, request, jsonify
import webbrowser

app = Flask(__name__)  


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/command", methods=["POST"])
def command():
    data = request.json
    user_command = data.get("command")

    print("Received:", user_command)

    try:
        from commands import execute_command
        execute_command(user_command)
    except Exception as e:
        print("Error:", e)

    return jsonify({"status": "ok"})



if __name__ == "__main__":
    print("Starting Flask server...")
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=False)