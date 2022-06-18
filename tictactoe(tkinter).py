import sys

try:

    try:
        
        import Tkinter as tk
        
    except:
        
        import tkinter as tk

except ImportError:
    
    print('Failed to import tkinter library')
    input('Press ENTER to exit')
    sys.exit(1)



root=tk.Tk() #Create a window

root.title('TikTakToe') #Title of the window
root.geometry('300x400+900+200') #Size of the window width x height
root.resizable(0,0) #Resizable width=false height=false
#root.overrideredirect(1) #Remove window border and title bar


pixel=tk.PhotoImage(width=1,height=1) #To define button size


header=tk.Frame(root, #Create a header frame
                height=100,
                width=300,
                bg='#ffaaaa')
header.grid_propagate(False) #Avoid resizing of frame with widget size
header.grid(row=1,column=0)


init_turn='X'
turn='' #X or O


label=tk.Label(header, #Show who's turn to play
               compound='c',
               image=pixel,
               height=45,
               width=300,
               bg='#ffaaaa',
               fg='#000000',
               font=('Verdana',15,'bold'))

label.grid(row=0,column=0)
#header.grid_rowconfigure(0,weight=1)


startBtn=tk.Button(header, #Button to start the game
                   compound='c',
                   image=pixel,
                   height=45,
                   width=300,
                   relief='flat', #Dent of the button
                   bd=0, #border width
                   bg='#ff9999',
                   activebackground='#ff8888', #bg color of the button during click
                   fg='#0000ff',
                   font=('Verdana',20,'bold'),
                   text='RESET',
                   command=lambda:reset())

startBtn.grid(row=1,column=0)
#startBtn.grid_rowconfigure(1,weight=1)

paper=tk.Frame(root, #Frame where the game is to be played
               height=300,
               width=300)

paper.grid(row=2,column=0)


win_pattern=['012','345','678','036','147','258','048','246']


class cells:
    
    def __init__(self,row,column):
        
        self.btnId=row*3+column
        
        self.btn=tk.Button(paper,
                           compound='c',
                           image=pixel,
                           height=95,
                           width=95,
                           bg='#ffffff',
                           fg='#000000',
                           font=("Verdana", 30, "bold"),
                           command=lambda:play(self))

        self.btn.grid(row=row,column=column)


playCount=0
response=[]
def reset(): #Initialize the game

    global playCount
    global response
    global turn

    playCount=0
    response=['','']
    turn=init_turn
    label['text']='Turn of '+turn
    
    for cell in paper.winfo_children():
        cell.destroy()
        
    for i in range(9):
        cells(i//3,i%3)


def play(cell): #On button click player

    global playCount
    global turn
    global response

    playCount+=1
    
    cell.btn['state']='disabled' #Disable the chicked button
    cell.btn['text']=turn #Show X or O in the clicked button

    if turn=='X': #Store the player response
        
        response[0]+=str(cell.btnId)
        winner=checkEnd(turn)
        turn='O' # Change the player (turn)
        
    else:
        
        response[1]+=str(cell.btnId)
        winner=checkEnd(turn)
        turn='X'
        
    if winner=='':
        
        if playCount==9:
            label['text']='DRAW'
        else:
            label['text']='Turn of '+turn
        
    else:
        
        label['text']=winner+' won the match!'


def checkEnd(turn): #To detect when a player wins
    
    if turn=='X':
        
        resp_index=0
        
    else:
        
        resp_index=1


    for i in win_pattern:
        
        if i[0] in response[resp_index] and i[1] in response[resp_index] and i[2] in response[resp_index]:
            
            label['text']=turn+' won the game'
            
            for cell in paper.winfo_children():
                
                cell['state']='disabled'

            return turn
        
    return ''


reset()

        
root.mainloop()#Open window
