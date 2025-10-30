import ttkbootstrap as tk

class Janela_principal:
    """classe para a criação da janela principal"""

    def __init__(self):
        
#criando janela
        self.janela = tk.Window(themename="superhero")

        #definindo titulo
        self.janela.title("Hello World")
        

        #colocar icone
        self.janela.iconbitmap("01_Hello_world/snowflake.ico")

        #tamanho
        self.janela.geometry("800x400+100+200")

        #aumente ou diminue minha janela
        self.janela.resizable(False,False)

        #criando bem vindo, são teextos
        self.label_titulo = tk.Label(self.janela,
                                text="Bem vindo!",
                                background="purple",
                                font="arial",
                                foreground="pink")
        self.label_titulo.pack()

        #criando texto diga seu nome
        self.label_text = tk.Label(self.janela, 
                            text="Digite seu nome:")
        self.label_text.pack()

        #caixa de texto
        self.entry_nome = tk.Entry(self.janela)
        self.entry_nome.pack()


        #diga bom dia ao pressionar o botao

        #botao pro bom dia
        self.button_bomdia = tk.Button(self.janela,
                                text="deseje bom dia",
                                command= self.mostrar)
        self.button_bomdia.pack()

        self.label_result = tk.Label(self.janela,
                                text="")
        self.label_result.pack()



    def run(self):
    #loop pra manter janela aberta
        self.janela.mainloop()


    def mostrar(self):
            """essa função pega o nome que esta digitado na caixa de texto e deseja bom dia"""
            nome = self.entry_nome.get()
            self.label_result.configure(text=f"Bom dia, {nome}")
