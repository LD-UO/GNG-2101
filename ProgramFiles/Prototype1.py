from PyPDF2 import PdfReader
import wx
import PyPDF2
import time
from gtts import gTTS
print('Imported Text-to-Speech')
print('Imported PDF-to-Text')
print('Imported GUI Handler')


# UI Code (Takes all user inputs and calls below functions)
# app = wx.App()

# frame = wx.Frame(None, title='Prototype')
# frame.Show()

# app.MainLoop()

# Open PDF/Read Text

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Inputs: Location of PDF and PDF File
# Outputs: Array of Strings, each element corresponds to one page from the pdf
# Description: Opens PDF from specified location, reads text and returns it
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def OpenPDF(fileName):
    reader = PdfReader(fileName)

    arrayOfPages = []

    for page in reader.pages:
        # to select text orientation
        # page.extract_text(0)

        arrayOfPages.append(page.extract_text())

    return arrayOfPages

startTime = time.time()
print(OpenPDF("test.pdf"))
print("Time to read file: "+(str)(time.time()-startTime))

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Inputs: Array of String from OpenPDF()
# Outputs: String/Array ready to send to Audio Convert
# Description: Organizes text (by chapter), exports to txt, allows user edits, reads txt and returns edited strings
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def toTextEditor(arrayOfPages):
    file = open("outputText.txt","w")
    for page in arrayOfPages:
        try:
            file.write(page)
        except:
            continue


startTime = time.time()
toTextEditor(OpenPDF("test.pdf"))
print("Time to write: "+(str)(time.time()-startTime))

# Convert edited text to mp3

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Input: String/Array + Location for outputs
# Output: Audio file(s)
# Description: Convert Strings to multiple audio files
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def AudioConvert(arrayOfStrings):
    for page in range(len(arrayOfStrings)):
        try:
            textToSpeech = gTTS(text=arrayOfStrings[page],lang='en')
        except:
            print("Please connect to internet to convert to audio")
        
        textToSpeech.save(f"{page}.mp3")

startTime = time.time()
AudioConvert(OpenPDF("test.pdf"))
print("Time to create mp3: "+(str)(time.time()-startTime))
