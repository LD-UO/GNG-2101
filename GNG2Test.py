from gtts import gTTS
print('Imported Text-to-Speech')
import PyPDF2
print('Imported PDF-to-Text')
import wx
print('Imported GUI Handler')


app = wx.App()

frame = wx.Frame(None, title='Prototype')
frame.Show()

app.MainLoop()
