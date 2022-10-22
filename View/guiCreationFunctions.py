import wx
import copy

def create_list(panel ,headings, sizes):
    return_list = wx.ListCtrl(
        panel, size = (-1, 100),
        style = wx.LC_REPORT | wx.BORDER_SUNKEN
    )
    for i in range(len(headings)):
        return_list.InsertColumn(i, headings[i], width=sizes[i])
    return return_list

def create_button(panel, name, function_on_press):
    return_button = wx.Button(panel, label=name)
    return_button.Bind(wx.EVT_BUTTON, function_on_press)
    return return_button


class Test:
    def __init__(self,name):
        self.name = name

    def print_name(self):
        print(self.name)

if __name__ == '__main__':
    a = Test('Erstens')
    b = copy.deepcopy(a)
    c = a
    c.name = "Was anderes"
    print(f"Name of a: {a.name}") #Name of a: Was anderes
    #print(a)
    print(f"Name of b: {b.name}") #Name of b: Erstens
    #print(b)
