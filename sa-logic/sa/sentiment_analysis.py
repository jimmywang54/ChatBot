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
    sentence = request.get_json()['sentence']
    storage_adapter={
        "import_path": "chatterbot.storage.SQLStorageAdapter",
        "database_uri": "sqlite:///test.sqlite3"
    }
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
            
    polarity = bot.get_response(sentence).serialize()['text']
    # print(polarity['text'])
    # print(type(polarity))
    # polarity = TextBlob(sentence).sentences[0].polarity
    return jsonify(
        sentence=sentence,
        polarity=polarity
    )
if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)