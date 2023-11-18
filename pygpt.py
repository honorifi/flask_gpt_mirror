from flask import Flask
from flask import request
from flask_cors import CORS
import openai
openai.api_key = "enter your own api_key requested from openai"

app = Flask(__name__)
CORS(app, resource=r'/*')

@app.route("/post_test", methods=["POST"])
def chat():
    name = input("\n")
    #if request.method == "POST":
    if name != "" : 
    #    name = request.form.get("name")
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "user", "content": name}
            ]
        )
        return completion.choices[0].message.content


if __name__ == "__main__":
    while True:
        reply = chat()
        print(reply)
#    app.run(host='0.0.0.0', port=81)
