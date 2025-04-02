import tkinter as tk

janela = tk.Tk()
janela.title('teste tkinter')

texte_label = tk.Label(janela,text = 'ISSO É UM TEXTO')
texte_label.pack()

janela.geometry("500x500")

entry1 = tk.Entry(janela)
entry1.pack()

btn = tk.Button(janela, text = 'CLIQUE AQUI')
btn.pack()

janela.mainloop()*
