import wx
import wx.xrc
import webbrowser
import os
import main as Dr
from Config import *
from User import *

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"QAU-Report(青岛农业大学每日上报)", pos = wx.DefaultPosition, size = wx.Size( 640,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 640,450 ), wx.Size( 640,450 ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Gui\image\image.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_bitmap2, 0, wx.ALL, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer23.SetMinSize( wx.Size( 200,40 ) )
		self.m_button7 = wx.Button( self, wx.ID_ANY, u"配置用户信息", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.m_button7.SetMinSize( wx.Size( 100,30 ) )
		self.m_button7.SetMaxSize( wx.Size( 100,30 ) )

		bSizer23.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"配置上报信息", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.m_button8.SetMinSize( wx.Size( 100,30 ) )
		self.m_button8.SetMaxSize( wx.Size( 100,30 ) )

		bSizer23.Add( self.m_button8, 0, wx.ALL, 5 )


		bSizer25.Add( bSizer23, 1, wx.EXPAND, 5 )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		bSizer26.SetMinSize( wx.Size( 200,60 ) )
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer26.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,60 ), 0 )
		self.m_textCtrl8.SetMinSize( wx.Size( 200,60 ) )
		self.m_textCtrl8.SetMaxSize( wx.Size( 200,60 ) )

		bSizer26.Add( self.m_textCtrl8, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer25.Add( bSizer26, 1, wx.EXPAND, 5 )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"开机自动上报", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"上报后自动关闭", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, u"上报失败自动再次上报", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_checkBox3, 0, wx.ALL, 5 )


		bSizer25.Add( bSizer27, 1, wx.EXPAND, 5 )

		self.m_toggleBtn1 = wx.ToggleButton( self, wx.ID_ANY, u"开始上报！", wx.DefaultPosition, wx.Size( 200,30 ), 0 )
		self.m_toggleBtn1.SetMinSize( wx.Size( 200,30 ) )
		self.m_toggleBtn1.SetMaxSize( wx.Size( 200,30 ) )

		bSizer25.Add( self.m_toggleBtn1, 0, wx.ALL|wx.EXPAND, 10 )


		bSizer30.Add( bSizer25, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer30 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menu11 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"打开User.json", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"打开 Config.json", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem2 )

		self.m_menu1.AppendSubMenu( self.m_menu11, u"打开源文件" )

		self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"退出", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem4 )

		self.m_menubar1.Append( self.m_menu1, u"菜单" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"使用说明", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem5 )

		self.m_menuItem6 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"项目GitHub", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem6 )

		self.m_menubar1.Append( self.m_menu2, u"帮助" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.Start_User )
		self.m_button8.Bind( wx.EVT_BUTTON, self.Start_Config )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.Auto_Switch )
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.Close_Switch )
		self.m_checkBox3.Bind( wx.EVT_CHECKBOX, self.Again_Switch )
		self.m_toggleBtn1.Bind( wx.EVT_TOGGLEBUTTON, self.Start_Report )
		self.Bind( wx.EVT_MENU, self.Open_User, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.Open_Config, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.Quit, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.Open_help, id = self.m_menuItem5.GetId() )
		self.Bind( wx.EVT_MENU, self.Open_Github, id = self.m_menuItem6.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Start_User( self, event ):
		self.user = User(None)
		self.user.Show()

	def Start_Config( self, event ):
		self.config = Config(None)
		self.config.Show()

	def Auto_Switch( self, event ):
		event.Skip()

	def Close_Switch( self, event ):
		event.Skip()

	def Again_Switch( self, event ):
		event.Skip()

	def Start_Report( self, event ):
		if (Dr.main()):
			wx.MessageBox('上报成功', '提示', wx.OK | wx.ICON_INFORMATION)

	def Open_User( self, event ):
		os.system("start explorer User.json")

	def Open_Config( self, event ):
		os.system("start explorer config.json")

	def Quit( self, event ):
		self.Close()

	def Open_help( self, event ):
		os.system("start explorer Specification.txt")

	def Open_Github( self, event ):
		webbrowser.open_new_tab('https://github.com/alexhoshina/QAU-Auto-Information-Report')