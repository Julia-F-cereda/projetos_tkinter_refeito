import ttkbootstrap as ttk
from tkinter import messagebox
import sqlite3

class Menu_cadastro():
    def __init__(self, janela_pai):
        self.menu_cadastro = ttk.Toplevel(janela_pai)
        self.janela_pai = janela_pai
        self.menu_cadastro.geometry("1920x1080")

        self.Label_titulo = ttk.Label(self.menu_cadastro,
                                    text="Login",
                                    foreground="pink",
                                    font=("Times New Roman",40))
        self.Label_titulo.pack(pady=10)

        #Label para o nome da caixa nome
        self.label_nome = ttk.Label(self.menu_cadastro,
                                     text="Nome completo",
                                     font=("Times New Roman",15))
        self.label_nome.pack()

      #Entry caixa para por o login
        self.entry_nome = ttk.Entry(self.menu_cadastro,
                                   text="Nome completo")
        self.entry_nome.pack(pady=10)



      #Label para o nome da caixa usuario
        self.label_usuario = ttk.Label(self.menu_cadastro,
                                     text="Usuário",
                                     font=("Times New Roman",15))
        self.label_usuario.pack()

      #Entry caixa para por o login
        self.entry_usuario = ttk.Entry(self.menu_cadastro,
                                   text="Usuário")
        self.entry_usuario.pack(pady=10)

      #label para o nome senha
        self.label_senha = ttk.Label(self.menu_cadastro,
                                   text="Senha",
                                   font=("Times New Roman",15))
        self.label_senha.pack()

      #entry para por a caixa p senha
        self.entry_senha = ttk.Entry(self.menu_cadastro,
                                   text="Senha",
                                   show="*") #para mnao mosrrar a senha
        self.entry_senha.pack()

        self.button_cadastro = ttk.Button(self.menu_cadastro,
                                          text="Cadastrar",
                                          command= self.inserir_usuario)
        self.button_cadastro.pack()

        self.criar_tabela_usuario()

        self.usuario = None

#############################################################################################################
    def criar_tabela_usuario(self):
       #criar conexao
       conexao = sqlite3.connect("05_Lista_Tarefas/bd_lista_tarefa.sqlite")
      #cursor
       cursor = conexao.cursor()
      #executar
       cursor.execute("""
                    CREATE TABLE IF NOT EXISTS usuario (
                    nome VARCHAR (80),
                    usuario VARCHAR(20) PRIMARY KEY,
                    senha VARCHAR(20)  
                          """)
       #comitar
       conexao.commit()
       #closar
       cursor.close()
       conexao.close()
       
#############################################################################################################
    def inserir_usuario(self):

      try:
        conexao = sqlite3.connect("05_Lista_Tarefas/bd_lista_tarefa.sqlite")
        cursor = conexao.cursor()

        nome = self.entry_nome.get()
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()


        cursor.execute("""
                      INSERT INTO usuario(nome, usuario, senha)
              VALUES(?, ?, ?);
                """, [nome, usuario, senha])
                        
        
        conexao.commit()

        messagebox.showinfo("cadastro","cadastrado com sucesso!")


      except:
        messagebox.showerror("cadastro", "Erro ao cadastrar")

      finally:
        conexao.close()
###########################################################################################################


    


    def run(self):
      self.menu_cadastro.mainloop()

if __name__ == "__main__":
   menu_cadastro = Menu_cadastro("")
   menu_cadastro.run()

        


    