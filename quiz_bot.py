import tkinter as tk          # import tkinter for GUI
from tkinter import messagebox     # import messagebox for showing dialog box messages

quiz_data=[           # list of question and answers
    {"question":"what is the capital of India?",
     "options":["delhi","pune","mumbai","chennai"],
     "answer":"delhi"
    },
    {"question":"which planet is known as the red planet?",
     "options":["earth","mars","saturn","neptune"],
     "answer":"mars"
    },
    {"question":"what is the hardest natural substance on earth?",
     "options":["carbon","graphite","diamond","gold"],
     "answer":"diamond"
    },
    {"question":"what is the largest organ in the human body?",
     "options":["heart","brain","lungs","skin"],
     "answer":"skin"
    },
    {"question":"how many continents are there in the world?",
     "options":["7","6","5","4"],
     "answer":"7"
    }
]
class Quiz_bot:  # define the main class
   def __init__(self,root):  # constructor: start working when some object is created 
       self.root=root       # main window
       self.root.title("Quiz bot") # window title
       self.root.geometry("500x400") # window size
       self.score=0   # score is 0
       self.q_index=0 # check what question we are on:start from 1st
       self.selected_answer = tk.StringVar() # save the selected radio button

       self.area=tk.Text(root,height=15,width=55,state="disabled",wrap="word") # create a text widget to show the q&a
       self.area.pack(pady=10) # place the widget on the screen by vertical spacing of 10
       self.options=tk.Frame(root) # create a frame(a page) on the window
       self.options.pack()  # place the widget on the screen
       self.next=tk.Button(root,text="next", command=self.next_question) # button that calls next_question when clicked
       self.next.pack(pady=10) # place the widget on the screen by vertical spacing of 10
       self.show_question() # call the function to display the 1st question

   def insert_area(self,text): # define the function for putting the messages on the text widget
       self.area.config(state="normal") # allow editing on the widget
       self.area.insert(tk.END,text+"\n") # insert the message
       self.area.config(state="disabled") # disable editing
       self.area.see(tk.END) # show the latest message
   def show_question(self): # function to display the current question and its options
      for i in self.options.winfo_children():
           i.destroy() # clear old radio buttons (previous question’s options)
      if self.q_index<len(quiz_data): # check if any more questions are left
           q_data=quiz_data[self.q_index] # take the index of that specific question
           self.insert_area(f"bot:{q_data["question"]}") #
           self.selected_answer.set(None)
           for option in q_data["options"]:
               rb=tk.Radiobutton(self.options,text=option,variable=self.selected_answer,value=option)
               rb.pack(anchor="w")
      else:
           self.show_result()
   def next_question(self):
       if self.q_index<len(quiz_data):
           selected=self.selected_answer.get()
           if selected=="":
               messagebox.showwarning("warning","please select an option")
               return
           q_data=quiz_data[self.q_index]
           if selected==q_data["answer"]:
               self.score+=1
               self.insert_area("you:"+selected)
               self.insert_area("bot:correct")
           else:
               self.insert_area("you: "+selected)
               self.insert_area(f"bot: wrong! correct answer:{q_data["answer"]}")
           self.q_index+=1
           self.show_question()
   def show_result(self):
       self.insert_area(f"bot:quiz over! your score:{self.score}/{len(quiz_data)}")
       self.next.config(state="disabled")
if __name__ == "__main__" :
    root=tk.Tk()
    app=Quiz_bot(root)
    root.mainloop()




