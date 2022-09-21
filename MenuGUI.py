from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import AddVocabGUI
import TestVocabGUI
import dataManger

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/MenuGUI")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def menu(window):
    def button1Actions():
        button_1.destroy()
        button_2.destroy()
        canvas.destroy()
        TestVocabGUI.testVocab(window)

    def button2Actions():
        button_1.destroy()
        button_2.destroy()
        canvas.destroy()
        AddVocabGUI.addVocab(window)

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 484,
        width = 725,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        725.0,
        484.0,
        fill="#FFF7F5",
        outline="")

    canvas.create_text(
        725/2,
        78.0,
        anchor="center",
        text="Home",
        fill="#000000",
        font=("Sansita Regular", 60 * -1)
    )

    canvas.create_text(
        725/2,
        142.0,
        anchor="center",
        text=f"{dataManger.DataManger.words_count} words has added to vocabulary",
        fill="#484646",
        font=("Sansita Regular", 34 * -1)
    )

    global button_image_1  # keep an extra reference to the image object.
    button_image_1 = PhotoImage(master=window,file=relative_to_assets("button_1.png"))

    button_1 = Button(
        master=window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=button1Actions,
        relief="flat"
    )
    button_1.place(
        x=403.0,
        y=244.0,
        width=278.0,
        height=176.0
    )

    global button_image_2   # keep an extra reference to the image object.
    button_image_2 = PhotoImage(master=window,file=relative_to_assets("button_2.png"))

    button_2 = Button(
        master=window,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=button2Actions,
        relief="flat"
    )

    button_2.place(
        x=53.0,
        y=244.0,
        width=278.0,
        height=176.0
    )

    # window.mainloop()

