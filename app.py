from flask import Flask, render_template, request, jsonify

# Delayed imports to prevent circular dependency
import logic_core
import tts_speaker

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    try:
        data = request.get_json()
        user_input = data.get("message", "").strip()
        tts = data.get("tts", False)
        gender = data.get("gender", "female")

        if not user_input:
            return jsonify({"response": "⚠️ Please enter a message."})

        response = logic_core.get_response(user_input)

        if tts:
            tts_speaker.speak(response, gender=gender)

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"response": f"❌ Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
