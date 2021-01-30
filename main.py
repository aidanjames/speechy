import tkinter.filedialog as fd
from tkinter import *
from GoogleAudioManager import GoogleAudioManager
import textract
from playsound import playsound
import os.path


audio_file_path = ""
pdf_name = ""


def find_document():
    global pdf_name
    global audio_file_path
    file_path = fd.askopenfilename(title="Select a PDF", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_name = file_path.split('/')[-1]
        audio_file_path = f"audio-files/{pdf_name}".replace('.pdf', '.mp3')
        speak(file_path)


def speak(file):
    text_to_read = textract.process(file, encoding='ascii').decode('utf-8')

    speech_manager = GoogleAudioManager()
    speech_manager.text_to_speech(text_to_read, outfile=audio_file_path)

    if os.path.isfile(audio_file_path):
        playsound(audio_file_path)


# ------- UI set up ------------ #
window = Tk()
window.title("Speaky")
window.config(padx=50, pady=50)
window.resizable(width=True, height=True)
window.geometry("250x250")

feedback_label = Label(text="Search for file to read.")
feedback_label.grid(row=0, column=0)
feedback_label.config(padx=10, pady=10)

open_file_button = Button(window, text='Search', command=find_document)
open_file_button.grid(row=1, column=0)
open_file_button.config(padx=5, pady=5)

window.mainloop()
