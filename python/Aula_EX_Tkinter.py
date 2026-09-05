import tkinter as tk

janela = tk.Tk()
janela.title('Opa bão man')
janela.geometry('400x300')

texto = tk.Label(janela, text='Bem vindo')
texto.pack()

def resposta_botão():
    nome = entrada_texto.get()
    texto['text'] = f'Olá {nome}'

    entrada_texto = tk.Entry(janela)
    entrada_texto.pack()

botão = tk.Button(janela, text='Botão', command=resposta_botão).pack()

janela.mainloop()