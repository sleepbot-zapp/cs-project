from random import choice
from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

database={'sleepbot':'123'}

msgs = []
msg2 = []

@app.route('/chat')
def chat_render():
    return render_template("chat.html")

@app.route("/chat", methods=['POST'])
def chat():
    text = request.form["text"]
    BOT_MSGS = [
        "Hi, how are you?",
        "Ohh... I can't understand what you trying to say. Sorry!",
        "I like to play games... But I don't know how to play!",
        "Sorry if my answers are not relevant. :))",
        "I feel sleepy! :("
    ]
    now = datetime.now()
    msgs.append(text)
    msg2.append(choice(BOT_MSGS))
    return render_template("chat.html", data=zip(msgs,msg2), time=now.strftime("%H:%M"))

"""
@app.route('/login', methods=['POST','GET'])
def login():
    name=request.form['username']
    pwd=request.form['password']
    if name not in database:
        return render_template('login.html',info='⚠️ Invalid User')
    else:
        if database[name]!=pwd:
            return render_template('login.html',info='⚠️ Invalid Password')
        else:
            return render_template('home.html',name=name)
"""

if __name__ == '__main__':
    app.run(debug=True)
