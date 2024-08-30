import tkinter as t
import random
def computer_input():
    return random.choice(['rock', 'paper', 'scissors'])
def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "The Computer wins!"
def user_input(user_choice):
    computer_choice = computer_input()
    result = winner(user_choice, computer_choice)
    user_label.config(text=f"You chose: {user_choice.capitalize()}")
    computer_label.config(text=f"Computer chose: {computer_choice.capitalize()}")
    result_label.config(text=result)
#Window creating
window = t.Tk()
window.title("Rock, Paper, Scissors")
frame1 = t.Frame(window, padx=20, pady=20,bg='peach puff')
frame1.pack(fill=t.BOTH, expand=True)
label1 = t.Label(frame1, text="Rock  Paper  Scissors", font=("Helvetica", 20, "bold"),bg='antique white')
label1.pack(pady=10)
user_label = t.Label(frame1, text="Make your choice!", font=("Helvetica", 14), bg="lightblue", width=25)
user_label.pack(pady=5)
computer_label = t.Label(frame1, text="", font=("Helvetica", 14), bg="lightgreen", width=25)
computer_label.pack(pady=5)
result_label = t.Label(frame1, text="", font=("Helvetica", 16, "bold"), bg="lightcoral", width=21)
result_label.pack(pady=5)
frame2 = t.Frame(frame1,bg='peach puff')
frame2.pack(side=t.BOTTOM, pady=10, fill=t.X)
b1=t.Button(frame2, text="Rock", command=lambda: user_input('rock'), bg="ivory2", width=10)
b2=t.Button(frame2, text="Paper", command=lambda: user_input('paper'), bg="ivory2", width=10)
b3=t.Button(frame2, text="Scissors", command=lambda: user_input('scissors'), bg="ivory2", width=10)
b1.pack(side=t.LEFT,padx=10)
b2.pack(side=t.LEFT,padx=10)
b3.pack(side=t.LEFT,padx=10)
window.mainloop()