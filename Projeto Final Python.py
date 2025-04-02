
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Criar banco de dados e tabela de clientes
def criar_banco():
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            endereco TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar cliente
def adicionar_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()

    if nome and email and telefone and endereco:
        conn = sqlite3.connect('clientes.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO clientes (nome, email, telefone, endereco)
            VALUES (?, ?, ?, ?)
        ''', (nome, email, telefone, endereco))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        limpar_campos()
    else:
        messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")

# Função para consultar cliente
def consultar_cliente():
    nome = entry_nome.get()

    if nome:
        conn = sqlite3.connect('clientes.db')
        c = conn.cursor()
        c.execute('SELECT * FROM clientes WHERE nome LIKE ?', ('%' + nome + '%',))
        clientes = c.fetchall()
        conn.close()

        if clientes:
            lista_clientes.delete(0, tk.END)
            for cliente in clientes:
                lista_clientes.insert(tk.END, f"ID: {cliente[0]} - Nome: {cliente[1]} - Email: {cliente[2]} - Telefone: {cliente[3]} - Endereço: {cliente[4]}")
        else:
            messagebox.showinfo("Resultado", "Nenhum cliente encontrado.")
    else:
        messagebox.showwarning("Erro", "Digite o nome do cliente para consultar.")

# Função para editar dados de um cliente
def editar_cliente():
    try:
        cliente_selecionado = lista_clientes.get(lista_clientes.curselection())
        cliente_id = cliente_selecionado.split(" - ")[0].split(":")[1].strip()

        novo_nome = entry_nome.get()
        novo_email = entry_email.get()
        novo_telefone = entry_telefone.get()
        novo_endereco = entry_endereco.get()

        if novo_nome and novo_email and novo_telefone and novo_endereco:
            conn = sqlite3.connect('clientes.db')
            c = conn.cursor()
            c.execute('''
                UPDATE clientes SET nome = ?, email = ?, telefone = ?, endereco = ?
                WHERE id = ?
            ''', (novo_nome, novo_email, novo_telefone, novo_endereco, cliente_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
            limpar_campos()
        else:
            messagebox.showwarning("Erro", "Todos os campos devem ser preenchidos!")

    except IndexError:
        messagebox.showwarning("Erro", "Selecione um cliente para editar.")

# Função para excluir dados de um cliente
def excluir_cliente():
    try:
        cliente_selecionado = lista_clientes.get(lista_clientes.curselection())
        cliente_id = cliente_selecionado.split(" - ")[0].split(":")[1].strip()

        conn = sqlite3.connect('clientes.db')
        c = conn.cursor()
        c.execute('DELETE FROM clientes WHERE id = ?', (cliente_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
        listar_clientes()
    except IndexError:
        messagebox.showwarning("Erro", "Selecione um cliente para excluir.")

# Função para listar clientes
def listar_clientes():
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM clientes')
    clientes = c.fetchall()
    conn.close()

    lista_clientes.delete(0, tk.END)
    for cliente in clientes:
        lista_clientes.insert(tk.END, f"ID: {cliente[0]} - Nome: {cliente[1]} - Email: {cliente[2]} - Telefone: {cliente[3]} - Endereço: {cliente[4]}")

# Função para limpar campos
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)

# Criar janela principal
root = tk.Tk()
root.title("Cadastro de Clientes - XYZ Comércio")

# Layout dos campos de entrada
label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

label_email = tk.Label(root, text="E-mail:")
label_email.grid(row=1, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

label_telefone = tk.Label(root, text="Telefone:")
label_telefone.grid(row=2, column=0)
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=2, column=1)

label_endereco = tk.Label(root, text="Endereço:")
label_endereco.grid(row=3, column=0)
entry_endereco = tk.Entry(root)
entry_endereco.grid(row=3, column=1)

# Botões de ação
button_adicionar = tk.Button(root, text="Cadastrar Cliente", command=adicionar_cliente)
button_adicionar.grid(row=4, column=0, columnspan=2)

button_consultar = tk.Button(root, text="Consultar Cliente", command=consultar_cliente)
button_consultar.grid(row=5, column=0, columnspan=2)

button_editar = tk.Button(root, text="Editar Cliente", command=editar_cliente)
button_editar.grid(row=6, column=0, columnspan=2)

button_excluir = tk.Button(root, text="Excluir Cliente", command=excluir_cliente)
button_excluir.grid(row=7, column=0, columnspan=2)

button_listar = tk.Button(root, text="Listar Clientes", command=listar_clientes)
button_listar.grid(row=8, column=0, columnspan=2)

# Lista de clientes
lista_clientes = tk.Listbox(root, width=80, height=10)
lista_clientes.grid(row=9, column=0, columnspan=2)

# Inicializar o banco de dados
criar_banco()

# Rodar o aplicativo
root.mainloop()
