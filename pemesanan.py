import wx
import FormPesan

class form(FormPesan.MyFrame1):
    def __init__(self,parent):
        FormPesan.MyFrame1.__init__(self,parent)
    
if __name__ == "__main__":
    app=wx.App(False)
    frame=form(None)
    frame.Show(True)
    app.MainLoop()
