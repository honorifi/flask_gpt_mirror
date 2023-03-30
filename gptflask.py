from flask import Flask, request, render_template
from flask_cors import CORS
import openai
openai.api_key = "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"

app = Flask(__name__)
CORS(app)

@app.route("/dc_test")
def consice_reply():
    return render_template("123.html")

# @app.route("/gpt_test")
# def gpt_test():
#     return render_template("gptmirror.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/verification", methods = ["POST"])
def verification():
    account = request.form.get("username")
    passwdd = request.form.get("password")
    veri_db = open("./database/db_test", "r").readlines()
    for line in veri_db:
        line = line.replace("\n", "")
        acc, pss = line.split(" ")
        print("acc: "+acc+"\npss: "+pss)
        print("account: "+account+"\npasswdd: "+passwdd)
        if acc == account and pss == passwdd:
            return render_template("gptmirror.html")
    return render_template("Verification_Denied.html")


@app.route("/post_test", methods = ["POST"])
def chat():
    if request.method == "POST" or request.method == "GET":
        name = request.form.get("name")
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "user", "content": name}
            ]
        )
        return completion.choices[0].message.content


if __name__ == "__main__":
#    while True:
#        reply = chat()
#        print(reply)
    app.run(host='0.0.0.0', port=81)
