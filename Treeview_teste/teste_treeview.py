import ttkbootstrap as ttk

def apagar_item():
    item_selecionado = treeview.selection()
    treeview.delete(item_selecionado)

janela = ttk.Window(themename="vapor")

treeview = ttk.Treeview(janela)
treeview.pack()

#se voce precisae que a coluna seja maior, vai mudar atraves do nome dado a coluna
treeview["columns"] = ("nome", "idade", "cidade")

treeview["show"] = "headings"
treeview.heading("nome", text="Nome completo")
treeview.heading("idade", text="Idade")
treeview.heading("cidade", text="Cidade")

treeview.insert("","end", values=["godofredo", "3", "matao"])

ttk.Button(janela, text= "DELETAR", command=apagar_item).pack()




treeview.column("idade",width=200, anchor="center")
treeview.insert("","end", values=["Godofredo", "3", "matao"])
janela.mainloop()
