import wx
import wolframalpha
import wikipedia
class akil(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(400, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Nakchathira")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hiii I am Nakchathira Akil's Digital Answerer.Can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        a = self.txt.GetValue()
        a = a.lower()
        try:
            app_id="L7PRE7-2UWJGRQ6AU"
            client=wolframalpha.Client(app_id)
            res=client.query(a)
            answer=next(res.results).text
            print(answer)
        except:
            a=a.split(' ')
            a=" ".join(a[2:])
            print(wikipedia.summary(a))


if __name__ == "__main__":
    app = wx.App(True)
    frame = akil()
    app.MainLoop()
