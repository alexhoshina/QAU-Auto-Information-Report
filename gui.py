import sys
sys.path.append('./Gui');
from Main import *
import wx

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
	app = wx.App()
	frm = Main(None)
	frm.Show(True)
	app.MainLoop()