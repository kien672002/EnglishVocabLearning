from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import MenuGUI
import dataManger

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/AddVocabGUI")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def addVocab(window):
    def button1Actions():
        s2 = entry_2.get().strip().removesuffix(' ').removeprefix(' ')
        s1 = entry_1.get("1.0", "end-1c").strip().replace('\t', ' ').removesuffix(' ').removeprefix(' ')
        s3 = entry_3.get("1.0", "end-1c").strip().replace('\t',' ').removeprefix(' ').removesuffix(' ')
        if (s2 == '' or s1 == '' or s3 == ''):
            return
        dataManger.DataManger.addVocab(s2, s1, s3)
        canvas.itemconfig(words_count_display,  text=f"{dataManger.DataManger.words_count} words has added to vocabulary",)
        entry_2.delete(0, "end")
        entry_3.delete(1.0, "end")
        entry_1.delete(1.0, "end")

        # print(s2)
        # print(s1)
        # print(s3)

    def button1Enter(e):
        button_1['image'] = button_image_1_enter

    def button1Leave(e):
        button_1['image'] = button_image_1_leave

    def button2Actions():
        canvas.destroy()
        button_1.destroy()
        button_2.destroy()
        MenuGUI.menu(window)

    def button2Enter(e):
        button_2['image'] = button_image_2_enter

    def button2Leave(e):
        button_2['image'] = button_image_2_leave

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
        text="Add ",
        fill="#000000",
        font=("Sansita Regular", 60 * -1)
    )

    words_count_display = canvas.create_text(
        725/2,
        142.0,
        anchor="center",
        text=f"{dataManger.DataManger.words_count} words has added to vocabulary",
        fill="#484646",
        font=("Sansita Regular", 34 * -1)
    )

    global entry_image_2
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        132.5,
        221.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        font=("Sansita Regular", 15 * -1),
        highlightthickness=0
    )
    entry_2.place(
        x=67.0,
        y=210.0,
        width=135.0,
        height=23.0
    )

    global entry_image_1
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        360.5,
        298.5,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#FFFFFF",
        font=("Sansita Regular", 15 * -1),
        highlightthickness=0
    )
    entry_1.place(
        x=67.0,
        y=280.0,
        width=587.0,
        height=40.0
    )

    global entry_image_3
    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        360.5,
        384.5,
        image=entry_image_3
    )
    entry_3 = Text(
        bd=0,
        bg="#FFFFFF",
        font=("Sansita Regular", 15 * -1),
        highlightthickness=0
    )
    entry_3.place(
        x=67.0,
        y=366.0,
        width=587.0,
        height=39.0
    )

    canvas.create_text(
        59.0,
        188.0,
        anchor="nw",
        text="Word: ",
        fill="#000000",
        font=("Sansita Regular", 15 * -1)
    )

    canvas.create_text(
        59.0,
        257.0,
        anchor="nw",
        text="Defination: ",
        fill="#000000",
        font=("Sansita Regular", 15 * -1)
    )

    canvas.create_text(
        59.0,
        343.0,
        anchor="nw",
        text="Example: ",
        fill="#000000",
        font=("Sansita Regular", 15 * -1)
    )

    global button_image_1_enter # keep an extra reference to the image object.
    global button_image_1_leave
    button_image_1_enter = PhotoImage(file=relative_to_assets("button_1_enter.png"))
    button_image_1_leave = PhotoImage(file=relative_to_assets("button_1_leave.png"))

    button_1 = Button(
        image=button_image_1_leave,
        borderwidth=0,
        highlightthickness=0,
        command=button1Actions,
        relief="flat"
    )
    button_1.place(
        x=302.0,
        y=417.0,
        width=151.0,
        height=35.0
    )

    button_1.bind("<Enter>", button1Enter)
    button_1.bind("<Leave>", button1Leave)


    global button_image_2_leave, button_image_2_enter # keep an extra reference to the image object.
    button_image_2_leave = PhotoImage(file=relative_to_assets("button_2_leave.png"))
    button_image_2_enter = PhotoImage(file=relative_to_assets("button_2_enter.png"))

    button_2 = Button(
        image=button_image_2_leave,
        borderwidth=0,
        highlightthickness=0,
        command=button2Actions,
        relief="flat"
    )
    button_2.place(
        x=33.0,
        y=26.0,
        width=53.0,
        height=35.0
    )

    button_2.bind("<Enter>", button2Enter)
    button_2.bind("<Leave>", button2Leave)


if __name__ == '__main__':
    window = Tk()
    window.geometry("725x484")
    window.configure(bg="#FFFFFF")
    window.resizable(False, False)

    addVocab(window)

    window.mainloop()