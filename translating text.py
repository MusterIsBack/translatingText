#translating text with googletrans API

#importing google translate API
import googletrans
from googletrans import Translator

while(True):
    transing = Translator()
    #asking user
    text1 = input("what's your text? ")
    lang = input("what language suould it be translated? ")

    #print and show the result
    print ("The rusult is: | " + transing.translate("{}" .format(text1) , '{}' .format(lang)).text + " |")
    ques = input("wanna try again?")
    if ques == 'yes':
        continue
    else:
        break