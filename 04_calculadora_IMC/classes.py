import ttkbootstrap as ttk
import messagebox as tkinter
class Classes():
    def __init__(self):

        self.classes = ttk.Window(themename="solar",
                               title="Calculador de IMC",
                               )
        #self.main.iconbitmap("") pra por icone no titulo
        

        self.classes.geometry("600x800")

        #titulo cima
        self.Label_inicio = ttk.Label(self.classes,
                                      text="Calculadora IMC",
                                      style="danger",
                                      font=("Times-New-Roman",40))
        self.Label_inicio.pack(pady=20)

        #label para escrever o peso
        self.Label_peso = ttk.Label(self.classes,
                                    text="Insira o seu Peso utilizando .",)
        self.Label_peso.pack(pady=20)

        #caixa de texto para o peso
        self.entry_peso = ttk.Entry(self.classes)
        self.entry_peso.pack(pady=5)

        #label para escrever a altura
        self.Label_altura = ttk.Label(self.classes,
                                      text="Insira a sua altura utilizando .",)
        self.Label_altura.pack(pady=20)
        
        #caixa de texto para altura
        self.entry_altura = ttk.Entry(self.classes)
        self.entry_altura.pack(pady=5)

        #Botão para calcular o imc
        self.button_calcular = ttk.Button(self.classes,
                                          text="Calcular IMC",
                                           command=lambda: self.calcular())
                                            #o lambda guarda o resultado e só mostra quando vc apertar o botao
        self.button_calcular.pack()

        self.Label_resultado = ttk.Label(self.classes,
                                         text="resultado:")
        self.Label_resultado.pack()

        self.label_erro = ttk.Label(self.classes,
                                    text="")
        self.label_erro.pack()
      

    def run(self):
        """essa função mantem a janela aberta"""
    #loop pra manter janela aberta
        self.classes.mainloop()

    def calcular(self):
        """essa função calcula o IMC e mostra o resultado"""

        try:
        #o try vai ser executado quando estver tudo certo, e ai se der certo ele pula o except
        #transformando os numeros em int 
            peso = float(self.entry_peso.get())
            altura = float(self.entry_altura.get())

            if peso <= 0 or altura <= 0:
                raise ValueError("coloque valores validos e positivos")
            #raise → cria um erro manualmente para que seja tratado no except.
            #value error= é quando voce escrever um valor que o prohgrama nao conseue realizar o calculo

            #fazendo a divisão

            resultado_div = (peso) / (altura ** 2)

            # classificação
            if resultado_div<18.5:
                classificacao = "Abaixo do peso"

            elif resultado_div<24.9:
                classificacao = "Normoponderal"

            elif resultado_div<29.9:
                classificacao = "Pre-obesidade"
                                                                                                                                                                     
            elif resultado_div<34.9:
                classificacao = "Obesidade grau 1"
                
            elif resultado_div<39.9:
                classificacao = "obesidade grau 2"

            elif resultado_div<40:
                classificacao = "obesidade morbida"


            self.Label_resultado.config(text=f"seu IMC é:{resultado_div:.2f} sua classificação é: {classificacao}")

        except ValueError:
            tkinter.messagebox.showerror
        #se caso o try nao estiver dando certo ele vai imprimir isso
            #elif para assim q acha o res
            self.label_erro.config(text="⚠️ Digite números válidos e positivos, use '.' e não letras.")
        





