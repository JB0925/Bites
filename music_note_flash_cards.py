from pyaudio_test import read_and_write_audio, get_pitch
import tkinter as tk
from pil import Image, ImageTk
import random
import os

root = tk.Tk()
filename = 'C:/Users/superuser/Bites/chromatic_note_cards'
file_ = random.choice(os.listdir(filename))

img = Image.open(os.path.join(filename, file_))
photo = ImageTk.PhotoImage(img)
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.create_image(50,50, anchor='nw', image=photo)

root.mainloop()


