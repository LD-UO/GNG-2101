from gtts import gTTS
print('Imported Text-to-Speech')
import PyPDF2
print('Imported PDF-to-Text')
import wx
print('Imported GUI Handler')


#UI Code (Takes all user inputs and calls below functions)
app = wx.App()

frame = wx.Frame(None, title='Prototype')
frame.Show()

app.MainLoop()

#Open PDF/Read Text

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Inputs: Location of PDF and PDF File
#Outputs: Text from pdf in array of strings
#Description: Opens PDF from specified location, reads text and returns it
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def OpenPDF():
    return null

#Organize text and dump to txt for edits

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Inputs: Array/String from OpenPDF()
#Outputs: String/Array ready to send to Audio Convert
#Description: Organizes text (by chapter), exports to txt, allows user edits, reads txt and returns edited strings
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def TextEditor():
    return null


#Convert edited text to mp3

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Input: String/Array + Location for outputs
#Output: Audio file(s)
#Description: Convert Strings to multiple audio files
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def AudioConvert():
    return null


