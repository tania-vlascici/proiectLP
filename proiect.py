from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window
root = Tk()
root.title("piatra hartie foarfeca")
root.configure(background="#9b59b6")

# picture
piatra_img = ImageTk.PhotoImage(Image.open("piatra-user.png"))
hartie_img = ImageTk.PhotoImage(Image.open("hartie-user.png"))
foarfeca_img = ImageTk.PhotoImage(Image.open("foarfeca-user.png"))
piatra_img_comp = ImageTk.PhotoImage(Image.open("piatra.png"))
hartie_img_comp = ImageTk.PhotoImage(Image.open("hartie.png"))
foarfeca_img_comp = ImageTk.PhotoImage(Image.open("foarfeca.png"))

# insert picture
user_label = Label(root, image=foarfeca_img, bg="#9b59b6")
comp_label = Label(root, image=foarfeca_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# scores
playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# indicators
user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER",
                       bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

# buttons
piatra = Button(root, width=20, height=2, text="PIATRA",
                bg="#FF3E4D", fg="white", command=lambda: updateChoice("piatra")).grid(row=2, column=1)
hartie = Button(root, width=20, height=2, text="HARTIE",
                bg="#FAD02E", fg="white", command=lambda: updateChoice("hartie")).grid(row=2, column=2)
foarfeca = Button(root, width=20, height=2, text="FOARFECA",
                  bg="#0ABDE3", fg="white", command=lambda: updateChoice("foarfeca")).grid(row=2, column=3)


# update message


def updateMessage(x):
    msg['text'] = x


# update user score


def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)


# update computer score


def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)


# check winner


def checkWin(player, computer):
    if player == computer:
        updateMessage("Este egalitate!!!")
    elif player == "piatra":
        if computer == "hartie":
            updateMessage("Tu ai pierdut!")
            updateCompScore()
        else:
            updateMessage("Tu ai castigat!")
            updateUserScore()
    elif player == "hartie":
        if computer == "foarfeca":
            updateMessage("Tu ai pierdut!")
            updateCompScore()
        else:
            updateMessage("Tu ai castigat!")
            updateUserScore()
    elif player == "foarfeca":
        if computer == "piatra":
            updateMessage("Tu ai pierdut!")
            updateCompScore()
        else:
            updateMessage("Tu ai castigat!")
            updateUserScore()

    else:
        pass


# update choices

choices = ["piatra", "hartie", "foarfeca"]


def updateChoice(x):
    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "piatra":
        comp_label.configure(image=piatra_img_comp)
    elif compChoice == "hartie":
        comp_label.configure(image=hartie_img_comp)
    else:
        comp_label.configure(image=foarfeca_img_comp)

    # for user
    if x == "piatra":
        user_label.configure(image=piatra_img)
    elif x == "hartie":
        user_label.configure(image=hartie_img)
    else:
        user_label.configure(image=foarfeca_img)

    checkWin(x, compChoice)




root.mainloop()
