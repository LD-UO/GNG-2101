from PyPDF2 import PdfReader
import wx
import PyPDF2
import time
from gtts import gTTS
print('Imported Text-to-Speech')
print('Imported PDF-to-Text')
print('Imported GUI Handler')


# UI Code (Takes all user inputs and calls below functions)
import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainW(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainW.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((503, 385))
        self.SetTitle(_("frame"))

        self.MainPanel = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.ALL | wx.EXPAND, 15)

        sizer_3 = wx.WrapSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_3, 0, 0, 0)

        PDFLabel = wx.StaticText(self.MainPanel, wx.ID_ANY, _("Input File:     "))
        sizer_3.Add(PDFLabel, 1, wx.ALL, 1)

        self.SelectFile = wx.Button(self.MainPanel, wx.ID_ANY, _("Select File"))
        sizer_3.Add(self.SelectFile, 0, 0, 0)

        label_3 = wx.StaticText(self.MainPanel, wx.ID_ANY, _("Program Language:  "))
        sizer_3.Add(label_3, 0, wx.LEFT, 30)

        self.ProgramLanguage = wx.Choice(self.MainPanel, wx.ID_ANY, choices=[_("English"), _("French")])
        self.ProgramLanguage.SetSelection(0)
        sizer_3.Add(self.ProgramLanguage, 0, wx.LEFT, 10)

        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(sizer_4, 1, wx.ALL | wx.EXPAND, 0)

        EditLabel = wx.StaticText(self.MainPanel, wx.ID_ANY, _("Edit Output Here:"))
        sizer_4.Add(EditLabel, 0, wx.BOTTOM | wx.TOP, 7)

        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_8, 1, wx.EXPAND, 0)

        sizer_8.Add((20, 0), 1, 0, 0)

        label_4 = wx.StaticText(self.MainPanel, wx.ID_ANY, _("Page Number:  "))
        sizer_8.Add(label_4, 0, wx.LEFT | wx.RIGHT, 20)

        self.PageNumberSelect = wx.Choice(self.MainPanel, wx.ID_ANY, choices=[_("1"), _("2"), _("3")])
        self.PageNumberSelect.SetSelection(0)
        sizer_8.Add(self.PageNumberSelect, 0, wx.BOTTOM, 10)

        grid_sizer_1 = wx.GridSizer(1, 1, 0, 0)
        sizer_4.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        self.TextEditBox = wx.TextCtrl(self.MainPanel, wx.ID_ANY, _("kcxljvx \naskdljf\nasjd\nfajsdfj\nadjfa\njdf\nadfj\nadsjf\nadfj"), style=wx.TE_MULTILINE)
        grid_sizer_1.Add(self.TextEditBox, 0, wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(sizer_5, 0, wx.EXPAND, 0)

        sizer_6 = wx.WrapSizer(wx.HORIZONTAL)
        sizer_5.Add(sizer_6, 1, wx.BOTTOM | wx.EXPAND | wx.TOP, 12)

        OutputLabel = wx.StaticText(self.MainPanel, wx.ID_ANY, _("Choose Output Location:  "))
        sizer_6.Add(OutputLabel, 0, 0, 0)

        self.SelectFolder = wx.Button(self.MainPanel, wx.ID_ANY, _("Select Folder"))
        sizer_6.Add(self.SelectFolder, 0, 0, 0)

        sizer_7 = wx.WrapSizer(wx.HORIZONTAL)
        sizer_5.Add(sizer_7, 1, wx.BOTTOM | wx.EXPAND | wx.TOP, 12)

        OutputLanguage = wx.StaticText(self.MainPanel, wx.ID_ANY, _("Choose Output Language:  "))
        sizer_7.Add(OutputLanguage, 0, 0, 0)

        self.OutputLanguageChoice = wx.Choice(self.MainPanel, wx.ID_ANY, choices=[_("English"), _("French")])
        self.OutputLanguageChoice.SetSelection(0)
        sizer_7.Add(self.OutputLanguageChoice, 0, 0, 0)

        self.button_2 = wx.Button(self.MainPanel, wx.ID_ANY, _("Convert"))
        sizer_5.Add(self.button_2, 0, wx.EXPAND, 0)

        self.MainPanel.SetSizer(sizer_1)

        self.Layout()
        # end wxGlade

# end of class MainW

class GUIAudioConverter(wx.App):
    def OnInit(self):
        self.MainWindow = MainW(None, wx.ID_ANY, "")
        self.SetTopWindow(self.MainWindow)
        self.MainWindow.Show()
        return True

# end of class GUIAudioConverter

if __name__ == "__main__":
    gettext.install("AudioConverter") # replace with the appropriate catalog name

    AudioConverter = GUIAudioConverter(0)
    AudioConverter.MainLoop()


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
#print(OpenPDF("test.pdf"))
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
            file.write(page+"<page>")
        except:
            continue


startTime = time.time()
toTextEditor(OpenPDF("test.pdf"))
print("Time to write: "+(str)(time.time()-startTime))

# Convert edited text to array of strings

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Input: file name
# Output: array of strings
# Description: Convert formatted text files into formatted array of strings
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def fromTextEditor(fileName):
    file = open(fileName,"r")
    # will need to move replace once page fuctionallity is added
    data = file.read().replace("<page>","")
    # <page> is used to denote end of pages
    # TODO: insert chapters by number of pages

    # <chapter> is used to denote end of chapters
    stringList = data.split("<chapter>")
    return stringList

# Convert array of strings to mp3

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

stringArray=OpenPDF("test.pdf")
startTime = time.time()
AudioConvert(stringArray)
print("Time to create mp3: "+(str)(time.time()-startTime))
