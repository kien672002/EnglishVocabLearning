from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import MenuGUI
import dataManger

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/TestVocabGUI")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def testVocab(window):
    def getItemWidth(canvas, item):
      coords = canvas.bbox(item)
      return coords[0], coords[2]

    def showQuestAns(): pass
    def placeAnswers(ans_list): pass

    def button1Actions():
        canvas.destroy()
        button_1.destroy()
        MenuGUI.menu(window)
        # showQuestAns()

    def button1Enter(e):
        button_1['image'] = button_image_1_enter

    def button1Leave(e):
        button_1['image'] = button_image_1_leave

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
        text="Test ",
        fill="#000000",
        font=("Sansita Regular", 60 * -1)
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

    button_1.bind("<Enter>", button1Enter)
    button_1.bind("<Leave>", button1Leave)

    button_1.place(
        x=33.0,
        y=26.0,
        width=53.0,
        height=35.0
    )

    global button_image_2
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        # command=lambda: showQuestAns,
        relief="flat"
    )

    canvas.create_text(
        725/2,
        163.0,
        anchor="center",
        text="Which one is best described for: ",
        fill="#000000",
        font=("Sansita Regular", 20 * -1)
    )
    global line1, line2, line3
    line1 = line2 = line3 = None

    def placeQuestion(question_text):
        global line1, line2, line3
        line1 = canvas.create_text(725 / 2, 195, anchor='center', text=question_text, fill='#79AD25',
                                   font=("Sansita Regular", 20 * -1))

        xl, xr = getItemWidth(canvas, line1)

        if (xl < 40 or xr > 735):
            tmp = question_text.split(' ')
            lline = len(tmp) * 2 // 3
            question_text_1 = ' '.join(tmp[:lline])
            question_text_2 = ' '.join(tmp[lline:])

            canvas.itemconfig(line1, text=question_text_1)
            line2 = canvas.create_text(725 / 2, 215, anchor='center', text=question_text_2, fill='#79AD25',
                                       font=("Sansita Regular", 20 * -1))

            xl, xr = getItemWidth(canvas, line1)
            if (xl < 40 or xr > 735):
                tmp = question_text.split(' ')
                lline1 = len(tmp) * 4 // 10
                lline2 = len(tmp) * 3 // 10 + lline1
                question_text_1 = ' '.join(tmp[:lline1])
                question_text_2 = ' '.join(tmp[lline1:lline2])
                question_text_3 = ' '.join(tmp[lline2:])

                canvas.itemconfig(line1, text=question_text_1)
                canvas.itemconfig(line2, text=question_text_2)
                line3 = canvas.create_text(725 / 2, 235, anchor='center', text=question_text_3, fill='#79AD25',
                                           font=("Sansita Regular", 20 * -1))

    # answers creating
    x_pos = 200.0
    x_pos_button = x_pos-30
    ans_a = canvas.create_text(
        x_pos,
        289.0,
        anchor="nw",
        text="Answer A",
        fill="#000000",
        font=("Sansita Regular", 16 * -1)
    )
    ans_b = canvas.create_text(
        x_pos,
        329.0,
        anchor="nw",
        text="Answer B",
        fill="#000000",
        font=("Sansita Regular", 16 * -1)
    )
    ans_c = canvas.create_text(
        x_pos,
        369.0,
        anchor="nw",
        text="Answer C",
        fill="#000000",
        font=("Sansita Regular", 16 * -1)
    )
    ans_d = canvas.create_text(
        x_pos,
        409.0,
        anchor="nw",
        text="Answer D",
        fill="#000000",
        font=("Sansita Regular", 16 * -1)
    )

    answers_pos_list = [[canvas.bbox(ans)[0], canvas.bbox(ans)[1], canvas.bbox(ans)[2], canvas.bbox(ans)[3]] for ans in
                        (ans_a, ans_b, ans_c, ans_d)]

    for ans in answers_pos_list:
        ans[0] = 199
        ans[2] = 500

    # for ans_pos in answers_pos_list:
    #     canvas.create_rectangle(199, ans_pos[1], 500, ans_pos[3])

    def placeAnswers(ans_list):
        canvas.itemconfig(ans_a, text=ans_list[0])
        canvas.itemconfig(ans_b, text=ans_list[1])
        canvas.itemconfig(ans_c, text=ans_list[2])
        canvas.itemconfig(ans_d, text=ans_list[3])

    def showQuestAns(e=None):
        global question
        canvas.delete(line1)
        canvas.delete(line2)
        canvas.delete(line3)
        question = dataManger.DataManger.getVocabTest()

        placeQuestion(question[0])
        placeAnswers(question[2])

        canvas.itemconfig(ans_a, fill = '#000000')
        canvas.itemconfig(ans_b, fill = '#000000')
        canvas.itemconfig(ans_c, fill = '#000000')
        canvas.itemconfig(ans_d, fill = '#000000')

        button_2.place_forget()

    button_2.bind("<Button-1>", showQuestAns)

    global question
    showQuestAns()

    def checkAnswer(pos):
        global question
        canvas.itemconfig(ans_a, fill = '#1BA105' if question[2][0] == question[1] else '#FF2E2E')
        canvas.itemconfig(ans_b, fill = '#1BA105' if question[2][1] == question[1] else '#FF2E2E')
        canvas.itemconfig(ans_c, fill = '#1BA105' if question[2][2] == question[1] else '#FF2E2E')
        canvas.itemconfig(ans_d, fill = '#1BA105' if question[2][3] == question[1] else '#FF2E2E')

        dataManger.DataManger.updateVocab(question[1], question[2][pos] == question[1])

        button_2.place(
            x=638.0,
            y=274.0,
            width=53.0,
            height=147.0
        )
        # question = showQuestAns()

    # Callback event that return mouse-clicked position, use this for choosing the answer
    def callback(event):
        global question
        # the answer lines are spaced by 40
        for ans_pos in answers_pos_list:
            if ans_pos[0] <= event.x <= ans_pos[2] and ans_pos[1] <= event.y <= ans_pos[3]:
                # print('clicked at:',answers_pos_list.index(ans_pos))
                checkAnswer(answers_pos_list.index(ans_pos))

    canvas.bind("<Button-1>", callback)

    def motion(event):
        ans_pos = answers_pos_list[0]
        if ans_pos[0] <= event.x <= ans_pos[2] and ans_pos[1] <= event.y <= ans_pos[3]:
            canvas.itemconfig(ans_a, font=("Sansita Regular", 16 * -1, 'underline'))
        else:
            canvas.itemconfig(ans_a, font=("Sansita Regular", 16 * -1))
        ans_pos = answers_pos_list[1]
        if ans_pos[0] <= event.x <= ans_pos[2] and ans_pos[1] <= event.y <= ans_pos[3]:
            canvas.itemconfig(ans_b, font=("Sansita Regular", 16 * -1, 'underline'))
        else:
            canvas.itemconfig(ans_b, font=("Sansita Regular", 16 * -1))
        ans_pos = answers_pos_list[2]
        if ans_pos[0] <= event.x <= ans_pos[2] and ans_pos[1] <= event.y <= ans_pos[3]:
            canvas.itemconfig(ans_c, font=("Sansita Regular", 16 * -1, 'underline'))
        else:
            canvas.itemconfig(ans_c, font=("Sansita Regular", 16 * -1))
        ans_pos = answers_pos_list[3]
        if ans_pos[0] <= event.x <= ans_pos[2] and ans_pos[1] <= event.y <= ans_pos[3]:
            canvas.itemconfig(ans_d, font=("Sansita Regular", 16 * -1, 'underline'))
        else:
            canvas.itemconfig(ans_d, font=("Sansita Regular", 16 * -1))

    canvas.bind('<Motion>', motion)

    # create hint button and the corresponding answer
    global hint_button
    hint_button = PhotoImage(file=relative_to_assets('hint_button.png'))

    ans_d_hint = Button(
        image=hint_button,
        borderwidth=0,
        highlightthickness=0,
        command=lambda : checkAnswer(3),
        relief="flat"
    )
    ans_d_hint.place(
        x=x_pos_button,
        y=407.0,
        width=20.0,
        height=20.0
    )

    ans_c_hint = Button(
        image=hint_button,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: checkAnswer(2),
        relief="flat"
    )
    ans_c_hint.place(
        x=x_pos_button,
        y=367.0,
        width=20.0,
        height=20.0
    )

    ans_b_hint = Button(
        image=hint_button,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: checkAnswer(1),
        relief="flat"
    )
    ans_b_hint.place(
        x=x_pos_button,
        y=327.0,
        width=20.0,
        height=20.0
    )

    ans_a_hint = Button(
        image=hint_button,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: checkAnswer(0),
        relief="flat"
    )
    ans_a_hint.place(
        x=x_pos_button,
        y=289.0,
        width=20.0,
        height=20.0
    )

if __name__ == '__main__':
    window = Tk()
    window.geometry("725x484")
    window.configure(bg="#FFFFFF")
    window.resizable(False, False)

    testVocab(window)

    window.mainloop()