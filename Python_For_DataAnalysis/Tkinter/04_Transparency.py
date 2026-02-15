# import tkinter as tk

# root = tk.Tk()
# root.title("Thinker")
# root.geometry("600x600+50+50")
# root.resizable(False, False)
# root.attributes("-alpha", 0.9)
# root.mainloop()

# import tkinter as tk


# root = tk.Tk()
# root.title("Tkinter Window Demo")
# root.geometry("300x200+50+50")
# root.resizable(0, 0)
# root.attributes("-topmost", 1)

# root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("Tkinter Window Demo")
root.geometry("300x200+50+50")
root.resizable(False, False)

try:
    # Use iconphoto on Linux and macOS
    photo = tk.PhotoImage(file="./demo.png")
    root.iconphoto(False, photo)
except tk.TclError:
    print("icon file not found.")

root.mainloop()
