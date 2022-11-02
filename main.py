from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
# -------------------------- Next card -------------------

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(current_bg, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


# ----------------------- Flip card --------------------------

def flip_card():
    canvas.itemconfig(current_bg, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# -------------------------- UI --------------------------------------#


window = Tk()
window.title("Flashcard Program")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
current_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_button = Button(image=right_img, command=next_card)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_img, command=next_card)
wrong_button.grid(column=1, row=1)

next_card()

window.mainloop()

