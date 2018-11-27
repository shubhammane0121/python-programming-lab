# Shubham Mane
#Gr-11810247
#roll no- M-38
#Division-M
from easygui import *
import sys
while 1:
    msgbox("wel come to shopping world")

    msg ="from where you wanted buy?"
    title = "welcome to shopping site world"
    choices = ["Amazon", "Flipkart", "Myntra"]
    choice = choicebox(msg, title, choices)

    msgbox("You chose: " + str(choice), "Survey Result")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)
        if choice=='Amazon':
            msg1 ="your choice is Amazon"
            title1 = "Amazon"
            choices1 = ["Electronic", "Fashion", "Automobiles"]
            choice1 = choicebox(msg, title, choices)

            msgbox("You chose: " + str(choice), "Survey Result")

            msg = "Do you want to continue?"
            title = "Please Confirm"
            if ccbox(msg, title):     # show a Continue/Cancel dialog
             pass  # user chose Continue
            else:
              sys.exit(0)
              
