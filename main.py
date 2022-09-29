from fileinput import filename
from PIL import Image, ImageDraw
from tkinter import Tk, Canvas, PhotoImage, Label, Button
import customtkinter
from tkinter.filedialog import askopenfilename
import os

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Montserrat"

# ------------------ Image Upload
path = "./raw_pictures/test.png"
logo = "This is a test"
canvas_img = None

def upload_photo():
    global fname
    fname = askopenfilename()
    display_photo(fname)


def display_photo(fname):
    global canvas_img
    canvas_img = PhotoImage(file=fname)
    canvas.create_image(500, 500, image=canvas_img)
    canvas.config(height=canvas_img.height(), width=canvas_img.width())
    canvas.grid(row=0, column=0)

    # with Image.open(fname) as im:
    #     h, w = im.size
    #     print(h, w)
    #     ImageDraw.Draw(im).text((h/2, w/2), logo, fill=(255, 255, 255))
        # im.show()

# for pic_file in os.listdir(path):
#     print(f"{path}/{pic_file}")


# ------------------------------ Tkinter GUI
window = Tk()
window.title("Watermark")
window.config(padx=20, pady=20, bg=YELLOW)

canvas = Canvas(width=1000, height=1000, bg=YELLOW, highlightthickness=0)
title_label = Label(text="Simple Watermark", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
upload_button = customtkinter.CTkButton(text="Upload Photo", command=upload_photo)
upload_button.grid(row=1, column=1)






window.mainloop()
