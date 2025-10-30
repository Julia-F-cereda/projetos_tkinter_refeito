import ttkbootstrap as ttk
import tkinter.messagebox
from menu_cadastro import Menu_cadastro
import sqlite3
class Menu_login():
   #o sel.menu_login é o nome da janela
   def __init__(self, classe_pai):

      self.janela_pai = classe_pai.menu_lista
      self.classe_pai = classe_pai

      self.menu_login = ttk.Toplevel(self.janela_pai)
      self.menu_login.geometry("1920x1080")

      #fechar a janela e eencerrar programa
      self.menu_login.protocol("WM_DELETE_WINDOW", self.sair)

      #Label titulo de cima login
      self.Label_titulo = ttk.Label(self.menu_login,
                                    text="Login",
                                    foreground="pink",
                                    font=("Times New Roman",40))
      self.Label_titulo.pack(pady=10)

      #Label para o nome da caixa usuario
      self.label_usuario = ttk.Label(self.menu_login,
                                     text="Usuário",
                                     font=("Times New Roman",15))
      self.label_usuario.pack()

      #Entry caixa para por o login
      self.entry_usuario = ttk.Entry(self.menu_login,
                                   text="Usuário")
      self.entry_usuario.pack(pady=10)

      #label para o nome senha
      self.label_senha = ttk.Label(self.menu_login,
                                   text="Senha",
                                   font=("Times New Roman",15))
      self.label_senha.pack()

      #entry para por a caixa p senha
      self.entry_senha = ttk.Entry(self.menu_login,
                                   text="Senha",
                                   show="*") #para mnao mosrrar a senha
      self.entry_senha.pack()

      #botão para logar
      frame_botao = ttk.Frame(self.menu_login)
      frame_botao.pack()
      ttk.Button(frame_botao, text="LOGAR",width=30, command=self.conferir).pack(side="left", padx=20, pady=(20,0))
      ttk.Button(frame_botao, text="SAIR",width=30, command=self.sair).pack(side="right",padx=20, pady=(20,0))
      ttk.Button(frame_botao, text="CADASTRO",width=30, command=self.chamar_janela).pack(side="right",padx=20, pady=(20,0))
  
#########################################################################3
   def run(self):
      self.menu_login.mainloop()
#############################################################################################################
   #eu chamei o memu login porque é ele que esta com a 
   def chamar_janela(self):
      Menu_cadastro(self.menu_login)
########################################################################
   def sair(self):
      resposta = tkinter.messagebox.askyesno(title="Sair", message="Tem certeza que deseja sair?")
      if resposta == True:
         exit()

 
        
##############################################################################################################
   #conferindo login
   def conferir(self):
      usuario = (self.entry_usuario.get())
      senha = (self.entry_senha.get())
      #fazendo conexao com banco de dados para pegar os cadastros anteriores
      conexao = sqlite3.connect("05_Lista_Tarefas/bd_lista_tarefa.sqlite")
      cursor = conexao.cursor()
      cursor.execute(
         """
            SELECT nome, usuario FROM usuario
            WHERE usuario = ? AND senha = ?;
         """,
         [usuario, senha]
      )
      #o fetchone esta ai pq a gente quer buscar apenas uma coisa, um id unico por exemplo
      resultado = cursor.fetchone()

      conexao.close()

      #se o resultado encontrado nao foi vazio
      if resultado != None:
         tkinter.messagebox.showinfo(title="cadastro",message=f"Bem vindo, {resultado[0]}!!")
         self.menu_login.destroy()
         self.janela_pai.deiconify()
         self.classe_pai.usuario = usuario
         self.classe_pai.atualizar_lista()
         
      else:
         tkinter.messagebox.showerror(title="cadastro",message="Login e senha Incorreto")
############################################################################################################


if __name__ == "__main__":
    # CORREÇÃO CRÍTICA: É OBRIGATÓRIO criar a janela principal (raiz)
    janela_principal = ttk.Window(themename="superhero")
    
    # Passa a janela principal para a classe
    login = Menu_login()
    
    # Executa o loop de eventos
    login.run()



      
      
      
      
      