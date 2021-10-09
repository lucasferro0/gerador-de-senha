from tkinter import *
from tkinter import messagebox
import random
import datetime


def buscar():
    try:
        n = int(entrada.get())
    except:
        status = messagebox.showerror(title="", message="Algo deu errado, tente novamente.")
    else:
        caracteres1 = ['0','1','2','3','4','5','6','7','8','9']
        caracteres2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
        caracteres3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']
        lista1 = []
        cont = 1
        while cont <= n:
            lista1.append(random.choice(caracteres1))
            cont+=1
        cont = 1
        while cont <= n:
            lista1.append(random.choice(caracteres2))
            cont+=1
        cont=1
        while cont <= n:
            lista1.append(random.choice(caracteres3))
            cont+=1
        random.shuffle(lista1)
        senha = []
        cont = 1
        while cont <= n:
            senha.append(random.choice(lista1))
            cont+=1
        senha_final = "".join(senha)
        status = messagebox.showinfo(title="",message=f"Senha gerada: {senha_final}")
        tempo = datetime.date.today()
        tempo = tempo.strftime("%d/%m/%y")
        arquivo = open("password.txt", 'w')
        arquivo.write(f"Senha gerada: {senha_final} [Senha criada em {tempo}]\n")
        arquivo.close()


tela = Tk()
tela.title("Gerador de senha")
tela.geometry("300x200")
tela.configure(background="#318EE0")

topo_estilo = Label(tela, background="black")
topo_estilo.place(x=58,y=7, width=204, height=38)

topo = Label(tela, background="#7FFFC4", text="Gerador de senhas", font="timesnewroman 15 bold")
topo.place(x=60,y=10, width=200, height=32)

quantidade = Label(tela, text="Quantidade de caracteres:", background="#318EE0", font="timesnewroman 10 bold", foreground="black")
quantidade.place(x=3,y=80)

entrada = Entry(tela, font="timesnewroman 10 bold")
entrada.place(x=180,y=83, width=80, height=16)

confirmar = Button(tela, text="Gerar senha", command=buscar ,background="#B9EDCD")
confirmar.place(x=114,y=150)


tela.mainloop()