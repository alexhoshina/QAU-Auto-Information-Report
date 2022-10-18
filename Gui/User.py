import json
import wx
import wx.xrc

class User ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"配置User.json", pos = wx.DefaultPosition, size = wx.Size( 300,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 300,200 ), wx.Size( 300,200 ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7.SetMinSize( wx.Size( 240,10 ) )
		self.UserName_staticText = wx.StaticText( self, wx.ID_ANY, u"学工账号", wx.DefaultPosition, wx.Size( 60,20 ), 0 )
		self.UserName_staticText.Wrap( -1 )

		self.UserName_staticText.SetMinSize( wx.Size( 60,20 ) )

		bSizer7.Add( self.UserName_staticText, 0, wx.ALL, 5 )

		self.UserName_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,20 ), 0 )
		self.UserName_textCtrl.SetMinSize( wx.Size( 150,20 ) )

		bSizer7.Add( self.UserName_textCtrl, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer7, 0, wx.TOP|wx.BOTTOM, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer10.SetMinSize( wx.Size( 240,10 ) )
		self.UserPwd_staticText = wx.StaticText( self, wx.ID_ANY, u"学工密码", wx.DefaultPosition, wx.Size( 60,20 ), 0 )
		self.UserPwd_staticText.Wrap( -1 )

		self.UserPwd_staticText.SetMinSize( wx.Size( 60,20 ) )

		bSizer10.Add( self.UserPwd_staticText, 0, wx.ALL, 5 )

		self.UserPwd_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,20 ), 0 )
		self.UserPwd_textCtrl.SetMinSize( wx.Size( 150,20 ) )

		bSizer10.Add( self.UserPwd_textCtrl, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer10, 0, wx.TOP|wx.BOTTOM, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer11.SetMinSize( wx.Size( 240,10 ) )
		self.ServerKey_staticText = wx.StaticText( self, wx.ID_ANY, u"ServerKey", wx.DefaultPosition, wx.Size( 60,20 ), 0 )
		self.ServerKey_staticText.Wrap( -1 )

		self.ServerKey_staticText.SetMinSize( wx.Size( 60,20 ) )

		bSizer11.Add( self.ServerKey_staticText, 0, wx.ALL, 5 )

		self.SvererKey_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,20 ), 0 )
		self.SvererKey_textCtrl.SetMinSize( wx.Size( 150,20 ) )

		bSizer11.Add( self.SvererKey_textCtrl, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer11, 0, wx.TOP|wx.BOTTOM, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		gSizer2.SetMinSize( wx.Size( 240,40 ) )
		self.Save_button = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.Save_button, 0, wx.ALIGN_RIGHT|wx.ALL, 13 )

		self.Cancel_button = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.Cancel_button, 0, wx.ALIGN_LEFT|wx.ALL, 13 )


		bSizer6.Add( gSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		self.UserName_textCtrl.Bind( wx.EVT_TEXT, self.Set_Username )
		self.UserPwd_textCtrl.Bind( wx.EVT_TEXT, self.Set_Userpwd )
		self.SvererKey_textCtrl.Bind( wx.EVT_TEXT, self.Set_ServerKey )
		self.Save_button.Bind( wx.EVT_BUTTON, self.User_Save )
		self.Cancel_button.Bind( wx.EVT_BUTTON, self.User_Cancel )

	def __del__( self ):
		pass
	def Set_Username( self, event ):
		event.Skip()
	def Set_Userpwd( self, event ):
		event.Skip()
	def Set_ServerKey( self, event ):
		event.Skip()
	def User_Save( self, event ):
		user = {}
		user['Username'] = self.UserName_textCtrl.GetValue()
		user['userpassword'] = self.UserPwd_textCtrl.GetValue()
		user['ServerKey'] = self.SvererKey_textCtrl.GetValue()
		print(user)
		user_json = json.dumps(user,ensure_ascii=False)
		try:
			with open('user2.json','w',encoding='utf-8') as f:
				f.write(user_json)
			wx.MessageBox('保存成功', '提示', wx.OK | wx.ICON_INFORMATION)
			self.Close()
		except:
			wx.MessageBox('保存失败', '提示', wx.OK | wx.ICON_INFORMATION)
			self.Close()
		

	def User_Cancel( self, event ):
		self.Close()
