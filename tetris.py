from META import EventHandller, GameManager
import tkinter as tk

root = tk.Tk()
app = GameManager()
manage = EventHandller(root, app)
app.window.mainloop()
