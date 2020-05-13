import tkinter as tk


class Application (tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.master.title("Programiranje 2")
        self.master.geometry("300x200")
        # self.pack()
        self.napravi_sucelje()

    def napravi_sucelje(self):
        self.pozdravBtn = tk.Button(self.master)
        self.pozdravBtn["text"] = "Pozdrav"
        self.pozdravBtn["command"] = self.pozdrav

        self.pozdravBtn["width"] = 6
        self.pozdravBtn["height"] = 2

        self.pozdravBtn.grid(row=0, column=0)

        self.ugasiBtn = tk.Button(
            self.master,
            text="Ugasi",
            bg='red',
            command=self.master.destroy,
            height=2, width=6
        )
        self.ugasiBtn.grid(row=0, column=1, padx=(10, 10))

    def pozdrav(self):
        print("Pozdrav iz sučelja")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
