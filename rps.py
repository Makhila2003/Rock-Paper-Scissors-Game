import tkinter as tk
import random

# Set up the main application window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x400")
window.config(bg="#2C3E50")  # Set background color

# Initialize scores
user_score = 0
computer_score = 0

# List of options with symbols
options = ["Rock 🪨", "Paper 📄", "Scissors ✂️"]

# Function to update game based on user's choice
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(options)
    
    # Extract plain text for comparison
    user_choice_text = user_choice.split()[0]
    computer_choice_text = computer_choice.split()[0]
    
    # Determine the outcome
    if user_choice_text == computer_choice_text:
        result = "It's a Tie!"
        result_label.config(fg="#F39C12")  # Orange color for ties
    elif (user_choice_text == "Rock" and computer_choice_text == "Scissors") or \
         (user_choice_text == "Paper" and computer_choice_text == "Rock") or \
         (user_choice_text == "Scissors" and computer_choice_text == "Paper"):
        result = "You Won!"
        result_label.config(fg="#2ECC71")  # Green color for win
        user_score += 1
    else:
        result = "You Lost!"
        result_label.config(fg="#E74C3C")  # Red color for loss
        computer_score += 1
    
    # Update the labels with the results and scores
    result_label.config(text=f"Result: {result}")
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}")

# Labels
title_label = tk.Label(window, text="Rock Paper Scissors", font=("Helvetica", 18, "bold"), fg="#ECF0F1", bg="#2C3E50")
title_label.pack(pady=20)

result_label = tk.Label(window, text="Result: ", font=("Helvetica", 16, "bold"), bg="#2C3E50")
result_label.pack()

user_choice_label = tk.Label(window, text="Your Choice: ", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
user_choice_label.pack()

computer_choice_label = tk.Label(window, text="Computer's Choice: ", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
computer_choice_label.pack()

score_label = tk.Label(window, text="Score - You: 0, Computer: 0", font=("Helvetica", 12, "bold"), fg="#ECF0F1", bg="#2C3E50")
score_label.pack(pady=20)

# Frame for buttons
button_frame = tk.Frame(window, bg="#2C3E50")
button_frame.pack(pady=20)

# Styling for buttons
button_style = {"font": ("Helvetica", 12, "bold"), "width": 10, "fg": "#ECF0F1", "bg": "#2980B9", "activebackground": "#3498DB", "activeforeground": "#ECF0F1", "bd": 0}

# Buttons with symbols
rock_button = tk.Button(button_frame, text="Rock 🪨", **button_style, command=lambda: play("Rock 🪨"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper 📄", **button_style, command=lambda: play("Paper 📄"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors ✂️", **button_style, command=lambda: play("Scissors ✂️"))
scissors_button.grid(row=0, column=2, padx=5)

# Run the application
window.mainloop()
