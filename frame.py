#!/usr/bin/env python
import wx
import download

class MyPanel(wx.Panel):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.FlexGridSizer(4, 3, 10, 10)

        urlLabel = wx.StaticText(self, label="Url:")
        self.url = wx.TextCtrl(self)
        spacer1 = wx.StaticText(self, label="")

        pathLabel = wx.StaticText(self, label="Path:")
        self.path = wx.TextCtrl(self)
        spacer2 = wx.StaticText(self, label="")
        spacer3 = wx.StaticText(self, label="")
        spacer4 = wx.StaticText(self, label="")

        ChoosePathBtn = wx.Button(self, label="Choose Path")

        progressLabel = wx.StaticText(self, label="Progress:")
        progress = wx.Gauge(self)
        BeginDownloadBtn = wx.Button(self, label="Download")

        sizer.AddMany([(urlLabel), (self.url, 1, wx.EXPAND), (spacer1),
            (pathLabel), (self.path, 1, wx.EXPAND), (ChoosePathBtn),
            (progressLabel), (progress, 1, wx.EXPAND), (spacer2),
            (spacer3), (BeginDownloadBtn, 1, wx.EXPAND), (spacer4)])

        sizer.AddGrowableCol(1, 1)

        hbox.Add(sizer, proportion = 2, flag = wx.ALL|wx.EXPAND, border = 15)
        self.SetSizer(hbox)


        self.SetAutoLayout(1)
        self.Show(True)

        self.Bind(wx.EVT_BUTTON, self.ChoosePath, ChoosePathBtn)

        self.Bind(wx.EVT_BUTTON, self.BeginDownload, BeginDownloadBtn)        

        self.pathValue = ""

    def ChoosePath(self, event):
        dialog = wx.DirDialog(None, "Choose a directory:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.pathValue = dialog.GetPath()
            self.path.SetValue(self.pathValue)

    def BeginDownload(self, event):
        path = self.path.GetValue()
        url = self.url.GetValue()

        download.getHtml(url, path)

app = wx.App(False)
frame = wx.Frame(None)
panel = MyPanel(frame)
frame.Show();
app.MainLoop()