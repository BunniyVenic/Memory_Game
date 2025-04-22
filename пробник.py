import customtkinter as ctk
#не забывай заменять customtkinter на ctk
class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        app = ctk.CTk()
        app.title("Memory game")
        app.geometry("400x500")
        ctk.set_appearance_mode("Dark")

        button = ctk.CTkButton(app, text="my button", command=self.button_callback, fg_color=("dark blue"))
        #button = customtkinter.CTkButton(root_tk, fg_color="red")  # single color name
        #button = customtkinter.CTkButton(root_tk, fg_color="#FF0000")  # single hex string
        #button = customtkinter.CTkButton(root_tk, fg_color=("#DB3E39", "#821D1A"))  # tuple color
        button.grid(row=0, column=0, padx=200, pady=20, sticky="ew")
        app.grid_columnconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self, width=510,height=290)
        self.main_frame.grid(row=0, column=10,columnspan=10, rowspan=10, ipadx=5, ipady=0, padx=0, pady=0, sticky="nw")
        self.main_frame.grid_rowconfigure(3, weight=1)

        self.switch_var = ctk.StringVar()
        self.switch_mode = ctk.CTkSwitch(self.main_frame,text="🌙",font=("Arial", 25), variable=self.switch_var,onvalue="on", offvalue="off",command=self.change_appearance_mode_event)
        self.switch_mode.grid(row=5, column=0, pady=100, padx=200, sticky="n")


        button = ctk.CTkButton(app, text="my button", command=self.button_callback, fg_color=("dark blue"))
        #button = customtkinter.CTkButton(root_tk, fg_color="red")  # single color name
        #button = customtkinter.CTkButton(root_tk, fg_color="#FF0000")  # single hex string
        #button = customtkinter.CTkButton(root_tk, fg_color=("#DB3E39", "#821D1A"))  # tuple color
        button.grid(row=0, column=0, padx=200, pady=20, sticky="ew")
        app.grid_columnconfigure(0, weight=1)

    def change_appearance_mode_event(self):
        if self.switch_var.get() == "on":
            ctk.set_appearance_mode("light")
            self.switch_mode.configure(text="☀")
        else:
            ctk.set_appearance_mode("dark")
            self.switch_mode.configure(text="🌙")
        app.mainloop()
    def button_callback(self):
        print("button pressed")
app=App()
app.mainloop()