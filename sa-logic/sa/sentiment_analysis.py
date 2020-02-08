from flask import Flask, request, jsonify

# Chatbot
from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

 


app = Flask(__name__)


@app.route("/testHealth") 
def hello():
    return "Hello World!"

@app.route("/analyse/sentiment", methods=['POST'])
def analyse_sentiment():
    question = request.get_json()['question']
    bot= ChatBot('Bot')
    trainer = ChatterBotCorpusTrainer(bot)

    corpus_path = './english/'

    for file in os.listdir(corpus_path):
        trainer.train(corpus_path + file)

    # while True:
    #    message = input('You:')
    #    print(message)
    #    if message.strip() == 'Bye':
    #        print('ChatBot: Bye')
    #        break
    #    else:
    #        reply = bot.get_response(message)
    #        print('ChatBot:', reply)
            
    answer = bot.get_response(question).serialize()['text']
    # print(polarity['text'])
    # print(type(polarity))
    # polarity = TextBlob(sentence).sentences[0].polarity
    return jsonify(
        question=question,
        answer=answer
    )
if __name__ == '__main__': app.run(host='0.0.0.0', port=5003)