from PyPDF2 import PdfReader
import wx
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import PyPDF2
import time
from gtts import gTTS

# UI Code (Takes all user inputs and calls below functions)
import sys
import os.path

# begin wxGlade: dependencies
import gettext
# end wxGlade

from pathlib import Path

# setupvalues
ProgLang = "English"
OutputLangNum = 0
OutputLang = 'en'  
EditPageNum = "1"
InputFileName = "Default.pdf"
OutputFileLocation = str(Path.home() / "Downloads")
TextFileName = "TextToEdit.txt"
SelectedLanguage = 'en'
SelectedLanguageNumber = 0
PagesPerChapter = 4




# Open PDF/Read Text

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Inputs: Location of PDF and PDF File
# Outputs: Array of Strings, each element corresponds to one page from the pdf
# Description: Opens PDF from specified location, reads text and returns it
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def openPDF(fileName):
    reader = PdfReader(fileName) #+".pdf"

    arrayOfPages = []

    for page in reader.pages:
        # to select text orientation
        # page.extract_text(0)

        arrayOfPages.append(page.extract_text())

    return arrayOfPages

# Open Txt/Read Text

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Inputs: Location of TXT File
# Outputs: Array of Strings of length 1 with text from the txt doc
# Description: Opens TXT from specified location, reads text and returns it
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def openTXT(fileName):
    file = open(fileName, "r")#+".txt"
    data = file.read()
    pages = []
    pages.append(data)
    return pages

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Inputs: Array of String from OpenPDF()
# Outputs: String/Array ready to send to Audio Convert
# Description: Organizes text (by chapter), exports to txt, allows user edits, reads txt and returns edited strings
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def toTextEditor(arrayOfPages, outputFileLocation):
    file = open(outputFileLocation, "w") #+".txt"
    file.write("********************************************** DO NOT REMOVE THIS HEADER **************************************************\n"
               + "You may use the service and the contents contained in these services for your own individual non-commercial purpose only.\n"
               + "Any other use, is strictly prohibited without the permission of the work's  publisher.\n"
               + "Vous pouvez utiliser le service et le contenu de ces services à des fins personnelles et non commerciales uniquement.\n"
               + "Toute autre utilisation est strictement interdite sans l'autorisation de l'éditeur.\n"
               + "****************************************************************************************************************<page>\n")
    for page in arrayOfPages:
        try:
            file.write(page+"<page>\n")
        except:
            continue
# Convert edited text to array of strings

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Input: file name
# Output: array of strings
# Description: Convert formatted text files into formatted array of strings
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def fromTextEditor(fileName, pagesPerChapter):
    data = openTXT(fileName)
    
    stringList = data[0].split("<page>")
    stringList = stringList[1:-1]
    data2 = ""

    for i in range(len(stringList)):
        
        if ((i+1) % pagesPerChapter == 0):
            stringList[i] += "<chapter>"
            
        data2 += stringList[i]

    # <chapter> is used to denote end of chapters
    stringList2 = data2.split("<chapter>")

    for i in stringList2:
        i.strip()

    return stringList2[:-1]

# Convert array of strings to mp3

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Input: String Array + Location for outputs
# Output: Audio file(s)
# Description: Convert Strings to multiple audio files
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



def audioConvert(arrayOfStrings, outputFileLocation, SelectedLanguage):
    for chapter in range(len(arrayOfStrings)):
        if(any(c.isalpha() for c in arrayOfStrings[chapter])):
            textToSpeech = gTTS(text=arrayOfStrings[chapter], lang=SelectedLanguage)

        textToSpeech.save(outputFileLocation+"\\"+str(chapter+1)+".mp3")

# toTextEditor(openTXT("test"), "outputFileName")
# audioConvert(fromTextEditor("outputFileName", 5), "outputAudioFile")













class MainW(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainW.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((432, 261))
        self.SetTitle(_("PDFtoMP3"))

        self.MainPanel = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.ALL | wx.EXPAND, 15)

        sizer_3 = wx.StaticBoxSizer(wx.StaticBox(self.MainPanel, wx.ID_ANY, ""), wx.HORIZONTAL)
        sizer_2.Add(sizer_3, 0, 0, 0)

        PDFLabel = wx.StaticText(self.MainPanel, wx.ID_ANY, _("Input File (PDF):     "))
        sizer_3.Add(PDFLabel, 1, wx.ALL, 1)

        self.SelectFile = wx.Button(self.MainPanel, wx.ID_ANY, _("Select File"))
        sizer_3.Add(self.SelectFile, 0, 0, 0)

        self.SettingsButton = wx.Button(self.MainPanel, wx.ID_ANY, _("Settings"))
        sizer_3.Add(self.SettingsButton, 0, wx.LEFT, 129)

        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(sizer_4, 1, wx.ALL | wx.EXPAND, 0)

        sizer_8 = wx.GridBagSizer(0, 0)
        sizer_4.Add(sizer_8, 0, wx.EXPAND, 0)

        self.EditPage = wx.Button(self.MainPanel, wx.ID_ANY, _("Edit Selected File"))
        sizer_8.Add(self.EditPage, (0, 0), (1, 1), wx.BOTTOM | wx.TOP, 20)

        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(sizer_5, 0, wx.EXPAND, 0)

        sizer_6 = wx.StaticBoxSizer(wx.StaticBox(self.MainPanel, wx.ID_ANY, ""), wx.HORIZONTAL)
        sizer_5.Add(sizer_6, 1, wx.BOTTOM | wx.EXPAND | wx.TOP, 12)

        OutputLabel = wx.StaticText(self.MainPanel, wx.ID_ANY, _("Choose Output Location:  "))
        sizer_6.Add(OutputLabel, 0, 0, 0)

        self.SelectFolder = wx.Button(self.MainPanel, wx.ID_ANY, _("Select Folder"))
        sizer_6.Add(self.SelectFolder, 0, 0, 0)

        self.button_2 = wx.Button(self.MainPanel, wx.ID_ANY, _("Convert"))
        sizer_5.Add(self.button_2, 0, wx.EXPAND, 0)

        self.MainPanel.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.SelectFilePress, self.SelectFile)
        self.Bind(wx.EVT_BUTTON, self.SettingsClicked, self.SettingsButton)
        self.Bind(wx.EVT_BUTTON, self.EditPagePressed, self.EditPage)
        self.Bind(wx.EVT_BUTTON, self.SelectFolderPressed, self.SelectFolder)
        self.Bind(wx.EVT_BUTTON, self.StartConversion, self.button_2)
        # end wxGlade

    def SelectFilePress(self, event):  # wxGlade: MainW.<event_handler>
        #print("Event handler 'SelectFilePress' not implemented!")
        #event.Skip
        root = tk.Tk()
        root.withdraw()
        
        global InputFileName
        InputFileName = filedialog.askopenfilename()
        print(InputFileName+" selected.")
        toTextEditor(openPDF(InputFileName), TextFileName)
        print("Finished importing.")
        tk.messagebox.showinfo(title="Done", message="Finished Importing.")
        
        
    def SettingsClicked(self, event):  # wxGlade: MainW.<event_handler>
        #print("Event handler 'SettingsClicked' not implemented!")
        #event.Skip()
        class App(tk.Tk):
            def __init__(self):
                super().__init__()
                self.geometry("320x80")
                self.eval('tk::PlaceWindow . center')
                self.title('Settings')

                # initialize data
                self.languages = ('en', 'fr')
                self.second = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

                # set up variable
                self.option_var = tk.StringVar(self)
                self.option_varr = tk.StringVar(self)

                # create widget
                self.create_wigets()

            def create_wigets(self):
                # padding for widgets using the grid layout
                paddings = {'padx': 5, 'pady': 5}

                # label
                label = ttk.Label(self,  text='Select output language:')
                label.grid(column=0, row=0, sticky=tk.W, **paddings)

                # option menu
                option_menu = ttk.OptionMenu(
                    self,
                    self.option_var,
                    self.languages[SelectedLanguageNumber],
                    *self.languages,
                    command=self.option_changed)

                option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)
                
                # label
                labell = ttk.Label(self,  text='Pages per Audio File:')
                labell.grid(column=0, row=1, sticky=tk.W, **paddings)
                # option menu
                option_menuu = ttk.OptionMenu(
                    self,
                    self.option_varr,
                    self.second[PagesPerChapter-1],
                    *self.second,
                    command=self.option_changedd)

                option_menuu.grid(column=1, row=1, sticky=tk.W, **paddings)
                

            def option_changed(self, *args):
                global SelectedLanguage
                global SelectedLanguageNumber
                SelectedLanguage = self.option_var.get()
                if SelectedLanguage == 'en':
                    SelectedLanguageNumber = 0
                else:
                    SelectedLanguageNumber = 1
                #print(SelectedLanguage)
            def option_changedd(self, *args):
                #SelectedLanguage = self.option_var.get()
                global PagesPerChapter
                PagesPerChapter = int(self.option_varr.get())


        if __name__ == "__main__":
            app = App()
            app.mainloop()

    def EditPagePressed(self, event):  # wxGlade: MainW.<event_handler>
        #print("Event handler 'EditPagePressed' not implemented!")
        #event.Skip()
        os.popen(TextFileName)
        

    def SelectFolderPressed(self, event):  # wxGlade: MainW.<event_handler>
        #print("Event handler 'SelectFolderPressed' not implemented!")
        #event.Skip()
        root = tk.Tk()
        root.withdraw()
        
        global OutputFileLocation
        OutputFileLocation = filedialog.askdirectory()
        #self.label_1.SetLabel(OutputFileLocation)
        #label_1 = wx.StaticText(self.MainPanel, wx.ID_ANY, _(OutputFileLocation))
        #sizer_6.Add(label_1, 0, wx.LEFT, 13)


        

    def StartConversion(self, event):  # wxGlade: MainW.<event_handler>
        #print("Event handler 'StartConversion' not implemented!")
        #event.Skip()
        global InputFileName
        if (InputFileName != "Default.pdf"):
            print('Converting to '+SelectedLanguage+'.')
            audioConvert(fromTextEditor(TextFileName, PagesPerChapter), OutputFileLocation, SelectedLanguage)
            print('Converted! Check your output location for the MP3. (Default is Downloads)')
        else:
            print("File not selected.")
            tk.messagebox.showerror(title="Error", message="File not selected. Please select a PDF.")
            
        
    #-------------------------------------------------------------------------------

    class MyApp(wx.App):
        """
        ....
        """
        def OnInit(self):

            #------------

            self.installDir = os.path.split(os.path.abspath(sys.argv[0]))[0]

            #------------

            frame = MyFrame()
            self.SetTopWindow(frame)
            frame.Show(True)

            return True

        #---------------------------------------------------------------------------

        def GetInstallDir(self):
            """
            Returns the installation directory for my application.
            """

            return self.installDir


        def GetIconsDir(self):
            """
            Returns the icons directory for my application.
            """

            icons_dir = os.path.join(self.installDir, "icons")
            return icons_dir

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


