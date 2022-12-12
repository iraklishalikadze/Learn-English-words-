from googletrans import Translator
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
choice_one = {}
word = Translator()

def split_text():
    global data_list
    with open("data.txt") as data:
        text = data.read()
        text_list = text.split()
    engl_dic = [{"English":engli_word, "Georgia":word.translate(engli_word, dest="ka").text} for engli_word in text_list]
    pandas.DataFrame(engl_dic).to_csv("words.csv", index=False)
    data_list = pandas.DataFrame(pandas.read_csv("words.csv")).to_dict('records')
    random_word()


def random_word():
    global choice_one, flip_timer
    window.after_cancel(flip_timer)
    choice_one = random.choice(data_list)
    canvas.itemconfig(languaje_text, text="English")
    canvas.itemconfig(translate_text, text=choice_one["English"])
    flip_timer = window.after(3000,translate_word)
    print(len(data_list))

def translate_word():
    canvas.itemconfig(languaje_text, text="Georgia")
    canvas.itemconfig(translate_text, text=choice_one["Georgia"])

def know_word():
    data_list.remove(choice_one)
    print(len(data_list))
    pandas.DataFrame(data_list).to_csv("words.csv", index=False)
    random_word()




window = Tk()
window.title("flashe")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,translate_word)

canvas = Canvas( width=800, height=526 )
begrownd_one = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=begrownd_one)
canvas.grid(row=0, column=0, columnspan=3)

languaje_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
translate_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=1)

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=know_word)
right_button.grid(row=1, column=2)

split_button = Button(bg="red", text="Split", width=10, font=("Ariel", 30, "italic"), command=split_text)
split_button.grid(row=1, column=0)


data_list = pandas.DataFrame(pandas.read_csv("words.csv")).to_dict('records')

random_word()

window.mainloop()

