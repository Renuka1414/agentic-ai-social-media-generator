from flask import Flask, render_template, request
from social_agents import generate_content
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        topic = request.form.get("topic")
        platform = request.form.get("platform")

        if topic:
            result = generate_content(topic, platform)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
