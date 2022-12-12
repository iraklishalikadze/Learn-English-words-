from googletrans import Translator
import pandas
word = Translator()
text_list = ["longest-serving,", "home"]
engl_dic = [{"English":engli_word, "Georgia":word.translate(engli_word, dest="ka").text} for engli_word in text_list]
print(engl_dic)
print(1)
print(2)
print(3)

