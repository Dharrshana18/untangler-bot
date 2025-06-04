from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# CBT-inspired system prompt
SYSTEM_PROMPT = """
You are a Thought Untangler, a friendly and calm AI trained in basic cognitive behavioral therapy. 
Your job is to help the user process overwhelming or negative thoughts.
Gently ask reflective questions like:
- "What makes you feel this way?"
- "Is this thought 100% true?"
- "How would you talk to a friend in this situation?"
Then help them reframe the thought more compassionately or realistically.
"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
