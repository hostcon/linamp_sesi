import tkinter as tk

janela = tk.Tk()
janela.title("Player")
janela.geometry("300x200")

def play():
    print("Play")

    

btn = tk.Button(janela, text="Play", command=play)
btn.pack()
janela.mainloop()