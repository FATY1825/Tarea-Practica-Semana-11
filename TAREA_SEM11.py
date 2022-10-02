#import PIL
from distutils.cmd import Command
from email import message
import tkinter
from PIL import Image, ImageTk
from cProfile import label
from PIL import Image, ImageFilter

from tkinter import PhotoImage, Tk, Button, Label, filedialog, messagebox

#Se crea una ventana y se le da el tamaño y se configura el color de fondo y se le da un titulo a la ventana
ventana=Tk()
ventana.geometry("550x300")
ventana.title("Imagen")
ventana.configure(bg="light pink")

#Se crea un label que mostrara la imagen que se cargara
label2 =Label(ventana, image="")

#Se crea una funcion para cargar la imagen desde los archivos y dentro de esta se le da las medidas y 
#se ubican en la ventana
def cargar():
    archivo = filedialog.askopenfilename()
    global imagen4
    imagen4 = Image.open(archivo)
    imagenrezis2 = imagen4.resize((200,200),Image.Resampling.LANCZOS)
    render2 =ImageTk.PhotoImage(imagenrezis2)
    label2.configure(image=render2)
    label2.image_names =render2
    label2.place(x=70, y=30)

#Se creo una funcion para poner el filtro de desenfoque junto con un messagebox para indicar que el filtro fue
#aplicado
def desenfocar():
    imagendesen= imagen4
    imagendesen= imagendesen.filter(ImageFilter.BoxBlur(20)) 
    messagebox.showinfo('PIL',"La imagen ha sido desenfocada")
    imagendesen.save("imagendes.png")
    imagendesen.show()
   
#Se crea una funcion para poner el filtro de contorno
def Contorno():
    imagencon= imagen4
    imagencon = imagencon.filter(ImageFilter.CONTOUR)
    messagebox.showinfo('PIL',"Se ha aplicado el contorno a la imagen")
    imagencon.save("imagecontorno.png")  
    imagencon.show()

#Se creo otra funcion para el filtro de Resaltar
def Resaltar():
    imagenresal= imagen4
    imagenresal= imagenresal.filter(ImageFilter.EMBOSS)
    messagebox.showinfo('PIL',"Se ha resaltado la imagen")
    imagenresal.save("imagenresal.png") 
    imagenresal.show()

#Se creo una ultima funcion para convertir de Color a B/N
def convertir():
    imagen3 = imagen4
    imagen3bn =imagen3.convert("L")
    messagebox.showinfo('PIL',"La imagen se ha convertido en B/N")
    imagen3bn.save("Blanco_negro.png")
    imagen3bn.show()


#Se crea un boton que permite guardar la imagen en blanco y negro y se le da un color y sus medidas
btn2 =Button(ventana, text="GUARDAR IMAGEN B/N", command=convertir)
btn2.configure(bg="thistle")
btn2.place(x=20, y=245)

#Se crea un boton que permite cargar la imagen en la ventana se le da un color y sus medidas
btn3 =Button(ventana, text="CARGAR IMAGEN", command=cargar)
btn3.configure(bg="thistle")
btn3.place(x=360, y=120)

#Se crea un boton que permite guardar la imagen desenfocada y se le da un color y sus medidas
btn4 =Button(ventana, text="DESENFOCAR IMAGEN", command=desenfocar)
btn4.configure(bg="thistle")
btn4.place(x=160, y=245)

#Se crea un boton que permite guardar la imagen del contorno y se le da un color y sus medidas
btn5 =Button(ventana, text="CONTORNO IMAGEN", command=Contorno)
btn5.configure(bg="thistle")
btn5.place(x=296, y=245)

#Se crea un boton que permite guardar la imagen que se resalto y se le da un color y sus medidas
btn6 =Button(ventana, text="RESALTAR IMAGEN", command=Resaltar)
btn6.configure(bg="thistle")
btn6.place(x=425, y=245)

#Hacemos un label para nuestros nombres
mair = tkinter.Label(ventana, text = "Maira Liseth Ramos Parada -SMIS012921")
mair.place(x=10, y=0)
fati = tkinter.Label(ventana, text = "Fatima del Carmen Ayala Santos -SMIS003321")
fati.place(x=240, y=0)
#Se llama a la ventana
ventana.mainloop()
