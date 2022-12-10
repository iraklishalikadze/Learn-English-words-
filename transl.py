from googletrans import Translator
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
word = Translator()

def split_text():
    with open("data.txt") as data:
        text = data.read()
        text_list = text.split()
    engl_dic = [{"English":engli_word, "Georgia":word.translate(engli_word, dest="ka").text} for engli_word in text_list]
    pandas.DataFrame(engl_dic).to_csv("words.csv")

window = Tk()
window.title("flashe")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas( width=800, height=526 )
begrownd_one = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=begrownd_one)
canvas.grid(row=0, column=0)

canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))




window.mainloop()

