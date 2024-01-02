import pygame, tkinter
from PIL import Image, ImageTk
from random import randint

# 用pygame載入背景音樂
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)



# 以下皆為用tk做剪刀石頭布

root = tkinter.Tk()
root.title("Rock Scissors Paper game.")

# picture
rock_img = ImageTk.PhotoImage(Image.open("rock.jpg").resize((300, 300)))
paper_img = ImageTk.PhotoImage(Image.open("paper.jpg").resize((300, 300)))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.jpg").resize((300, 300)))
rockComputer_img = ImageTk.PhotoImage(Image.open("rockCom.jpg").resize((300, 300)))
paperComputer_img = ImageTk.PhotoImage(Image.open("paperCom.jpg").resize((300, 300)))
scissorComputer_img = ImageTk.PhotoImage(Image.open("scissorCom.jpg").resize((300, 300)))

root.configure(background="#C1AE8D") 

user_label = tkinter.Label(root, image=scissor_img, bg="#263f6a").grid(row=2, column=1)
comp_label = tkinter.Label(root, image=scissorComputer_img, bg="#263f6a").grid(row=2, column=5)
 
 
playerScore = tkinter.Label(root, text=0, font=("Arial",20), fg="white", bg="#C1AE8D")
computerScore = tkinter.Label(root, text=0, font=("Arial",20), fg="white", bg="#C1AE8D")
computerScore.grid(row=2, column=2)
playerScore.grid(row=2, column=4)


user_indicator = tkinter.Label(root, font=("Arial", 25), text="User", bg="#C1AE8D", fg="black")
com_indicator = tkinter.Label(root, font=("Arial", 25), text="Computer", bg="#C1AE8D", fg="black")
user_indicator.grid(row=1, column=1)
com_indicator.grid(row=1, column=5)


rock = tkinter.Button(root, width=15, height=2, bg="#C67052", text="ROCK", font=("Arial",11), command=lambda:Func("rock")).grid(row=3, column=2)
paper = tkinter.Button(root, width=15, height=2, bg="#CF9546", text="PAPER", font=("Arial",11), command=lambda:Func("paper") ).grid(row=3, column=3)
scissor = tkinter.Button(root, width=15, height=2,bg="#849271", text="SCISSOR", font=("Arial",11), command=lambda:Func("scissor") ).grid(row=3, column=4)

msg = tkinter.Label(root, font=("Arial", 15), bg="#C1AE8D", fg="black")
msg.grid(row=2, column=3)


# check winner
def checkWin(player, computer):
    if player == computer:
        updateMsg("平手")
        
    elif player == "rock":
        if computer == "paper":
            updateMsg("輸了 可惜")
            compScore()
        else:
            updateMsg("贏了欸 恭喜")
            userScore()
    elif player =="paper":
        if computer =="scissor":
            updateMsg("輸了 可惜")
            compScore()
        else:
            updateMsg("贏了欸 恭喜")
            userScore()
    elif player == "scissor":
        if computer =="rock":
            updateMsg("輸了 可惜")
            compScore()
        else:
            updateMsg("贏了欸 恭喜")
            userScore()
    else:
        pass


# Score Function
def updateMsg(x):
    msg["text"] = x

def userScore():
    userscore = int(playerScore["text"])
    userscore+=1
    playerScore["text"] = str(userscore)
    
def compScore():
    compscore = int(computerScore["text"])
    compscore+=1
    computerScore["text"] = str(compscore)
        
        
# Choice function
choice=["rock", "paper", "scissor"]
def Func(x):
    comChoice = choice[randint(0,2)]
    checkWin(x, comChoice) 
    global comp_label, user_label
    
    
    if comChoice=="rock":
        comp_label = tkinter.Label(root, image=rockComputer_img, bg="#263f6a").grid(row=2, column=5)
    elif comChoice=="paper":
        comp_label = tkinter.Label(root, image=paperComputer_img, bg="#263f6a").grid(row=2, column=5)
    else:
        comp_label = tkinter.Label(root, image=scissorComputer_img, bg="#263f6a").grid(row=2, column=5)
        
    if x=="rock":
        user_label = tkinter.Label(root, image=rock_img, bg="#263f6a").grid(row=2, column=1)
    elif x=="paper":
        user_label = tkinter.Label(root, image=paper_img, bg="#263f6a").grid(row=2, column=1)
    else:
        user_label = tkinter.Label(root, image=scissor_img, bg="#263f6a").grid(row=2, column=1)

root.mainloop()