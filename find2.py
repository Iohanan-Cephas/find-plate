import re
import os
import PyPDF2
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES

license_plate_pattern = r'[A-Z]{3}\d{4}|[A-Z]{3}\d[A-Z]\d{2}'

def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text()
    return text

def process_pdf(event):
    pdf_path = event.data.strip('{}') 
    text = extract_text_from_pdf(pdf_path)

    license_plates = re.findall(license_plate_pattern, text)

    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'found_license_plates.txt')

    with open(desktop_path, 'w') as txt_file:
        for plate in license_plates:
            txt_file.write(plate + '\n')

    status_label.config(text=f'License plates saved in: {desktop_path}')

root = TkinterDnD.Tk()
root.title("Vehicle License Plate Extractor")
root.geometry("400x200")

instruction_label = tk.Label(root, text="Drag the PDF into this window")
instruction_label.pack(pady=20)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', process_pdf)

root.mainloop()
