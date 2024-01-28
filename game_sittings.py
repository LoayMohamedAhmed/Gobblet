from tkinter import *

from button import button1
from hVSh import *
from image_label import ImageLabel
from tkinter import filedialog
from AI_mode import AI
from AIvsAI import AIvsAI

class sitting(tk.Label):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.player1_image = None
        self.player2_image = None
        self.level = {"easy":1 , "meduim" : 2, "hard": 3}
        self.selected_mode = tk.StringVar(self)
        self.selected_level = tk.StringVar(self)
        self.selected_levelAI1 = tk.StringVar(self)
        self.selected_levelAI2 = tk.StringVar(self)
        self.background1 = ImageLabel(self, image_path="assets\\gray.jpg", size=(1500,800), position=(0.5,0.5)) 
        self.player1 = button1(self, "assets\\player.png", (0.4,0.3), event=lambda: self.choose_image1(self.player1), size=(200,300))
        self.player1_txt = tk.Label(self, text="player 1", font=("Arial", 20))
        self.player1_txt.place(relx=0.4, rely=0.05, anchor='center')

        self.player2 = button1(self, "assets\\player.png", (0.6,0.3), event=lambda: self.choose_image2(self.player2), size=(200,300))
        self.player2_txt = tk.Label(self, text="player 2", font=("Arial", 20))
        self.player2_txt.place(relx=0.6, rely=0.05, anchor='center')
        self.modes =  ["1 vs 1", "1 vs AI","AI vs AI"]
        self.levels = ["easy" , "meduim" , "hard"]
        self.option_menu = tk.OptionMenu(self, self.selected_mode , *self.modes, command=self.control_mode)
        self.option_menu.config(width=20)  # Set the width of the OptionMenu
        self.option_menu.place(relx=0.5, rely=0.55, anchor='center') 
        self.selected_mode.set("select mode")
        self.selected_level.set("select level")
        self.selected_levelAI1.set("select level of AI1")
        self.selected_levelAI2.set("select level of AI2")
        self.start_b = None
    
    def choose_image1(self, player):
        # Open the file dialog and get the selected file
        self.player1_image = filedialog.askopenfilename()
        player.update_image(self.player1_image)
        
    def choose_image2(self, player):
        # Open the file dialog and get the selected file
        self.player2_image= filedialog.askopenfilename()
        # Update the image of the button
        player.update_image(self.player2_image)
    
    def control_mode(self , choice):
        if choice == "1 vs 1":
            self.start_b.destroy_button() if self.start_b != None else True
            if self.player2_image == None:
                self.player2_image = "assets\\player.png"
            if self.player1_image == None:
                self.player1_image = "assets\\player.png"
            self.start_b = button1(self,"assets\\button2.png",(0.5,0.7),event=lambda: self.master.switch_frame(PageOne ,self.player1_image ,self.player2_image),size=(150,100))
        elif choice == "1 vs AI":
            self.start_b.destroy_button() if self.start_b != None else True
            self.level_option = tk.OptionMenu(self, self.selected_level , *self.levels , command=self.control_level)
            self.level_option.config(width=20)  # Set the width of the OptionMenu
            self.level_option.place(relx=0.5, rely=0.62, anchor='center') 
            
        else:
            self.start_b.destroy_button() if self.start_b != None else True
            self.AI_level_option = tk.OptionMenu(self, self.selected_levelAI1 , *self.levels )
            self.AI_level_option .config(width=20)  # Set the width of the OptionMenu
            self.AI_level_option .place(relx=0.4, rely=0.62, anchor='center') 

            self.AI_level_option2 = tk.OptionMenu(self, self.selected_levelAI2 , *self.levels , command=self.control_levelAI1)
            self.AI_level_option2.config(width=20)  # Set the width of the OptionMenu
            self.AI_level_option2.place(relx=0.6, rely=0.62, anchor='center')
            #self.start=button1(self,"assets\\button2.png",(0.5,0.8),event=lambda: self.master.switch_frame(AIvsAI , self.level[self.selected_level]),size=(150,100))


            

    def control_level(self ,choice):
        if choice == "eaasy":
            if self.player2_image == None:
                self.player2_image = "assets\\player.png"
            if self.player1_image == None:
                self.player1_image = "assets\\player.png"
            self.start_b.destroy_button() if self.start_b != None else True
            self.start_b=button1(self,"assets\\button2.png",(0.5,0.8),event=lambda: self.master.switch_frame(AI , self.level["easy"],self.player1_image ,self.player2_image),size=(150,100))
        elif choice == "meduim":
            if self.player2_image == None:
                self.player2_image = "assets\\player.png"
            if self.player1_image == None:
                self.player1_image = "assets\\player.png"
            self.start_b.destroy_button() if self.start_b != None else True
            self.strat=button1(self,"assets\\button2.png",(0.5,0.8),event=lambda: self.master.switch_frame(AI , self.level["meduim"],self.player1_image ,self.player2_image),size=(150,100))
        else:
             if self.player2_image == None:
                self.player2_image = "assets\\player.png"
             if self.player1_image == None:
                self.player1_image = "assets\\player.png"
             self.start_b.destroy_button() if self.start_b != None else True
             self.start_b=button1(self,"assets\\button2.png",(0.5,0.8),event=lambda: self.master.switch_frame(AI , self.level["hard"],self.player1_image ,self.player2_image),size=(150,100))
    
    def control_levelAI1(self ,choice):
        if choice == "eaasy":
            self.start_b.destroy_button() if self.start_b != None else True
            self.start_b=button1(self,"assets\\button2.png",(0.5,0.8),event=lambda: self.master.switch_frame(AIvsAI , (self.level[self.selected_levelAI1.get()] ,self.level[self.selected_levelAI2.get()])),size=(150,100))
        elif choice == "meduim":
            self.start_b.destroy_button() if self.start_b != None else True
            self.start_b=button1(self,"assets\\button2.png",(0.5,0.8),event=lambda: self.master.switch_frame(AIvsAI , (self.level[self.selected_levelAI1.get()] ,self.level[self.selected_levelAI2.get()])),size=(150,100))
        else:
             self.start_b.destroy_button() if self.start_b != None else True
             self.start_b=button1(self,"assets\\button2.png",(0.5,0.8),event=lambda: self.master.switch_frame(AIvsAI , (self.level[self.selected_levelAI1.get()] ,self.level[self.selected_levelAI2.get()])),size=(150,100))

