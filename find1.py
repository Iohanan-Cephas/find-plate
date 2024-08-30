import re
import os
import PyPDF2

pdf_path = 'C:/Users/your-user/Desktop/test.pdf'

license_plate_pattern = r'[A-Z]{3}\d{4}|[A-Z]{3}\d[A-Z]\d{2}'

def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text()
    return text

text = extract_text_from_pdf(pdf_path)

license_plates = re.findall(license_plate_pattern, text)

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'found_license_plates.txt')

with open(desktop_path, 'w') as txt_file:
    for plate in license_plates:
        txt_file.write(plate + '\n')

print(f'License plates saved in: {desktop_path}')
