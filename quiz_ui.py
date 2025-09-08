from tkinter import *

bgcolor = "steelblue"

class QuizInterface:

    def __init__(self):

        self.window = Tk()
        self.window.title("QUIZZ")
        self.window.configure(bg = bgcolor, padx = 40 , pady = 40)


        self.score_label = Label(text = "SCORE: ", font=("TkDefaultFont", 20))
        self.score_label.configure(bg = bgcolor)
        self.score_label.grid(row = 0, column = 1)


        self.question_box = Canvas(width= 350, height= 400, highlightthickness= 0 , bg = "antique white")
        self.question_box.create_text(175,200, text = "Question Text", fill = bgcolor, font= ("Arial" , 20 , "italic"))
        self.question_box.grid(row = 1, column = 0, columnspan = 2, pady = 20)


        self.check_box = Canvas(width = 100, height= 100, highlightthickness= 0, bg= bgcolor)
        checkimage = PhotoImage(file = "true.png")
        self.check_box.create_image(50,50, image = checkimage)
        self.check_box.grid(row = 2, column = 0)


        self.wrong_box = Canvas(width=100, height=100, highlightthickness= 0, bg= bgcolor)
        checkimage2 = PhotoImage(file="false.png")
        self.wrong_box.create_image(50, 50, image=checkimage2)
        self.wrong_box.grid(row=2, column=1)

        self.window.mainloop()

