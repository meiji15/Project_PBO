# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frameRegister
###########################################################################

class frameRegister ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Register", pos = wx.DefaultPosition, size = wx.Size( 259,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.Nama = wx.StaticText( self, wx.ID_ANY, u"Nama Lengkap : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Nama.Wrap( -1 )
		gSizer6.Add( self.Nama, 0, wx.ALL, 5 )
		
		self.m_nama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_nama, 0, wx.ALL, 5 )
		
		self.Nik = wx.StaticText( self, wx.ID_ANY, u"NIK :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Nik.Wrap( -1 )
		gSizer6.Add( self.Nik, 0, wx.ALL, 5 )
		
		self.m_nik = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_nik, 0, wx.ALL, 5 )
		
		self.Alamat = wx.StaticText( self, wx.ID_ANY, u"Alamat :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Alamat.Wrap( -1 )
		gSizer6.Add( self.Alamat, 0, wx.ALL, 5 )
		
		self.m_alamat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_alamat, 0, wx.ALL, 5 )
		
		self.Telepon = wx.StaticText( self, wx.ID_ANY, u"No Telepon :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Telepon.Wrap( -1 )
		gSizer6.Add( self.Telepon, 0, wx.ALL, 5 )
		
		self.m_telepon = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_telepon, 0, wx.ALL, 5 )
		
		self.Pass = wx.StaticText( self, wx.ID_ANY, u"Password :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Pass.Wrap( -1 )
		gSizer6.Add( self.Pass, 0, wx.ALL, 5 )
		
		self.m_pass = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_pass, 0, wx.ALL, 5 )
		
		self.email = wx.StaticText( self, wx.ID_ANY, u"Email :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.email.Wrap( -1 )
		gSizer6.Add( self.email, 0, wx.ALL, 5 )
		
		self.m_email = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_email, 0, wx.ALL, 5 )
		
		
		gSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_Daftar = wx.Button( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_Daftar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( gSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_Daftar.Bind( wx.EVT_BUTTON, self.DaftarButton )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def DaftarButton( self, event ):
		event.Skip()
	

