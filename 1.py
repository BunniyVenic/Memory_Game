import customtkinter

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        app = customtkinter.CTk()
        app.title("Memory game")
        app.geometry("400x150")
        customtkinter.set_appearance_mode("Dark")  # Themes: "blue" (standard), "green", "dark-blue"



        button = customtkinter.CTkButton(app, text="my button", command=self.button_callback, fg_color=("dark blue"))
        #button = customtkinter.CTkButton(root_tk, fg_color="red")  # single color name
        #button = customtkinter.CTkButton(root_tk, fg_color="#FF0000")  # single hex string
        #button = customtkinter.CTkButton(root_tk, fg_color=("#DB3E39", "#821D1A"))  # tuple color
        button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        #app.grid_columnconfigure(0, weight=1)
        app.mainloop()
    def button_callback(self):
        print("button pressed")
app=App()
app.mainloop()