import re
import sqlite3
import sqlite3 as sql
from customtkinter import *
from rich.traceback import install

# Deixar os erros mais visiveis
install()

# Setando as configs
# CTk
set_appearance_mode('dark')
text_color = '#f8f3de'
main_color = '#ff4103'
sup_color = '#ec2800'

# Sqlite3
conexao = sql.connect('data.db')
cursor = conexao.cursor()

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('500x350')
        self.title('Login')
        self.resizable(width=False, height=False)
        self.configure(fg_color='#001321')

        # Setando as tabelas do .db
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        gon TEXT NOT NULL,
        key TEXT NOT NULL
        )""")

        def fechar_main():
            self.destroy()

        main_font = CTkFont(family='Segoe UI light', size=40)
        sup_font = CTkFont(family='Segoe UI light', size=20)
        but_font = CTkFont(family='Segoe UI light', size=16)
        pattern_gon = re.compile(r'^gon0[0-9]{6}@aluno\.firjansenaisesi\.com\.br$')

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
                           width=250,
                           height=15,
                           fg_color='#061827',
                           text_color=text_color,
                           border_color=text_color)
        ent_gon.grid(row=1, column=0)

        # Senha
        frame_senha = CTkFrame(frame_login,
                               width=250,
                               height=24,
                               fg_color='transparent',
                               corner_radius=0)
        frame_senha.grid_propagate(False)
        frame_senha.grid(row=3, column=0)

        lbl_senha = LabelButton(frame_login, text='SENHA')
        lbl_senha.grid(row=2, column=0, pady=10)

        ent_senha = CTkEntry(frame_senha,
                           width=221,
                           height=15,
                           fg_color='#061827',
                           text_color=text_color,
                           border_color=text_color)
        ent_senha.grid(row=0, column=0)

        # Função do checkbox de esconder senha
        check_senha_bool = BooleanVar(value=False)
        def func_check_senha():
            if check_senha_bool.get():
                ent_senha.configure(show='*')
            elif not check_senha_bool.get():
                ent_senha.configure(show='')

        check_senha = CTkCheckBox(frame_senha,
                                  width=15,
                                  height=15,
                                  corner_radius=360,
                                  text='',
                                  fg_color=main_color,
                                  border_color=text_color,
                                  border_width=2,
                                  hover_color=main_color,
                                  variable=check_senha_bool,
                                  offvalue=False,
                                  onvalue=True,
                                  command=func_check_senha)
        check_senha.grid(row=0, column=1, padx=5)

        # Botão de LOGIN
        but_login = CTkButton(frame_login,
                              width=100,
                              height=35,
                              text='login',
                              font=but_font,
                              text_color=text_color,
                              fg_color=main_color,
                              hover_color=sup_color)
        but_login.grid(row=4, column=0, pady=(15, 0))

        # Botão de Cadastrar
        def func_but_cadastrar():
            # TopLevel do cadastro
            class CadastrarTopLvl(CTkToplevel):
                def __init__(self, master, **kwargs):
                    super().__init__(master, **kwargs, fg_color='#001321')
                    self.resizable(False, False)
                    self.title('Cadastrar')
                    self.geometry('500x600')
                    self.protocol('WM_DELETE_WINDOW', fechar_main)

                    # Root 1
                    lbl_cadastro = LabelTitle(self, text='CADASTRO')
                    lbl_cadastro.grid(row=0, column=0, pady=10)

                    frame_widgets = FrameLogin(self)
                    frame_widgets.configure(height=500)
                    frame_widgets.grid(row=1, column=0, padx=50, pady=0)

                    # Root 2
                    # Username
                    lbl_user = LabelButton(frame_widgets, text='Username')
                    lbl_user.grid(row=0, column=0, pady=10, padx=150)

                    ent_user = CTkEntry(frame_widgets,
                                        width=250,
                                        height=25,
                                        fg_color='#061827',
                                        text_color=text_color,
                                        border_color=text_color,
                                        placeholder_text='(Ex: João Silva; joão_silva; joao_silva)',
                                        placeholder_text_color='#193140',
                                        font=CTkFont(family='Segoe UI light', size=10))
                    ent_user.grid(row=1, column=0)

                    # GON
                    lbl_gon_cad = LabelButton(frame_widgets, text='GON')
                    lbl_gon_cad.grid(row=2, column=0, pady=10, padx=180)

                    ent_gon_cad = CTkEntry(frame_widgets,
                                            width=250,
                                            height=25,
                                            fg_color='#061827',
                                            text_color=text_color,
                                            border_color=text_color,
                                            placeholder_text='(Ex: gon0123456@aluno.firjansenaisesi.com.br)',
                                            placeholder_text_color='#193140',
                                            font=CTkFont(family='Segoe UI light', size=10))
                    ent_gon_cad.grid(row=3, column=0)

                    # Senha
                    frame_senha_cad = CTkFrame(frame_widgets,
                                               width=250,
                                               height=24,
                                               fg_color='transparent',
                                               corner_radius=0)
                    frame_senha_cad.grid_propagate(False)
                    frame_senha_cad.grid(row=5, column=0)

                    lbl_senha_cad = LabelButton(frame_widgets, text='SENHA')
                    lbl_senha_cad.grid(row=4, column=0, pady=10)

                    ent_senha_cad = CTkEntry(frame_senha_cad,
                                             width=221,
                                             height=15,
                                             fg_color='#061827',
                                             text_color=text_color,
                                             border_color=text_color,
                                             placeholder_text='(Ex: joaozinho123@a)',
                                             placeholder_text_color='#193140')
                    ent_senha_cad.grid(row=0, column=0)

                    # Função do checkbox de esconder senha
                    check_senha_bool_cad = BooleanVar(value=False)

                    def func_check_senha_cad():
                        if check_senha_bool_cad.get():
                            ent_senha_cad.configure(show='*')
                        elif not check_senha_bool_cad.get():
                            ent_senha_cad.configure(show='')

                    check_senha_cad = CTkCheckBox(frame_senha_cad,
                                              width=15,
                                              height=15,
                                              corner_radius=360,
                                              text='',
                                              fg_color=main_color,
                                              border_color=text_color,
                                              border_width=2,
                                              hover_color=main_color,
                                              variable=check_senha_bool_cad,
                                              offvalue=False,
                                              onvalue=True,
                                              command=func_check_senha_cad)
                    check_senha_cad.grid(row=0, column=1, padx=5)

                    # Confirmar senha
                    frame_senha2_cad = CTkFrame(frame_widgets,
                                               width=250,
                                               height=24,
                                               fg_color='transparent',
                                               corner_radius=0)
                    frame_senha2_cad.grid_propagate(False)
                    frame_senha2_cad.grid(row=7, column=0)

                    lbl_senha2_cad = LabelButton(frame_widgets, text='CONFIRMAR SENHA')
                    lbl_senha2_cad.grid(row=6, column=0, pady=10)

                    ent_senha2_cad = CTkEntry(frame_senha2_cad,
                                             width=221,
                                             height=15,
                                             fg_color='#061827',
                                             text_color=text_color,
                                             border_color=text_color,
                                             placeholder_text='(Ex: joaozinho123@a)',
                                             placeholder_text_color='#193140')
                    ent_senha2_cad.grid(row=0, column=0)

                    # Função do checkbox de esconder senha
                    check_senha2_bool_cad = BooleanVar(value=False)

                    def func_check_senha2_cad():
                        if check_senha2_bool_cad.get():
                            ent_senha2_cad.configure(show='*')
                        elif not check_senha2_bool_cad.get():
                            ent_senha2_cad.configure(show='')

                    check_senha2_cad = CTkCheckBox(frame_senha2_cad,
                                                  width=15,
                                                  height=15,
                                                  corner_radius=360,
                                                  text='',
                                                  fg_color=main_color,
                                                  border_color=text_color,
                                                  border_width=2,
                                                  hover_color=main_color,
                                                  variable=check_senha2_bool_cad,
                                                  offvalue=False,
                                                  onvalue=True,
                                                  command=func_check_senha2_cad)
                    check_senha2_cad.grid(row=0, column=1, padx=5)

                    # Botão Cadastro
                    # Função do Botão
                    def func_button_cadastro():
                        username = str(ent_user.get())
                        gon = str(ent_gon_cad.get()).lower()
                        senha = str(ent_senha_cad.get())
                        conf_senha = str(ent_senha2_cad.get())

                        valido = True

                        # Verificando se o username é válido
                        if not(6 <= len(username) <= 20):
                            valido = False

                        # Verificações com a senha
                        equal_key = senha == conf_senha
                        if equal_key:
                            # Verificando o tamanho
                            if not(6 <= len(senha) <= 20):
                                valido = False

                            # Verificando se há uma letra maiúscula e uma minúscula
                            if senha.isupper() or senha.islower():
                                valido = False

                            # Verificando se há um caractere especial
                            pattern_have_special_char = re.compile(r'[!@#$%.*()/\[\]&]')
                            if not(pattern_have_special_char.search(senha)):
                                valido = False

                            # Verificando se há um número
                            pattern_have_number = re.compile(r'[0-9]')
                            if not pattern_have_number.search(senha):
                                valido = False
                        else:
                            valido = False

                        # Verificando se o GON é válido
                        if not(pattern_gon.match(gon)):
                            valido = False

                        if valido:
                            pass

                        if not valido:
                            lbl_regras_senha.configure(text_color=sup_color)
                            lbl_regras_senha.after(1000, lambda: lbl_regras_senha.configure(text_color=text_color))

                    # Corpo do Botão
                    but_cadastro = CTkButton(frame_widgets,
                                             width=130,
                                             height=35,
                                             fg_color=main_color,
                                             hover_color=sup_color,
                                             font=but_font,
                                             text_color=text_color,
                                             text='cadastrar',
                                             command=func_button_cadastro)
                    but_cadastro.grid(row=8, column=0, pady=(25, 0), columnspan=2)

                    # Regras de senha
                    lbl_regras_senha = CTkLabel(frame_widgets,
                                                text='''A senha deve conter:
    * 6-20 caracteres
    * Ao menos uma letra maiúscula e uma minúscula
    * Ao menos um caractere especial (!@#$%&.)
    * Ao menos um número
O username deve conter:
    * 6-20 caracteres''',
                                                text_color=text_color,
                                                font=CTkFont(family='Segoe UI light', size=13),
                                                justify='left')
                    lbl_regras_senha.grid(row=9, column=0, pady=15, columnspan=2)

            self.withdraw()
            cadastrar_toplvl = CadastrarTopLvl(self)

        but_cadastrar = CTkButton(frame_login,
                                  width=100,
                                  height=15,
                                  bg_color='#061827',
                                  fg_color='#061827',
                                  hover_color='#061827',
                                  text_color=main_color,
                                  text='cadastrar',
                                  font=CTkFont(family='Segoe UI light',
                                               size=12,
                                               underline=True),
                                  command=func_but_cadastrar)
        but_cadastrar.grid(row=5, column=0, pady=10)

conexao.commit()
app = App()
app.mainloop()
