from uteis.comandos_botao import *
from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle

root = Tk()

style_alt = ThemedStyle(root)
style_alt.set_theme('breeze')

botao = ttk.Button(root, text="Armênio", command=bt_armeno)
botao.grid(row=0, column=0)

botao = ttk.Button(root, text="Árabe", command=bt_arabe)
botao.grid(row=0, column=1)

botao = ttk.Button(root, text="Búlgaro", command=bt_bulgado)
botao.grid(row=0, column=2)

botao = ttk.Button(root, text="Mandarim", command=bt_mandarim)
botao.grid(row=0, column=3)

botao = ttk.Button(root, text="Taiwanês", command=bt_taiwanes)
botao.grid(row=0, column=4)

botao = ttk.Button(root, text="Croata", command=bt_croata)
botao.grid(row=0, column=5)

botao = ttk.Button(root, text="Tcheco", command=bt_tcheco)
botao.grid(row=0, column=6)

botao = ttk.Button(root, text="Dinamarquês", command=bt_dinamarques)
botao.grid(row=0, column=7)

botao = ttk.Button(root, text="Holandês", command=bt_holandes)
botao.grid(row=0, column=8)

botao = ttk.Button(root, text="Inglês", command=bt_ingles)
botao.grid(row=0, column=9)

botao = ttk.Button(root, text="Estoniano", command=bt_estoniano)
botao.grid(row=1, column=0)

botao = ttk.Button(root, text="Filipino", command=bt_filipino)
botao.grid(row=1, column=1)

botao = ttk.Button(root, text="Finlandês", command=bt_finlandes)
botao.grid(row=1, column=2)

botao = ttk.Button(root, text="Francês", command=bt_frances)
botao.grid(row=1, column=3)

botao = ttk.Button(root, text="Georgiano", command=bt_georgiano)
botao.grid(row=1, column=4)

botao = ttk.Button(root, text="Alemão", command=bt_alemao)
botao.grid(row=1, column=5)

botao = ttk.Button(root, text="Grego", command=bt_grego)
botao.grid(row=1, column=6)

botao = ttk.Button(root, text="Hebraico", command=bt_hebraico)
botao.grid(row=1, column=7)

botao = ttk.Button(root, text="Hindi", command=bt_hindi)
botao.grid(row=1, column=8)

botao = ttk.Button(root, text="Húngaro", command=bt_hungaro)
botao.grid(row=1, column=9)

botao = ttk.Button(root, text="Indonesiano", command=bt_indonesiano)
botao.grid(row=2, column=0)

botao = ttk.Button(root, text="Italiano", command=bt_italiano)
botao.grid(row=2, column=1)

botao = ttk.Button(root, text="Letoniano", command=bt_letoniano)
botao.grid(row=2, column=2)

botao = ttk.Button(root, text="Lituano", command=bt_lituano)
botao.grid(row=2, column=3)

botao = ttk.Button(root, text="Macedônio", command=bt_macedonio)
botao.grid(row=2, column=4)

botao = ttk.Button(root, text="Malaio", command=bt_malaio)
botao.grid(row=2, column=5)

botao = ttk.Button(root, text="Norueguês", command=bt_noruegues)
botao.grid(row=2, column=6)

botao = ttk.Button(root, text="Polonês", command=bt_polones)
botao.grid(row=2, column=7)

botao = ttk.Button(root, text="Português", command=bt_portugues)
botao.grid(row=2, column=8)

botao = ttk.Button(root, text="Romeno", command=bt_romeno)
botao.grid(row=2, column=9)

botao = ttk.Button(root, text="Russo", command=bt_russo)
botao.grid(row=3, column=0)

botao = ttk.Button(root, text="Sérvio", command=bt_servio)
botao.grid(row=3, column=1)

botao = ttk.Button(root, text="Eslovaco", command=bt_eslovaco)
botao.grid(row=3, column=2)

botao = ttk.Button(root, text="Esloveniano", command=bt_esloveniano)
botao.grid(row=3, column=3)

botao = ttk.Button(root, text="Espanhol", command=bt_espanhol)
botao.grid(row=3, column=4)

botao = ttk.Button(root, text="Sueco", command=bt_sueco)
botao.grid(row=3, column=5)

botao = ttk.Button(root, text="Tailandês", command=bt_tailandes)
botao.grid(row=3, column=6)

botao = ttk.Button(root, text="Turco", command=bt_turco)
botao.grid(row=3, column=7)

botao = ttk.Button(root, text="Ucraniano", command=bt_ucraniano)
botao.grid(row=3, column=8)

botao = ttk.Button(root, text="Vietnamita", command=bt_vietnamita)
botao.grid(row=3, column=9)

root.mainloop()
