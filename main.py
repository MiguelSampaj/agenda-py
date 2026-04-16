import re
import sqlite3 as sql
from customtkinter import *

set_appearance_mode('dark')
text_color = '#f8f3de'
main_color = '#ff4103'
sup_color = '#ec2800'

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('500x350')
        self.title('Login')
        self.resizable(width=False, height=False)
        self.configure(fg_color='#001321')

        main_font = CTkFont(family='Segoe UI light', size=40)
        sup_font = CTkFont(family='Segoe UI light', size=20)

        class FrameLogin(CTkFrame):
            def __init__(self, master, **kwargs):
                super().__init__(master, **kwargs, width=400, height=250, fg_color='#061827', corner_radius=25)
                self.grid_propagate(False)

        class LabelTitle(CTkLabel):
            def __init__(self, master, **kwargs):
                super().__init__(master, **kwargs, font=main_font, text_color=main_color)

        class LabelButton(CTkLabel):
            def __init__(self, master, **kwargs):
                super().__init__(master, **kwargs, font=sup_font, text_color=main_color)

        # Root 1
        lbl_login = LabelTitle(self, text='LOGIN')
        lbl_login.grid(pady=10, row=0)

        frame_login = FrameLogin(self)
        frame_login.grid(padx=50, pady=0, row=1)

        # Root 2
        # GON
        lbl_gon = LabelButton(frame_login, text='GON')
        lbl_gon.grid(row=0, column=0, pady=10, padx=180)

        ent_gon = CTkEntry(frame_login,
                           width=200,
                           height=15,
                           fg_color='#061827',
                           text_color=text_color,
                           border_color=text_color)
        ent_gon.grid(row=1, column=0)

        # Senha
        frame_senha = CTkFrame(frame_login,
                               width=200,
                               height=24,
                               fg_color='transparent',
                               corner_radius=0)
        frame_senha.grid_propagate(False)
        frame_senha.grid(row=3, column=0)

        lbl_senha = LabelButton(frame_login, text='SENHA')
        lbl_senha.grid(row=2, column=0, pady=10)

        ent_senha = CTkEntry(frame_senha,
                           width=170,
                           height=15,
                           fg_color='#061827',
                           text_color=text_color,
                           border_color=text_color)
        ent_senha.grid(row=0, column=0)

        check_senha = CTkCheckBox(frame_senha,
                                  width=15,
                                  height=15,
                                  corner_radius=360,
                                  text='',
                                  fg_color=main_color,
                                  border_color=text_color,
                                  border_width=2,
                                  hover_color=main_color)
        check_senha.grid(row=0, column=1, padx=5)

        # Botão de LOGIN
        but_login = CTkButton(frame_login,
                              width=100,
                              height=35,
                              text='login',
                              font=CTkFont(family='Segoe UI light', size=16),
                              text_color=text_color,
                              fg_color=main_color,
                              hover_color=sup_color)
        but_login.grid(row=4, column=0, pady=15)


app = App()
app.mainloop()
