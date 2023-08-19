#!/usr/bin/env python
# coding: utf-8

# In[20]:


import tkinter as tk
import numpy as np
import winsound
import time


# In[23]:


def play(user_choice):
    global you_score, cpu_score
    cpu_choice = np.random.choice(["Rock", "Paper", "Scissors"])
    if (
        user_choice == "Rock" and cpu_choice == "Paper"
    ) or (
        user_choice == "Paper" and cpu_choice == "Scissors"
    ) or (
        user_choice == "Scissors" and cpu_choice == "Rock"
    ): #Perdu
        msg_string = f"You chose {user_choice}\nCPU chose {cpu_choice}\nYou lost"
        cpu_score += 1
        cpu_score_label.config(text = str(cpu_score))
        res = False
        winsound.Beep(1000, 1000)
    elif user_choice == cpu_choice: #Nul
        msg_string = f"You chose {user_choice}\nCPU chose {cpu_choice}\nIt's a draw game!"
        res = None
        winsound.Beep(1500, 1000)
    else: #Gagné
        msg_string = f"You chose {user_choice}\nCPU chose {cpu_choice}\nYou won"
        you_score += 1
        you_score_label.config(text = str(you_score))
        res = True
        winsound.Beep(2000, 1000)
        
    message.config(text = msg_string)
    return res

def reset():
    global you_score, cpu_score
    intervalle = .5
    for _ in range(3):
        winsound.Beep(1000, int(intervalle * 1000))
        time.sleep(intervalle)
        
        
    you_score = 0
    you_score_label.config(text = str(you_score))
    cpu_score = 0
    cpu_score_label.config(text = str(cpu_score))
    message.config(text = "Hello")


# In[24]:


window = tk.Tk()
window.title("Rock Paper Scissors - The Game")
root = tk.Frame(master=window, bg="white")
window.geometry("400x300")

you_score = 0
cpu_score = 0

YOU_COLORS = ("#eb1a4e", "black")
CPU_COLORS = ("blue", "white")

score_frame = tk.Frame(master=root)
you_label = tk.Label(master=score_frame, text="YOU", font=("Arial", 25), bg=YOU_COLORS[0], fg=YOU_COLORS[1])
you_label.grid(row=0, column=0)

you_score_label = tk.Label(master=score_frame, text="0", font=("Arial", 25), bg=YOU_COLORS[1], fg=YOU_COLORS[0])
you_score_label.grid(row=0, column=1)

cpu_score_label = tk.Label(master=score_frame, text="0", font=("Arial", 25), bg=CPU_COLORS[1], fg=CPU_COLORS[0])
cpu_score_label.grid(row=0, column=2)

cpu_label = tk.Label(master=score_frame, text="CPU", font=("Arial", 25), bg=CPU_COLORS[0], fg=CPU_COLORS[1])
cpu_label.grid(row=0, column=3)

options_frame = tk.Frame(master=root)

rock_btn = tk.Button(master=options_frame, text="Rock", font=("Arial", 11), command=lambda : play("Rock"))
rock_btn.pack()
paper_btn = tk.Button(master=options_frame, text="Paper", font=("Arial", 11), command=lambda : play("Paper"))
paper_btn.pack()
sci_btn = tk.Button(master=options_frame, text="Scissors", font=("Arial", 11), command=lambda : play("Scissors"))
sci_btn.pack()


actions_frame = tk.Frame(master=root)
reset_btn = tk.Button(master=actions_frame, text="Reset", font=("Arial", 11), command=reset)
reset_btn.pack()
exit_btn = tk.Button(master=actions_frame, text="Exit", font=("Arial", 11), command=exit)
exit_btn.pack()


msg_frame = tk.Frame(master=root)
message = tk.Label(master=msg_frame, text='Hello')
message.pack()

score_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
options_frame.grid(row=1, column=0, rowspan=2, padx=5, pady=5)
msg_frame.grid(row=1, column=1, rowspan=2, padx=5, pady=5)
actions_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.pack()

window.mainloop()


# In[ ]:


winsound.Beep()

