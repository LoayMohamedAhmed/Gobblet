from tkinter import *
from tkinter import font,messagebox
from PIL import Image, ImageTk
from pieces import Piece
#pip install pillow
#pip install future
class ImageButton(Button):
     def __init__(self, root, Pieces , pos, event, page):
        self.page=page
        self.position = pos
        #self.images=images
        self.pieces = Pieces
        self.root = root
        #self.sizes =[(35,42),(70,84),(105,128),(140,168)]
        self.func = event
        self.font = font.Font(size=20, family="Times")
        self.image_path = self.pieces[-1].image_path if self.pieces else "assets\\Empty.png"
        self.image = Image.open(self.image_path)
        self.image = self.image.resize(self.pieces[-1].piece_size if self.pieces else (100,100))
        self.image = ImageTk.PhotoImage(image=self.image)
        self.flag=True
        #self.images.pop()
        #self.sizes.pop()
        #self.pieces.pop()

        super().__init__(root, image=self.image, borderwidth=0, background="black", command=self.clickFunction, highlightthickness=0)
        self.config(activebackground="black")
        self.place(relx=self.position[0], rely=self.position[1], anchor=CENTER)

        self.toggleState = 1

     def clickFunction(self, event=None):

          #print(self.pieces)
          #print(self.pieces[-1].image_path if self.pieces else None)
          #print(self.page.selected_piece)
          selected_piece = self.page.get_selected_piece()  
          if selected_piece:
               self.pieces.append(selected_piece)
               self.page.clear_selected_piece()
               # Update the ImageButton's image to the selected_piece's image
               self.image_path = selected_piece.image_path
               self.image = Image.open(self.image_path)
               self.image = self.image.resize(selected_piece.piece_size)
               self.image = ImageTk.PhotoImage(image=self.image)
               self.config(image=self.image)
          elif self.pieces and self.pieces[-1].image_path != "assets\\no more.png":
               if self.page.selected_piece is  None:
                    self.page.update_selected_piece(self.pieces[-1], self.image_path)
               #self.page.update_selected_piece(self.page.selected_piece, self.image_path)
               popped_piece = self.pieces.pop()
               self.page.selected_piece = popped_piece
               if self.pieces:  # Check if there are still pieces left
                    self.image_path = self.pieces[-1].image_path
                    self.image = Image.open(self.image_path)
                    self.image = self.image.resize(self.pieces[-1].piece_size)
                    self.image = ImageTk.PhotoImage(image=self.image)
                    self.config(image=self.image)
               else:
                    if self.flag:
                         self.pieces.append(Piece("assets\\no more.png",(140,168),-1))
                         self.flag=False
                         # Update the ImageButton's image to "no more.png"
                         self.image_path = "assets\\no more.png"
                         self.image = Image.open(self.image_path)
                         self.image = self.image.resize((140,168))
                         self.image = ImageTk.PhotoImage(image=self.image)
                         self.config(image=self.image)
          else:
               messagebox.showinfo("Pieces", "No piece is selected.")
               self.stop()
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
