from tkinter import *
from tkinter import font,messagebox
from PIL import Image, ImageTk
from pieces import Piece

#pip install pillow
#pip install future
class ImageButton(Button):
     def __init__(self, root, Pieces , pos, event , Btype):
        self.position = pos
        self.page = root
        self.pieces = Pieces
        self.root = root
        self.func = event
        self.Btype = Btype
        self.font = font.Font(size=20, family="Times")
        self.image = Image.open(self.pieces[-1].image_path)
        self.image = self.image.resize(self.pieces[-1].piece_size)
        self.image = ImageTk.PhotoImage(image=self.image)
        self.flag=True

        super().__init__(root, image=self.image, borderwidth=0, background="black", command=self.clickFunction, highlightthickness=0)
        self.config(activebackground="black")
        self.place(relx=self.position[0], rely=self.position[1], anchor=CENTER)

        self.toggleState = 1

     def clickFunction(self, event=None):
               
               if self.page.selected_piece !=None and self.Btype == "board":
                    self.pieces.append(self.page.selected_piece)
                    self.page.selected_piece = None
                    self.page.change_turn()
                    self.page.chose()
                    self.page.select_piece(None)

               else:
                    if self.pieces:
                         self.current_piece = self.pieces[-1]
                         if self.current_piece.player == self.page.player_turn and self.page.played:
                              self.page.chose()
                              self.page.select_piece(self.pieces[-1]) 
                              self.pieces.pop()
                    

               if self.pieces:
                    self.image=self.pieces[-1].image_path
                    self.size = self.pieces[-1].piece_size
                    
                    self.image = Image.open(self.image)
                    self.image = self.image.resize(self.size)
                    self.image = ImageTk.PhotoImage(image=self.image)
                    self.config(image=self.image)
                    self.func()  # Call the function passed in the 'event' parameter
               elif self.flag:
                    self.image = Image.open("assets\\no more.png" if self.Btype =="player" else "assets\\gray.jpg")
                    self.image = self.image.resize((150,150))
                    self.image = ImageTk.PhotoImage(image=self.image)
                    self.config(image=self.image)
                    self.flag = False
               else:
                    messagebox.showinfo("peaces", "you have selected all pices") if self.Btype =="player" else True
                    self.stop() if self.Btype =="player" else True
     def stop(self):
          # Create a new window
          top = Toplevel()
          top.title("stop")
          top.geometry('%dx%d+%d+%d' % (500, 300,500,300))
          # Open the image file
          img = Image.open('assets\\stop.jpg')
          img = img.resize((500,300))
          # Convert the image file to a PhotoImage object
          img = ImageTk.PhotoImage(img)
          
          # Create a label with the image
          label = Label(top, image=img)
          label.image = img  # keep a reference!

          # Display the label
          label.pack()
     
