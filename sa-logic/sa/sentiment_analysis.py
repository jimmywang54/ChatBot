from flask import Flask, request, jsonify

# Chatbot
from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

 


app = Flask(__name__)


@app.route("/testHealth") 
def hello():
    return "Hello World!"

@app.route("/analyse/chatbot", methods=['POST'])
def analyse_sentiment():
    question = request.get_json()['question']
    bot= ChatBot('Bot')
    trainer = ChatterBotCorpusTrainer(bot)

    corpus_path = './english/'

    for file in os.listdir(corpus_path):
        trainer.train(corpus_path + file)
            
    answer = bot.get_response(question).serialize()['text']
    
    return jsonify(
        question=question,
        answer=answer
    )
if __name__ == '__main__': app.run(host='0.0.0.0', port=8080)