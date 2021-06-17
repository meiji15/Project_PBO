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
## Class frameLogin
###########################################################################

class frameLogin ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login", pos = wx.DefaultPosition, size = wx.Size( 235,167 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 10, 74, 90, 90, False, "Berlin Sans FB" ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.Username = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Username.Wrap( -1 )
		self.Username.SetFont( wx.Font( 10, 70, 90, 90, False, "Century751 SeBd BT" ) )
		
		gSizer4.Add( self.Username, 1, wx.ALL, 5 )
		
		self.m_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_username, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.Password = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Password.Wrap( -1 )
		self.Password.SetFont( wx.Font( 10, 70, 90, 90, False, "Century751 SeBd BT" ) )
		
		gSizer4.Add( self.Password, 0, wx.ALL, 5 )
		
		self.m_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_password, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_Daftar = wx.Button( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Daftar.SetFont( wx.Font( 10, 70, 90, 90, False, "Century751 SeBd BT" ) )
		
		gSizer4.Add( self.m_Daftar, 0, wx.ALL, 5 )
		
		self.m_Login = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Login.SetFont( wx.Font( 10, 70, 90, 90, False, "Century751 SeBd BT" ) )
		
		gSizer4.Add( self.m_Login, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( gSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_Daftar.Bind( wx.EVT_BUTTON, self.DaftarButton )
		self.m_Login.Bind( wx.EVT_BUTTON, self.LoginButton )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def DaftarButton( self, event ):
		event.Skip()
	
	def LoginButton( self, event ):
		event.Skip()
	

