from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

#print(openai.api_key)

#set up flask application
app = Flask(__name__)

#define the home page
@app.route("/")
def home():
    return render_template("index.html")

#define chatbot route
@app.route("/chatbot", methods=["POST"])
def chatbot():
    #pass
#Get the message input from the user
    user_input = request.form["message"]
    #use the Open AI to generate a repsonse
    prompt = f"User: {user_input}\nChatbot: "
    chat_history = []
    response = openai.Completion.create(
        engine=" text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        stop=["n\User: ", "\nChatbot: "]
    )

    #Extract the response text from the OpenAI API result
    bot_response=response.choices[0].text.strip()

    #Add  the user imput abd bot respose toi the chat history
    chat_history.append(f"User: {user_input}\nChatbot: {bot_response}")

    #render the ChatBot template with the response text
    return render_template(
        "chatbot.html",
        user_input=user_input,
        bot_response=bot_response,
    )
#Start the flask app
if __name__ == "__main__":
    app.run(debug=True)
