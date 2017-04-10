import wx 

class SettingsPanel(wx.MiniFrame):

    def __init__(self, parent, id=wx.ID_ANY, title="Settings Panel", pos=wx.DefaultPosition,
             size=wx.DefaultSize,
             style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.FRAME_NO_TASKBAR
             | wx.FRAME_FLOAT_ON_PARENT | wx.CLIP_CHILDREN):

        wx.MiniFrame.__init__(self, parent, id, title, pos, size, style)

        self.targetTitleBar = parent.titleBar
        self.parent = parent
        self.panel = wx.Panel(self, -1)

        self.targetTitleBar.Refresh() # an example of calling the mock object

class MockTitleBar(object):
    def __init__(self):
        pass
    def Refresh(self):
        print "refresh"

app = wx.PySimpleApp()
title_bar = MockTitleBar()
top_frame = wx.Frame(None)
top_frame.titleBar = title_bar
frame = SettingsPanel(top_frame)
# top_frame.Show()
frame.Show()
app.MainLoop()
