import glob
import wx
import guiCreationFunctions as create

class ArgumentPanel(wx.Panel):    
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.row_obj_dict = {}
        self.index = 0

        self.argument_list = create.create_list(self, ['Type','Position','Pattern', 'Arguments'], [60, 60, 240, 240])
        main_sizer.Add(self.argument_list, 0, wx.ALL | wx.EXPAND, 5)    
    
        edit_button = create.create_button(self, 'Edit', self.getLine)
        main_sizer.Add(edit_button, 0, wx.ALL | wx.CENTER, 5) 
  
        set_button = create.create_button(self, 'Set', self.add_line)
        main_sizer.Add(set_button, 0, wx.ALL | wx.CENTER, 5)

        self.SetSizer(main_sizer)

    def getLine(self, event):
        column_count = self.argument_list.GetColumnCount()
        line = []
        for column in range(column_count):
            item = self.argument_list.GetItem(0, column)
            line.append(item.GetText())
        print(line)

    def add_line(self, event):
        line = f"Line {self.index}"
        self.argument_list.InsertItem(self.index, line)
        self.argument_list.SetItem(self.index, 1, "01/19/2010")
        self.index = self.index + 1


class MainFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None,
                         title='files-to-csv')
        self.panel = ArgumentPanel(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
