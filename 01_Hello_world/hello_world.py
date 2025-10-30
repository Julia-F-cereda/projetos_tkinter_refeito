import tkinter as tk

#criando janela
janela = tk.Tk()

#definindo titulo
janela.title("Hello World")

#pintar a tela
janela.configure(bg="pink")

#colocar icone
janela.iconbitmap("01_Hello_world")

#tamanho
janela.geometry("800x400+100+200")

#aumente ou diminue minha janela
janela.resizable(False,False)

#criando bem vindo, são teextos
label_titulo = tk.Label(janela,
                        text="Bem vindo!",
                        bg="purple",
                        font="arial",
                        foreground="pink")
label_titulo.pack()

#criando texto diga seu nome
label_text = tk.Label(janela, 
                      text="Digite seu nome:")
label_text.pack()

#caixa de texto
entry_nome = tk.Entry(janela)
entry_nome.pack()


#diga bom dia ao pressionar o botao
def button_bomdia():
    """essa função pega o nome que esta digitado na caixa de texto e deseja bom dia"""
    nome = entry_nome.get()
    label_result.configure(text=f"Bom dia, {nome}")

#botao pro bom dia
button_bomdia = tk.Button(janela,
                          text="deseje bom dia",
                          command=button_bomdia)
button_bomdia.pack()

label_result = tk.Label(janela,
                        text="")
label_result.pack()




#loop pra manter janela aberta
janela.mainloop()


