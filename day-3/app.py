from flask import Flask, render_template, request
from nltk.chat.util import Chat

que1 = r'how are you'
answers1 = [
    'all well',
    'I am good',
    'awesome'
]

que2 = r'what can you do'
answers2 = [
    'i can reply to your queries',
    'I am here to answer you questions',
    'I can chat with you'
]

que3 = r'what is your name'
answers3 = [
    ' my name is chatty',
    'i am chatty'
]

que4 = r'kya aaj barish hogi'
answers4 = [
    'its look like it will rain today',
    'baarish ka mausam he',
    'baarish ho sakti he mausam kharaab he'
]
# question answer pairs
qa_pair = [
    (que1, answers1),
    (que2, answers2),
    (que3, answers3),
    (que4, answers4),
]

chatbot = Chat(qa_pair)

app = Flask(__name__)

@app.route('/')
def home():
    global chatbot
    query = request.args.get('query')
    if query !=None:
        response =chatbot.respond(query)
        if response==None:
           response = 'Sorry I am not sure'
    else:
        response =''
    return render_template('index.html' , result=response)

@app.route('/chatbot')
def chat():
    return "<h2>Chat Bot</h2>"

app.run(debug = True)