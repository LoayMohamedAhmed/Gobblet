from tkinter import *
from tkinter import font,messagebox
from PIL import Image, ImageTk
#pip install pillow
#pip install future
class ImageButton(Button):
     def __init__(self, root, images, pos, event):
        self.position = pos
        self.images=images
        self.root = root
        self.sizes =[(35,42),(70,84),(105,128),(140,168)]
        self.func = event
        self.font = font.Font(size=20, family="Times")
        self.image = Image.open(images[-1])
        self.image = self.image.resize(self.sizes[-1])
        self.image = ImageTk.PhotoImage(image=self.image)
        self.flag=True
        self.images.pop()
        self.sizes.pop()

        super().__init__(root, image=self.image, borderwidth=0, background="black", command=self.clickFunction, highlightthickness=0)
        self.config(activebackground="black")
        self.place(relx=self.position[0], rely=self.position[1], anchor=CENTER)

        self.toggleState = 1

     def clickFunction(self, event=None):
           if self.images:

                self.image=self.images.pop()
                self.size = self.sizes.pop()
                self.image = Image.open(self.image)
                self.image = self.image.resize(self.size)
                self.image = ImageTk.PhotoImage(image=self.image)
                self.config(image=self.image)
                if not self.images and self.flag:
                     self.images.append("assets\\no more.png")
                     self.sizes.append((140,168))
                     self.flag=False
                self.func()  # Call the function passed in the 'event' parameter
           else:
                #messagebox.showinfo("peaces", "you have selected all pices")
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