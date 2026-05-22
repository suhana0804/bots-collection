import tkinter as tk
def bot_response(user_text):
    user_text=user_text.lower()
    if user_text in ("hi", "hii", "hello"):
        return "Hello! How can I help you today?"
    elif user_text=="bye":
        return "Goodbye! Have a great day."
    elif user_text in ("thank you", "thanks"):
        return "You're welcome!"
    elif user_text in ("How do I show a text as an output in python?"):
        return "Use the function print().Place the text you want to print in the bracket."
    elif user_text in ("What function to use for asking questions to the user?"):
        return "Use the function input().Place the text you want to ask in the bracket."
    elif user_text in ("What are the data types in python?"):
        return "There are many data types in python. For example: str()- acts like a text,int()- takes only integer,float()-takes decimal values."
    elif user_text in ("How do I know which one is a list or a tuple?"):
        return "The biggest visual difference is,list as square brakets([]) and tuple has normal brakets()."
    elif user_text in ("Is it possible to write conditional statements like in other progamming languages?"):
        return "Yes, ofcourse! You can use if and else conditions. Want to know more in detail?"
    elif user_text in ("I like coding and biology. Are there jobs which combine these two subjects?"):
        return "Yes there are many!. The most popular ones are Bioinformatics and Biotechnology."
    elif user_text in ("I want my code to keep on running straight for 5 times. What do I do?"):
        return "You can use for loop. Type-for i #(a variabble) in range(0,6): Do you want me to explain in detail and also know about while loop?"
    else:
        return "Sorry, I didn't understand that."
def send_message():
    user_text=d.get()       
    c.insert(tk.END,f"You:{user_text}\n")
    bot_reply=bot_response(user_text)
    c.insert(tk.END,f"Bot:{bot_reply}\n")   
a=tk.Tk()
a.title("Chatbot")
a.geometry("500x500")
a.config(bg="lightblue")
b=tk.Label(a,text=" Python Chatbot",bg="black",fg="white",font=("Algerian", 24))
c=tk.Text(a,width=60, height=20)
d=tk.Entry(a,width=40)
e=tk.Button(a,text="Send",command=send_message)
b.pack()
c.pack()
d.pack()
e.pack()     
a.mainloop()

