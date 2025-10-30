import ttkbootstrap as ttk

janela = ttk.Window(themename="vapor")

treeview = ttk.Treeview(janela)
treeview.pack()

#se voce precisae que a coluna seja maior, vai mudar atraves do nome dado a coluna
treeview["columns"] = ("nome", "idade", "cidade")

treeview.heading("nome", text="Nome completo")
treeview.heading("", text="Nome completo")





janela.mainloop()
