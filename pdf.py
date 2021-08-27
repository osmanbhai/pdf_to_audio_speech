from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3

root =Tk()
root.geometry("100x100")


def open_pdf():
    open_file = filedialog.askopenfilename(initialdir="C:\\Users\\osman\\PycharmProjects\\audiobook")
    title = "open pdf"
    filetypes = (("PDF Files","*.pdf"),
                 ("ALL Files","*.*"))
    if open_file:
        top = Toplevel()
        my_text = Text(top, height=500, width=500)
        my_text.pack()
        pdfReader = PyPDF2.PdfFileReader(open_file)
        speaker = pyttsx3.init()

        pages = pdfReader.numPages
        for i in range(pages):
                page = pdfReader.getPage(i)
                text = page.extractText()

                speaker.say(text)
                speaker.runAndWait()


button =Button(root,text = "open file",command = open_pdf)
button.pack()
root.mainloop()