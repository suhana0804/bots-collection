import json
import random
import nltk # natural language tool kit
import tkinter as tk
from tkinter import scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download("punkt_tab")

with open("intents.json") as file:
    data=json.load(file)

X=[]
y=[]

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        X.append(pattern)
        y.append(intent["tag"])

vectorizer=TfidfVectorizer(tokenizer=nltk.word_tokenize)
X_vec=vectorizer.fit_transform(X)

model=LogisticRegression()
model.fit(X_vec,y)

def get_response(user_input):
    input_vec=vectorizer.transform([user_input])
    prediction=model.predict(input_vec)[0]
    for intent in data["intents"]:
        if intent ["tag"]==prediction:
            return random.choice(intent["responses"])
        
class chatbotgui:
    def __init__(self,root):
        self.root=root
        self.root.title("ML Chatbot")
        self.root.geometry("500x550")

        self.chat_area=scrolledtext.ScrolledText(root,wrap=tk.WORD, state="disabled", font=("Arial",12))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_field=tk.Entry(root,font=("Arial",12))
        self.entry_field.pack(padx=10,pady=5,fill=tk.X)
        self.entry_field.bind("<Return>",self.send_message)
        send_btn=tk.Button(root,text="send",command=self.send_message,font=("Arial",12))
        send_btn.pack(pady=5)
        self.display_bot_message("Hi,I'm a chatbot.Ask me anything")
    def display_bot_message(self,msg):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END,f"bot:{msg}\n")
        self.chat_area.config(state="disabled")
        self.chat_area.yview(tk.END)
    def display_user_message(self,msg):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END,f"you:{msg}\n")
        self.chat_area.config(state="disabled")
        self.chat_area.yview(tk.END)
    def send_message(self,event=None):
        user_input=self.entry_field.get().strip()
        if user_input=="":
            return
        self.entry_field.delete(0,tk.END)
        self.display_user_message(user_input)
        response=get_response(user_input)
        self.display_bot_message(response)
if __name__ == "__main__":
    root=tk.Tk()
    app=chatbotgui(root)
    root.mainloop()