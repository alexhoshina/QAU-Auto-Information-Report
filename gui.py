import sys
sys.path.append('./Gui');
from Main import *
import wx

if __name__ == '__main__':
	app = wx.App()
	frm = Main(None)
	frm.Show(True)
	app.MainLoop()