import Keylogger
import os
from pathlib import Path


def notepad(file_name):
  """Opens a text file in Notepad.

  Args:
    file_name: The name of the text file to open.
  """
  os.system("notepad.exe " + file_name)

if __name__ == "__main__":
  file_name = "log.txt"
  

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

file_path = r"D:\CS INTERN\build\log.txt"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\CS INTERN\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Keylogger")
photo = PhotoImage(
    file=relative_to_assets("icon_1.png"))
window.iconphoto(False, photo)
window.geometry("728x409")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 409,
    width = 728,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    364.0,
    204.0,
    image=image_image_1
)

canvas.create_rectangle(
    4.0,
    86.0,
    378.0,
    96.0,
    fill="#F6EDED",
    outline="")

canvas.create_text(
    17.0,
    31.0,
    anchor="nw",
    text="KEYLOGGER",
    fill="#FFFFFF",
    font=("Inter Italic Bold", 48 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:Keylogger.start() ,
    relief="flat"
)
button_1.pack()
button_1.place(
    x=115.0,
    y=325.0,
    width=130.0,
    height=41.0
)


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:notepad(file_name),
    relief="flat"
)
button_2.place(
    x=311.0,
    y=325.0,
    width=130.0,
    height=41.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:window.destroy(),
    relief="flat"
)
button_3.place(
    x=506.0,
    y=325.0,
    width=130.0,
    height=41.0
)

canvas.create_text(
    450.0,
    190.0,
    anchor="nw",
    text="Press Esc to Stop Capturing",
    fill="#FFFFFF",
    font=("CourierPrime", 20 * -1)
)
window.resizable(False, False)
window.mainloop()

