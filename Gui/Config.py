import json
import os
import re
import wx
import wx.xrc

class Config ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 440,830 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 440,830 ), wx.Size( 440,830 ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer = wx.BoxSizer( wx.VERTICAL )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.CurrentPosition_staticText = wx.StaticText( self, wx.ID_ANY, u"您当前所在地", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.CurrentPosition_staticText.Wrap( -1 )

		bSizer1.Add( self.CurrentPosition_staticText, 0, wx.ALL, 5 )

		self.CurrentPosition_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"中国山东省青岛市城阳区城阳街道青岛农业大学(教学楼)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CurrentPosition_textCtrl.SetMinSize( wx.Size( 120,30 ) )

		bSizer1.Add( self.CurrentPosition_textCtrl, 0, wx.ALL, 5 )


		bSizer.Add( bSizer1, 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.TodaySchedule_staticText = wx.StaticText( self, wx.ID_ANY, u"今日具体行程", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.TodaySchedule_staticText.Wrap( -1 )

		bSizer2.Add( self.TodaySchedule_staticText, 0, wx.ALL, 5 )

		TodaySchedule_comboBoxChoices = [ u"无", u"有" ]
		self.TodaySchedule_comboBox = wx.ComboBox( self, wx.ID_ANY, u"无", wx.DefaultPosition, wx.DefaultSize, TodaySchedule_comboBoxChoices, 0 )
		self.TodaySchedule_comboBox.SetSelection( 0 )
		self.TodaySchedule_comboBox.SetMinSize( wx.Size( 120,30 ) )

		bSizer2.Add( self.TodaySchedule_comboBox, 0, wx.ALL, 5 )


		bSizer.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.BRHGTJZRSFYXLQKOne_staticText = wx.StaticText( self, wx.ID_ANY, u"本人或共同居住人是否有下列情况", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.BRHGTJZRSFYXLQKOne_staticText.Wrap( -1 )

		bSizer3.Add( self.BRHGTJZRSFYXLQKOne_staticText, 0, wx.ALL, 5 )

		BRHGTJZRSFYXLQKOne_comboBoxChoices = [ u"无", u"确诊病例", u"疑似病例", u"无症状感染者" ]
		self.BRHGTJZRSFYXLQKOne_comboBox = wx.ComboBox( self, wx.ID_ANY, u"无", wx.DefaultPosition, wx.DefaultSize, BRHGTJZRSFYXLQKOne_comboBoxChoices, 0 )
		self.BRHGTJZRSFYXLQKOne_comboBox.SetSelection( 0 )
		self.BRHGTJZRSFYXLQKOne_comboBox.SetMinSize( wx.Size( 120,30 ) )

		bSizer3.Add( self.BRHGTJZRSFYXLQKOne_comboBox, 0, wx.ALL, 5 )


		bSizer.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.BRHGTJZRSFYXLQKTwo_staticText = wx.StaticText( self, wx.ID_ANY, u"本人或共同居住人是否有下列情况", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.BRHGTJZRSFYXLQKTwo_staticText.Wrap( -1 )

		bSizer4.Add( self.BRHGTJZRSFYXLQKTwo_staticText, 0, wx.ALL, 5 )

		BRHGTJZRSFYXLQKTwo_comboBoxChoices = [ u"无", u"密切接触者", u"次密切接触者", u"一般接触者", u"其他重点风险人员" ]
		self.BRHGTJZRSFYXLQKTwo_comboBox = wx.ComboBox( self, wx.ID_ANY, u"无", wx.DefaultPosition, wx.DefaultSize, BRHGTJZRSFYXLQKTwo_comboBoxChoices, 0 )
		self.BRHGTJZRSFYXLQKTwo_comboBox.SetSelection( 0 )
		self.BRHGTJZRSFYXLQKTwo_comboBox.SetMinSize( wx.Size( 120,30 ) )

		bSizer4.Add( self.BRHGTJZRSFYXLQKTwo_comboBox, 0, wx.ALL, 5 )


		bSizer.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.SZSQTNSFFSYQ_staticText = wx.StaticText( self, wx.ID_ANY, u"所在县市区7天内是否发生疫情", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.SZSQTNSFFSYQ_staticText.Wrap( -1 )

		bSizer5.Add( self.SZSQTNSFFSYQ_staticText, 0, wx.ALL, 5 )

		SZSQTNSFFSYQ_comboBoxChoices = [ u"否", u"是" ]
		self.SZSQTNSFFSYQ_comboBox = wx.ComboBox( self, wx.ID_ANY, u"否", wx.DefaultPosition, wx.DefaultSize, SZSQTNSFFSYQ_comboBoxChoices, 0 )
		self.SZSQTNSFFSYQ_comboBox.SetSelection( 0 )
		self.SZSQTNSFFSYQ_comboBox.SetMinSize( wx.Size( 120,30 ) )

		bSizer5.Add( self.SZSQTNSFFSYQ_comboBox, 0, wx.ALL, 5 )


		bSizer.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.LJSHJCS_staticText = wx.StaticText( self, wx.ID_ANY, u"7天内本人或家庭成员是否有疫情重点地区旅居史", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.LJSHJCS_staticText.Wrap( -1 )

		bSizer6.Add( self.LJSHJCS_staticText, 0, wx.ALL, 5 )

		LJSHJCS_comboBoxChoices = [ u"否", u"是" ]
		self.LJSHJCS_comboBox = wx.ComboBox( self, wx.ID_ANY, u"否", wx.DefaultPosition, wx.DefaultSize, LJSHJCS_comboBoxChoices, 0 )
		self.LJSHJCS_comboBox.SetSelection( 0 )
		self.LJSHJCS_comboBox.SetMinSize( wx.Size( 120,30 ) )

		bSizer6.Add( self.LJSHJCS_comboBox, 0, wx.ALL, 5 )


		bSizer.Add( bSizer6, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.BRHGTJZRSFYYXZZWQY_staticText = wx.StaticText( self, wx.ID_ANY, u"本人或共同居住人是否有以下症状未痊愈", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.BRHGTJZRSFYYXZZWQY_staticText.Wrap( -1 )

		bSizer7.Add( self.BRHGTJZRSFYYXZZWQY_staticText, 0, wx.ALL, 5 )

		BRHGTJZRSFYYXZZWQY_comboBoxChoices = [ u"无", u"咳嗽或咽痛", u"发热", u"乏力,胸闷等" ]
		self.BRHGTJZRSFYYXZZWQY_comboBox = wx.ComboBox( self, wx.ID_ANY, u"无", wx.DefaultPosition, wx.DefaultSize, BRHGTJZRSFYYXZZWQY_comboBoxChoices, 0 )
		self.BRHGTJZRSFYYXZZWQY_comboBox.SetSelection( 0 )
		self.BRHGTJZRSFYYXZZWQY_comboBox.SetMinSize( wx.Size( 120,30 ) )

		bSizer7.Add( self.BRHGTJZRSFYYXZZWQY_comboBox, 0, wx.ALL, 5 )


		bSizer.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.JRSFCSWFL_staticText = wx.StaticText( self, wx.ID_ANY, u"今日是否从省外返鲁", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.JRSFCSWFL_staticText.Wrap( -1 )

		bSizer8.Add( self.JRSFCSWFL_staticText, 0, wx.ALL, 5 )

		JRSFCSWFL_comboBoxChoices = [ u"否", u"是" ]
		self.JRSFCSWFL_comboBox = wx.ComboBox( self, wx.ID_ANY, u"否", wx.DefaultPosition, wx.DefaultSize, JRSFCSWFL_comboBoxChoices, 0 )
		self.JRSFCSWFL_comboBox.SetSelection( 0 )
		self.JRSFCSWFL_comboBox.SetMinSize( wx.Size( 120,30 ) )

		bSizer8.Add( self.JRSFCSWFL_comboBox, 0, wx.ALL, 5 )


		bSizer.Add( bSizer8, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.JRSFCSNQTDJSFQ_staticText = wx.StaticText( self, wx.ID_ANY, u"今日是否从省内返青", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.JRSFCSNQTDJSFQ_staticText.Wrap( -1 )

		bSizer9.Add( self.JRSFCSNQTDJSFQ_staticText, 0, wx.ALL, 5 )

		JRSFCSNQTDJSFQ_comboBoxChoices = [ u"否", u"是" ]
		self.JRSFCSNQTDJSFQ_comboBox = wx.ComboBox( self, wx.ID_ANY, u"否", wx.DefaultPosition, wx.DefaultSize, JRSFCSNQTDJSFQ_comboBoxChoices, 0 )
		self.JRSFCSNQTDJSFQ_comboBox.SetSelection( 0 )
		self.JRSFCSNQTDJSFQ_comboBox.SetMinSize( wx.Size( 120,30 ) )

		bSizer9.Add( self.JRSFCSNQTDJSFQ_comboBox, 0, wx.ALL, 5 )


		bSizer.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.IsInSchoolOfDay_staticText = wx.StaticText( self, wx.ID_ANY, u"当天是否在校", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.IsInSchoolOfDay_staticText.Wrap( -1 )

		bSizer10.Add( self.IsInSchoolOfDay_staticText, 0, wx.ALL, 5 )

		IsInSchoolOfDay_comboBoxChoices = [ u"否", u"是" ]
		self.IsInSchoolOfDay_comboBox = wx.ComboBox( self, wx.ID_ANY, u"是", wx.DefaultPosition, wx.DefaultSize, IsInSchoolOfDay_comboBoxChoices, 0 )
		self.IsInSchoolOfDay_comboBox.SetSelection( 1 )
		self.IsInSchoolOfDay_comboBox.SetMinSize( wx.Size( 120,30 ) )

		bSizer10.Add( self.IsInSchoolOfDay_comboBox, 0, wx.ALL, 5 )


		bSizer.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.ISNATDay_staticText = wx.StaticText( self, wx.ID_ANY, u"当天是否进行核酸检测", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.ISNATDay_staticText.Wrap( -1 )

		bSizer11.Add( self.ISNATDay_staticText, 0, wx.ALL, 5 )

		ISNATDay_comboBoxChoices = [ u"未检测", u"校内检测", u"校外检测" ]
		self.ISNATDay_comboBox = wx.ComboBox( self, wx.ID_ANY, u"校内检测", wx.DefaultPosition, wx.DefaultSize, ISNATDay_comboBoxChoices, 0 )
		self.ISNATDay_comboBox.SetSelection( 1 )
		self.ISNATDay_comboBox.SetMinSize( wx.Size( 120,30 ) )

		bSizer11.Add( self.ISNATDay_comboBox, 0, wx.ALL, 5 )


		bSizer.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.DayTemperature_staticText = wx.StaticText( self, wx.ID_ANY, u"本人今日体温范围", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.DayTemperature_staticText.Wrap( -1 )

		bSizer12.Add( self.DayTemperature_staticText, 0, wx.ALL, 5 )

		DayTemperature_comboBoxChoices = [ u"36℃以下", u"36℃-37.2℃", u"37.3℃-38℃", u"38℃以上" ]
		self.DayTemperature_comboBox = wx.ComboBox( self, wx.ID_ANY, u"36℃-37.2℃", wx.DefaultPosition, wx.DefaultSize, DayTemperature_comboBoxChoices, 0 )
		self.DayTemperature_comboBox.SetSelection( 1 )
		self.DayTemperature_comboBox.SetMinSize( wx.Size( 120,30 ) )

		bSizer12.Add( self.DayTemperature_comboBox, 0, wx.ALL, 5 )


		bSizer.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.Vaccination_staticText = wx.StaticText( self, wx.ID_ANY, u"疫苗接种情况", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.Vaccination_staticText.Wrap( -1 )

		bSizer13.Add( self.Vaccination_staticText, 0, wx.ALL, 5 )

		Vaccination_comboBoxChoices = [ u"尚未接种", u"已接种第一针", u"已接种第二针", u"已接种第三针" ]
		self.Vaccination_comboBox = wx.ComboBox( self, wx.ID_ANY, u"已接种第三针", wx.DefaultPosition, wx.DefaultSize, Vaccination_comboBoxChoices, 0 )
		self.Vaccination_comboBox.SetSelection( 3 )
		self.Vaccination_comboBox.SetMinSize( wx.Size( 120,30 ) )

		bSizer13.Add( self.Vaccination_comboBox, 0, wx.ALL, 5 )


		bSizer.Add( bSizer13, 1, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.FirstStitchDate_staticText = wx.StaticText( self, wx.ID_ANY, u"第一针接种日期", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.FirstStitchDate_staticText.Wrap( -1 )

		bSizer14.Add( self.FirstStitchDate_staticText, 0, wx.ALL, 5 )

		self.FirstStitchDate_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"2000-13-32", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FirstStitchDate_textCtrl.SetMinSize( wx.Size( 120,30 ) )

		bSizer14.Add( self.FirstStitchDate_textCtrl, 0, wx.ALL, 5 )


		bSizer.Add( bSizer14, 1, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.TwoStitchDate_staticText = wx.StaticText( self, wx.ID_ANY, u"第二针接种日期", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.TwoStitchDate_staticText.Wrap( -1 )

		bSizer15.Add( self.TwoStitchDate_staticText, 0, wx.ALL, 5 )

		self.TwoStitchDate_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"2000-13-32", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TwoStitchDate_textCtrl.SetMinSize( wx.Size( 120,30 ) )

		bSizer15.Add( self.TwoStitchDate_textCtrl, 0, wx.ALL, 5 )


		bSizer.Add( bSizer15, 1, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.ThreeStitchDate_staticText = wx.StaticText( self, wx.ID_ANY, u"第三针接种日期", wx.DefaultPosition, wx.Size( 260,20 ), 0 )
		self.ThreeStitchDate_staticText.Wrap( -1 )

		bSizer16.Add( self.ThreeStitchDate_staticText, 0, wx.ALL, 5 )

		self.ThreeStitchDate_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"2000-13-32", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ThreeStitchDate_textCtrl.SetMinSize( wx.Size( 120,30 ) )

		bSizer16.Add( self.ThreeStitchDate_textCtrl, 0, wx.ALL, 5 )


		bSizer.Add( bSizer16, 1, wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		gSizer3.SetMinSize( wx.Size( 240,40 ) )
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button3, 0, wx.ALIGN_RIGHT|wx.ALL, 13 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button4, 0, wx.ALIGN_LEFT|wx.ALL, 13 )


		bSizer.Add( gSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.Config_Save )
		self.m_button4.Bind( wx.EVT_BUTTON, self.Config_Cancel )

	def __del__( self ):
		pass

	def check_config(self,config):
			for key in config:
				if (config[key] == '是' or config[key] == '有' or config[key] == '未检测' or config[key] == '36℃以下' or config[key] == '尚未接种'):
					config[key] = '0'
				elif (config[key] == '否' or config[key] == '无' or config[key] == '确诊病例' or config[key] == '密切接触者' or config[key] == '咳嗽或咽痛' or config[key] == '校内检测' or config[key] == '36℃-37.2℃' or config[key] == '已接种第一针'):
					config[key] = '1'
				elif (config[key] == '疑似病例' or config[key] == '次密切接触者' or config[key] == '发热' or config[key] == '校外检测' or config[key] == '37.3℃-38℃' or config[key] == '已接种第二针'):
					config[key] = '2'
				elif (config[key] == '无症状感染者' or config[key] == '乏力,胸闷等' or config[key] == '38℃以上' or config[key] == '已接种第三针'):
					config[key] = '3'
				elif (config[key] == '其他重点风险人员'):
					config[key] = '4'
			return config
	# Virtual event handlers, override them in your derived class
	def Config_Save( self, event ):
		config = {'cookies':'{"insert_cookie":"29594869"}'}
		config['CurrentPosition'] = self.CurrentPosition_textCtrl.GetValue()
		config['Country'] = re.search(r"(.+?国)",config['CurrentPosition']).group(1)
		config['Province'] = re.search(r"国(.+?省)",config['CurrentPosition']).group(1)
		config['City'] = re.search(r"省(.+?市)",config['CurrentPosition']).group(1)
		if (re.search(r"市(.+?市)",config['CurrentPosition'])):
			config['County'] = re.search(r"市(.+?市)",config['CurrentPosition']).group(1)
		elif (re.search(r"市(.+?区)",config['CurrentPosition'])):
			config['County'] = re.search(r"市(.+?区)",config['CurrentPosition']).group(1)
		elif (re.search(r"市(.+?县)",config['CurrentPosition'])):
			config['County'] = re.search(r"市(.+?县)",config['CurrentPosition']).group(1)

		if (re.search(r"区(.+?路)",config['CurrentPosition'])):
			config['street_number'] = re.search(r"区(.+?路)",config['CurrentPosition']).group(1)
		elif (re.search(r"县(.+?路)",config['CurrentPosition'])):
			config['street_number'] = re.search(r"县(.+?路)",config['CurrentPosition']).group(1)
		elif (re.search(r"市(.+?路)",config['CurrentPosition'])):
			config['street_number'] = re.search(r"市.+?市(.+?路)",config['CurrentPosition']).group(1)

		config['FirstStitchDate'] = self.FirstStitchDate_textCtrl.GetValue()
		config['TwoStitchDate'] = self.TwoStitchDate_textCtrl.GetValue()
		config['ThreeStitchDate'] = self.ThreeStitchDate_textCtrl.GetValue()
		config['Vaccination'] = self.Vaccination_comboBox.GetValue()
		config['TodaySchedule'] = self.TodaySchedule_comboBox.GetValue()
		config['BRHGTJZRSFYXLQKOne'] = self.BRHGTJZRSFYXLQKOne_comboBox.GetValue()
		config['BRHGTJZRSFYXLQKTwo'] = self.BRHGTJZRSFYXLQKTwo_comboBox.GetValue()
		config['SZSQTNSFFSYQ'] = self.SZSQTNSFFSYQ_comboBox.GetValue()
		config['LJSHJCS'] = self.LJSHJCS_comboBox.GetValue()
		config['BRHGTJZRSFYYXZZWQY'] = self.BRHGTJZRSFYXLQKOne_comboBox.GetValue()
		config['JRSFCSWFL'] = self.JRSFCSWFL_comboBox.GetValue()
		config['JRSFCSNQTDJSFQ'] = self.JRSFCSNQTDJSFQ_comboBox.GetValue()
		config['DayTemperature'] = self.DayTemperature_comboBox.GetValue()
		config['IsInSchoolOfDay'] = self.IsInSchoolOfDay_comboBox.GetValue()
		config['ISNATDay'] = self.ISNATDay_comboBox.GetValue()
		config = self.check_config(config)
		config['cookies'] = json.loads(config['cookies'])
		config_json = json.dumps(config,ensure_ascii=False)
		try:
			with open('config2.json','w',encoding='utf-8') as f:
				f.write(config_json)
			wx.MessageBox('保存成功', '提示', wx.OK | wx.ICON_INFORMATION)
			self.Close()
		except:
			wx.MessageBox('保存失败', '提示', wx.OK | wx.ICON_INFORMATION)
			self.Close()
		

	
	def Config_Cancel( self, event ):
		self.Close()
