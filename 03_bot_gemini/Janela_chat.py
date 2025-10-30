import ttkbootstrap as ttk
from classe_bot_gemini import Boot_gemini
class Janela_chat():
    def __init__(self):

        #criação de janela, ttk pq é o apelido do ttkbootstrap
        self.janela = ttk.Window( themename= "solar",
                                title="Ms. Sokie",
                                  )
        self.janela.iconbitmap("03_bot_gemini/coracao.ico")
        self.janela.geometry("800x600")

        #titulo
        self.label_titulo = ttk.Label(self.janela,
                                text="Bem vindo ao Mr. sokie",
                                foreground="#ca2a82",
                                style="danger",
                                font=('Times-New-Roman',20))
                                
                                
        self.label_titulo.pack(pady=20)

        #faça sua pergunta
        self.label_titulo2 = ttk.Label(self.janela,
                                       text="Insira a sua pergunta na caixa abaixo",
                                        foreground="#e28ecc",
                                       font=('Times-New-Roman',20))
                                  
        self.label_titulo2.pack(pady=20)

        #caixa de texto
        self.fazer_pergunta = ttk.Entry(self.janela)
        self.fazer_pergunta.pack(pady=20)


        #diga bom dia ao pressionar o botao

        #botao p responder a pergunta
        self.button_perguntar = ttk.Button(self.janela,
                                text="Perguntar",
                                command= self.responder)
        
        self.button_perguntar.pack(pady=20)

        self.Label_reposta = ttk.Label(self.janela,
                                       text=" ",
                                       )
        self.Label_reposta.pack(pady=20)


        #criando robo q da resposta
        self.robo =  Boot_gemini()

    def responder(self):
        pergunta = self.fazer_pergunta.get()
        resposta = self.robo.responder(pergunta)
        self.Label_reposta.configure(text= f" {resposta}")

        self.st.delete("1.0", ttk.END)
        self.st.insert("1.0",resposta)
        
        #self.label_result.configure(text=f"Bom dia, {nome}")

        

    



    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    chat = Janela_chat()
    chat.janela.mainloop() 
          