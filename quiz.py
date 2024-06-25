import tkinter as tk
from tkinter import ttk
import random

# Expanded list of quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Madrid", "Paris"],
        "answer": "Paris"
    },
    {
        "question": "Which is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Mars", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "Jane Austen", "Mark Twain", "J.K. Rowling"],
        "answer": "Harper Lee"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["Monaco", "Malta", "Vatican City", "San Marino"],
        "answer": "Vatican City"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Oxygen", "Gold", "Osmium", "Oganesson"],
        "answer": "Oxygen"
    },
    {
        "question": "In what year did the Titanic sink?",
        "options": ["1912", "1905", "1923", "1918"],
        "answer": "1912"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Claude Monet", "Leonardo da Vinci", "Pablo Picasso"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"],
        "answer": "Mount Everest"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Gold", "Iron", "Diamond", "Platinum"],
        "answer": "Diamond"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")

        self.question_index = 0
        self.score = 0

        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 16), padding=10)
        self.style.configure("TButton", font=("Arial", 14), padding=10)
        self.style.configure("TRadiobutton", font=("Arial", 14), padding=10)

        # Progress bar frame
        self.progress_frame = tk.Frame(root)
        self.progress_frame.pack(pady=10)

        self.progress_labels = []
        for i in range(10):
            label = tk.Label(self.progress_frame, text=str(i+1), font=("Arial", 14), width=4, relief="solid")
            label.grid(row=0, column=i, padx=5)
            self.progress_labels.append(label)

        self.title_label = ttk.Label(root, text="General Knowledge Quiz", style="TLabel")
        self.title_label.pack(pady=10)

        self.question_label = ttk.Label(root, text="", wraplength=700, style="TLabel", justify="center")
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            btn = ttk.Radiobutton(root, text="", variable=self.options_var, value="", style="TRadiobutton")
            btn.pack(anchor="w", padx=20, pady=5)
            self.option_buttons.append(btn)

        self.next_button = ttk.Button(root, text="Next", command=self.next_question, style="TButton")
        self.next_button.pack(pady=20)

        self.score_label = ttk.Label(root, text="Score: 0", style="TLabel")
        self.score_label.pack(pady=20)

        random.shuffle(quiz_data)  # Shuffle questions at the start
        self.load_question()

    def load_question(self):
        current_question = quiz_data[self.question_index]
        self.question_label.config(text=current_question["question"])

        self.options_var.set("")
        for i, option in enumerate(current_question["options"]):
            self.option_buttons[i].config(text=option, value=option)

    def next_question(self):
        if self.options_var.get() == quiz_data[self.question_index]["answer"]:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.progress_labels[self.question_index].config(bg="green")
        else:
            self.progress_labels[self.question_index].config(bg="red")

        self.question_index += 1

        if self.question_index < len(quiz_data):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        self.question_label.config(text=f"Your final score is {self.score}/{len(quiz_data)}")
        self.options_var.set("")
        for btn in self.option_buttons:
            btn.pack_forget()
        self.next_button.pack_forget()

        self.restart_button = ttk.Button(self.root, text="Restart Quiz", command=self.restart_quiz, style="TButton")
        self.restart_button.pack(pady=20)

    def restart_quiz(self):
        self.question_index = 0
        self.score = 0
        self.score_label.config(text="Score: 0")
        random.shuffle(quiz_data)  # Reshuffle questions

        for label in self.progress_labels:
            label.config(bg="SystemButtonFace")

        self.restart_button.pack_forget()
        for btn in self.option_buttons:
            btn.pack(anchor="w", padx=20, pady=5)
        self.next_button.pack(pady=20)
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x700")  # Increased window size to fit everything
    app = QuizApp(root)
    root.mainloop()