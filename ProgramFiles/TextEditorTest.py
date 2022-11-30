# sample_one.py

import sys
import os.path
import wx

# class MyFrame
# class MyApp

#-------------------------------------------------------------------------------

# This is how you pre-establish a file filter so that the
# dialog only shows the extension(s) you want it to.

wildcard = "Text (*.txt)|*.txt|"        \
           "Executable (*.exe)|*.exe|"  \
           "Library (*.dll)|*.dll|"     \
           "Driver (*.sys)|*.sys|"      \
           "ActiveX (*.ocx)|*.ocx|"     \
           "Python (*.py)|*.py|"        \
           "Python (*.pyw)|*.pyw|"      \
           "All (*.*)|*.*"

#-------------------------------------------------------------------------------

class MyFrame(wx.Frame):
    def __init__(self, filename="noname.txt"):
        super(MyFrame, self).__init__(None, size=(400, 300))

        #------------

        # Return icons folder.
        self.icons_dir = wx.GetApp().GetIconsDir()

        #------------

        self.filename = filename
        self.dirname  = "."

        #------------

        # Simplified init method.
        self.CreateInteriorWindowComponents()
        self.CreateExteriorWindowComponents()

        #------------

        self.CenterOnScreen()

    #---------------------------------------------------------------------------

    def SetTitle(self):
        """
        ...
        """

        # MyFrame.SetTitle overrides wx.Frame.SetTitle,
        # so we have to call it using super :
        super(MyFrame, self).SetTitle("Editor %s" % self.filename)


    def CreateInteriorWindowComponents(self):
        """
        Create "interior" window components. In this case
        it is just a simple multiline text control.
        """

        self.control = wx.TextCtrl(self, -1, value="", style=wx.TE_MULTILINE)


    def CreateExteriorWindowComponents(self):
        """
        Create "exterior" window components, such as menu and status bar.
        """

        # Simplified init method.
        self.SetTitle()

        #------------

        frameIcon = wx.Icon(os.path.join(self.icons_dir,
                                         "icon_wxWidgets.ico"),
                            type=wx.BITMAP_TYPE_ICO)
        self.SetIcon(frameIcon)

        #------------

        self.CreateMenu()
        self.CreateStatusBar()
        self.BindEvents()


    def CreateMenu(self):
        """
        Create menu and menu bar.
        """

        menuBar = wx.MenuBar()

        #------------

        fileMenu = wx.Menu()

        for id, label, helpText, handler in \
            [(wx.ID_ABOUT, "&About",
              "Information about this program.", self.OnAbout),
             (None, None, None, None),
             (wx.ID_OPEN, "&Open",
              "Open a new file.", self.OnOpen),
             (wx.ID_SAVE, "&Save",
              "Save the current file.", self.OnSave),
             (wx.ID_SAVEAS, "Save &as",
              "Save the file under a different name.", self.OnSaveAs),
             (None, None, None, None),
             (wx.ID_EXIT, "E&xit",
              "Terminate the program.", self.OnCloseMe)]:

            if id == None:
                fileMenu.AppendSeparator()
            else:
                item = fileMenu.Append(id, label, helpText)

                #------------

                # Bind some events to an events handler.
                self.Bind(wx.EVT_MENU, handler, item)

        #------------

        # Add the fileMenu to the menuBar.
        menuBar.Append(fileMenu, "&File")

        #------------

        # Add the menuBar to the frame.
        self.SetMenuBar(menuBar)


    def BindEvents(self):
        """
        ...
        """

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)


    def DefaultFileDialogOptions(self):
        """
        Return a dictionary with file dialog options that can be
        used in both the save file dialog as well as in the open
        file dialog.
        """

        return dict(message="Choose a file :",
                    defaultDir=self.dirname,
                    wildcard=wildcard)


    def AskUserForFilename(self, **dialogOptions):
        """
        ...
        """

        dialog = wx.FileDialog(self, **dialogOptions)

        if dialog.ShowModal() == wx.ID_OK:
            userProvidedFilename = True
            self.filename = dialog.GetFilename()
            self.dirname = dialog.GetDirectory()
            # Update the window title with the new filename.
            self.SetTitle()
        else:
            userProvidedFilename = False

        dialog.Destroy()

        return userProvidedFilename


    def OnOpen(self, event):
        """
        Open file.
        """

        if self.AskUserForFilename(style=wx.FD_OPEN,
                                   **self.DefaultFileDialogOptions()):
            file = open(os.path.join(self.dirname, self.filename), 'r', encoding='utf-8')
            self.control.SetValue(file.read())
            file.close()


    def OnSave(self, event):
        """
        Save file.
        """

        with open(os.path.join(self.dirname, self.filename), 'w', encoding='utf-8') as file:
            file.write(self.control.GetValue())


    def OnSaveAs(self, event):
        """
        Save file as.
        """

        if self.AskUserForFilename(defaultFile=self.filename, style=wx.FD_SAVE,
                                   **self.DefaultFileDialogOptions()):
            self.OnSave(event)


    def OnAbout(self, event):
        """
        About dialog.
        """

        dialog = wx.MessageDialog(self,
                                  "A sample editor in wxPython.",
                                  "About sample editor",
                                  wx.OK)
        dialog.ShowModal()
        dialog.Destroy()


    def OnCloseMe(self, event):
        """
        Close the main window.
        """

        self.Close(True)


    def OnCloseWindow(self, event):
        """
        Quit and destroy application.
        """

        self.Destroy()

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

#-------------------------------------------------------------------------------

def main():
    app = MyApp(False)
    app.MainLoop()

#-------------------------------------------------------------------------------

if __name__ == "__main__" :
    main()
