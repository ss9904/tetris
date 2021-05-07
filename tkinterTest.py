from hoge import main
import tkinter

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.geometry("400x600")
        self.master.title("test")


        toolbar = tkinter.Frame(self.master)
        
        for i in range(3):
            button= tkinter.Button(toolbar, text=str(i), width=2)
            button.pack(side=tkinter.LEFT)

        toolbar.pack(fill=tkinter.X)




if __name__ == "__main__":
    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()