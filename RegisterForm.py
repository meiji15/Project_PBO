import wx
import Register

class subClass(Register.frameRegister):
    def __init__(self, parent):
        Register.frameRegister.__init__(self, parent)
        self.database = {"user":"admin"}

    def cek(self):
        self.username = self.m_username.GetValue()
        self.password = self.m_password.GetValue()

    def DaftarButton(self, event):
        self.cek()
        self.database[self.username] = self.password
        wx.MessageBox("Pendaftaran Berhasil")

app = wx.App()
frame = subClass(parent=None)
frame.Show()
app.MainLoop()