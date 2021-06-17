import wx
import FormLogin

class subClass(FormLogin.frameLogin):
    def __init__(self, parent):
        FormLogin.frameLogin.__init__(self, parent)
        self.database = {"user":"admin"}

    def cek(self):
        self.username = self.m_username.GetValue()
        self.password = self.m_password.GetValue()

    def DaftarButton(self, event):
        self.cek()
        self.database[self.username] = self.password
        wx.MessageBox("Pendaftaran Berhasil")

    def LoginButton(self, event):
        self.cek()
        try:
            if self.database[self.username] == self.password:
                wx.MessageBox("Login Berhasil")
            else:
                wx.MessageBox("Login Gagal")
        except:
            print ("error")

app = wx.App()
frame = subClass(parent=None)
frame.Show()
app.MainLoop()