import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.master.geometry("600x800")
        self.master.title("test")

        a = tk.Canvas(width=550, height=700, bg="cyan")

        for y in range(10):
            for x in range(5):
                a.create_rectangle(
                    x*25, y*25, (x+1)*25, (y+1)*25,
                    outline="white", width=1,
                    fill="gray"
                )

        a.place(x=25, y=50)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()