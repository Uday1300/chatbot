from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from clean import clean_corpus

chatbot = ChatBot("Chatbot")
trainer = ListTrainer(chatbot)
corpus_file = "chat.txt"

cleaned_corpus = clean_corpus(corpus_file)

if isinstance(cleaned_corpus, list):
    trainer.train(cleaned_corpus)
else:
    print("Error: clean_corpus should return a list of conversations.")

exit_condition = ("q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_condition:
        break
    else:
        print(f"{chatbot.get_response(query)}")
