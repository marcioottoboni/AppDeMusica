import Classes as CL
import tkinter as tk

# Função chamada quando o botão "OK" é clicado
def mostrar_informacoes():
    cantores = entry_cantores.get()
    estilos = entry_estilos.get()
    
    if sl_top10.get() == 1:
        teste = CL.Spotify(cantores, estilos).Top_10_Musicas()
    if sl_dico.get() == 1:
        CL.Spotify(cantores, estilos).Todas_Discografia()
    if sl_parecidos.get() == 1:
       var_parecidos =  CL.Spotify(cantores, estilos).Top_20_Parecidos()
       print(var_parecidos)
    if sl_parecidos.get() != 1 and sl_dico.get() != 1 and sl_top10.get() != 1:
       print(f'Selecione alguma opcao!') 
    
# Configuração da janela
root = tk.Tk()
root.title("Download De Musicas")
largura, altura, posicaoX,posicaoY  = 460,160,900,900
root.geometry(f"{largura}x{altura}+{posicaoX}+{posicaoY}")

# Título para Cantores
label_cantores = tk.Label(root, text="  Cantor:")
label_cantores.grid(row=0, column=0, columnspan=2)
entry_cantores = tk.Entry(root)
entry_cantores.grid(row=0, column=2, columnspan=2)

#Linha de Espaco 
label_separador_0 = tk.Label(root, text="")
label_separador_0.grid(row=1, column=0, columnspan=2)

# Título para Estilos
label_estilos = tk.Label(root, text="Estilo:")
label_estilos.grid(row=2, column=0, columnspan=2)
entry_estilos = tk.Entry(root)
entry_estilos.grid(row=2, column=2, columnspan=2)

# Inicia os check button em branco
sl_top10,sl_dico, sl_parecidos = tk.IntVar(),tk.IntVar(),tk.IntVar()

ck_top10 = tk.Checkbutton(root, text="Top 10 músicas", variable=sl_top10)
ck_disco = tk.Checkbutton(root, text="Toda a discografia", variable=sl_dico)
ck_parecidos = tk.Checkbutton(root, text="Top 20 parecidos", variable=sl_parecidos)

ck_top10.grid(row=3, column=0)
ck_disco.grid(row=3, column=1)
ck_parecidos.grid(row=3, column=2)

#Linha de Espaco 
label_separador = tk.Label(root, text="")
label_separador.grid(row=4, column=0, columnspan=2)

# Botão "OK"
botao_ok = tk.Button(root, text="Baixar", command=mostrar_informacoes)
botao_ok.grid(row=5, column=2, columnspan=4)

# Iniciar a interface
root.mainloop()
