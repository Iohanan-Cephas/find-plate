# Extract Vehicle License Plates from PDF

This script was created at my workplace to assist a colleague who needed to copy and paste at least 250 vehicle plates from a PDF but didn't know how to use a PC effectively. I thought it would be helpful to write a simple script to automate this task. However, my coworker ended up converting the PDF to an Excel file and copying the plates from the column.

The `find1.py` script requires you to change the path to the PDF every time you need to use a different one. The `find2.py` script provides a GUI where you can simply drag and drop the PDF into the window to perform the task.

## Requirements

Make sure you have the following libraries installed:

```bash
pip install PyPDF2
```

```bash
pip install tkinterdnd2
```

## Running the code

To run the code, use the following commands in the terminal:

```bash
python find1.py
```

```bash
python find2.py
```
