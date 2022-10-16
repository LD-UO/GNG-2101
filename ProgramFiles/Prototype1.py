from PyPDF2 import PdfReader
import wx
import PyPDF2
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
# Outputs: Text from pdf in array of strings
# Description: Opens PDF from specified location, reads text and returns it
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def OpenPDF(fileName):
    reader = PdfReader(fileName)

    returnValue = ""
        
    for page in reader.pages:
        returnValue += page.extract_text()

# to select text orientation
# page.extract_text(0)

# returns one long string of all text
    return returnValue

print(OpenPDF("example.pdf"))
# Organize text and dump to txt for edits

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Inputs: Array/String from OpenPDF()
# Outputs: String/Array ready to send to Audio Convert
# Description: Organizes text (by chapter), exports to txt, allows user edits, reads txt and returns edited strings
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def TextEditor(string):
    return


# Convert edited text to mp3

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Input: String/Array + Location for outputs
# Output: Audio file(s)
# Description: Convert Strings to multiple audio files
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def AudioConvert():
    return
