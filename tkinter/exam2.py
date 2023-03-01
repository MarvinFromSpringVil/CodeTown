import tkinter as tk 
import cv2
from PIL import Image, ImageTk

# prepare image
width = 320; height = 240
color_image = cv2.imread('image.png')
color_image = cv2.resize(color_image, (width, height))
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY )

# window 
window=tk.Tk()
window.title("My First GUI")
window.geometry("{}x{}+100+100".format(width, height+40))

# function1: convert numpy image into tk image 
def np_image_to_tk_image(np_image):
	img = cv2.cvtColor(np_image, cv2.COLOR_BGR2RGB)
	img = Image.fromarray(img)
	imgtk = ImageTk.PhotoImage(image=img)
	return imgtk

# lable 
imgtk = np_image_to_tk_image(color_image)
label = tk.Label(window, image=imgtk) # register tk image 
label.pack()

# functon2: get gray scale tk image 
def get_grayscale_tk_image():
	imgtk = np_image_to_tk_image(gray_image)
	label.config(image=imgtk)
	label.image = imgtk
# functon3: get color tk image 
def get_color_tk_image():
	imgtk = np_image_to_tk_image(color_image)
	label.config(image=imgtk)
	label.image = imgtk

# button 
button1 = tk.Button(window, text="GrayScale",
					command=get_grayscale_tk_image)
button2 = tk.Button(window, text="Color",
					command=get_color_tk_image)
button1.pack(side="left", expand=True, fill='both')
button2.pack(side="right", expand=True, fill='both')

window.mainloop()