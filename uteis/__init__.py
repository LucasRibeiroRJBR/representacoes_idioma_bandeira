from tkinter import *

from uteis.textos import *


class JanelaIdioma():
    def __init__(self, idioma, texto, bandeira):
        self.idioma = idioma
        self.texto = texto
        self.bandeira = bandeira

    def criar_janela(self):
        if self.idioma == "Armênio":
            self.texto = armeno

            root_armeno = Toplevel()

            bandeira = Label(root_armeno, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_armeno = Label(root_armeno, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_armeno.grid(row=1, column=0)

        if self.idioma == "Árabe":
            self.texto = arabe

            root_arabe = Toplevel()

            bandeira = Label(root_arabe, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_arabe = Label(root_arabe, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_arabe.grid(row=1, column=0)

        if self.idioma == "Búlgaro":
            self.texto = bulgado

            root_bulgado = Toplevel()

            bandeira = Label(root_bulgado, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_bulgado = Label(root_bulgado, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_bulgado.grid(row=1, column=0)

        if self.idioma == "Mandarim":
            self.texto = mandarim

            root_mandarim = Toplevel()

            bandeira = Label(root_mandarim, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_mandarim = Label(root_mandarim, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_mandarim.grid(row=1, column=0)

        if self.idioma == "Taiwanês":
            self.texto = taiwanes

            root_taiwanes = Toplevel()

            bandeira = Label(root_taiwanes, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_taiwanes = Label(root_taiwanes, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_taiwanes.grid(row=1, column=0)

        if self.idioma == "Croata":
            self.texto = croata

            root_croata = Toplevel()

            bandeira = Label(root_croata, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_croata = Label(root_croata, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_croata.grid(row=1, column=0)

        if self.idioma == "Tcheco":
            self.texto = tcheco

            root_tcheco = Toplevel()

            bandeira = Label(root_tcheco, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_tcheco = Label(root_tcheco, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_tcheco.grid(row=1, column=0)

        if self.idioma == "Dinamarquês":
            self.texto = dinamarques

            root_dinamarques = Toplevel()

            bandeira = Label(root_dinamarques, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_dinamarques = Label(root_dinamarques, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_dinamarques.grid(row=1, column=0)

        if self.idioma == "Holandês":
            self.texto = holandes

            root_holandes = Toplevel()

            bandeira = Label(root_holandes, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_holandes = Label(root_holandes, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_holandes.grid(row=1, column=0)

        if self.idioma == "Inglês":
            self.texto = ingles

            root_ingles = Toplevel()

            bandeira = Label(root_ingles, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_ingles = Label(root_ingles, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_ingles.grid(row=1, column=0)

        if self.idioma == "Estoniano":
            self.texto = estoniano

            root_estoniano = Toplevel()

            bandeira = Label(root_estoniano, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_estoniano = Label(root_estoniano, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_estoniano.grid(row=1, column=0)

        if self.idioma == "Filipino":
            self.texto = filipino

            root_filipino = Toplevel()

            bandeira = Label(root_filipino, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_filipino = Label(root_filipino, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_filipino.grid(row=1, column=0)

        if self.idioma == "Finlandês":
            self.texto = finlandes

            root_finlandes = Toplevel()

            bandeira = Label(root_finlandes, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_finlandes = Label(root_finlandes, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_finlandes.grid(row=1, column=0)

        if self.idioma == "Francês":
            self.texto = frances

            root_frances = Toplevel()

            bandeira = Label(root_frances, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_frances = Label(root_frances, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_frances.grid(row=1, column=0)

        if self.idioma == "Georgiano":
            self.texto = georgiano

            root_georgiano = Toplevel()

            bandeira = Label(root_georgiano, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_georgiano = Label(root_georgiano, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_georgiano.grid(row=1, column=0)

        if self.idioma == "Alemão":
            self.texto = alemao

            root_alemao = Toplevel()

            bandeira = Label(root_alemao, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_alemao = Label(root_alemao, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_alemao.grid(row=1, column=0)

        if self.idioma == "Grego":
            self.texto = grego

            root_grego = Toplevel()

            bandeira = Label(root_grego, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_grego = Label(root_grego, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_grego.grid(row=1, column=0)

        if self.idioma == "Hebraico":
            self.texto = hebraico

            root_hebraico = Toplevel()

            bandeira = Label(root_hebraico, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_hebraico = Label(root_hebraico, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_hebraico.grid(row=1, column=0)

        if self.idioma == "Hindi":
            self.texto = hindi

            root_hindi = Toplevel()

            bandeira = Label(root_hindi, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_hindi = Label(root_hindi, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_hindi.grid(row=1, column=0)

        if self.idioma == "Húngaro":
            self.texto = hungaro

            root_hungaro = Toplevel()

            bandeira = Label(root_hungaro, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_hungaro = Label(root_hungaro, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_hungaro.grid(row=1, column=0)

        if self.idioma == "Indonesiano":
            self.texto = indonesiano

            root_indonesiano = Toplevel()

            bandeira = Label(root_indonesiano, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_indonesiano = Label(root_indonesiano, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_indonesiano.grid(row=1, column=0)

        if self.idioma == "italiano":
            self.texto = italiano

            root_italiano = Toplevel()

            bandeira = Label(root_italiano, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_italiano = Label(root_italiano, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_italiano.grid(row=1, column=0)

        if self.idioma == "Letoniano":
            self.texto = letoniano

            root_letoniano = Toplevel()

            bandeira = Label(root_letoniano, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_letoniano = Label(root_letoniano, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_letoniano.grid(row=1, column=0)

        if self.idioma == "Lituano":
            self.texto = lituano

            root_lituano = Toplevel()

            bandeira = Label(root_lituano, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_lituano = Label(root_lituano, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_lituano.grid(row=1, column=0)

        if self.idioma == "Macedônio":
            self.texto = macedonio

            root_macedonio = Toplevel()

            bandeira = Label(root_macedonio, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_macedonio = Label(root_macedonio, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_macedonio.grid(row=1, column=0)

        if self.idioma == "Malaio":
            self.texto = malaio

            root_malaio = Toplevel()

            bandeira = Label(root_malaio, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_malaio = Label(root_malaio, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_malaio.grid(row=1, column=0)

        if self.idioma == "Norueguês":
            self.texto = noruegues

            root_noruegues = Toplevel()

            bandeira = Label(root_noruegues, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_noruegues = Label(root_noruegues, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_noruegues.grid(row=1, column=0)

        if self.idioma == "Polonês":
            self.texto = polones

            root_polones = Toplevel()

            bandeira = Label(root_polones, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_polones = Label(root_polones, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_polones.grid(row=1, column=0)

        if self.idioma == "Português":
            self.texto = portugues

            root_portugues = Toplevel()

            bandeira = Label(root_portugues, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_portugues = Label(root_portugues, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_portugues.grid(row=1, column=0)

        if self.idioma == "Romeno":
            self.texto = romeno

            root_romeno = Toplevel()

            bandeira = Label(root_romeno, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_romeno = Label(root_romeno, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_romeno.grid(row=1, column=0)

        if self.idioma == "Russo":
            self.texto = russo

            root_russo = Toplevel()

            bandeira = Label(root_russo, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_russo = Label(root_russo, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_russo.grid(row=1, column=0)

        if self.idioma == "Sérvio":
            self.texto = servio

            root_servio = Toplevel()

            bandeira = Label(root_servio, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_servio = Label(root_servio, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_servio.grid(row=1, column=0)

        if self.idioma == "Eslovaco":
            self.texto = eslovaco

            root_eslovaco = Toplevel()

            bandeira = Label(root_eslovaco, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_eslovaco = Label(root_eslovaco, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_eslovaco.grid(row=1, column=0)

        if self.idioma == "Esloveniano":
            self.texto = esloveniano

            root_esloveniano = Toplevel()

            bandeira = Label(root_esloveniano, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_esloveniano = Label(root_esloveniano, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_esloveniano.grid(row=1, column=0)

        if self.idioma == "Espanhol":
            self.texto = espanhol

            root_espanhol = Toplevel()

            bandeira = Label(root_espanhol, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_espanhol = Label(root_espanhol, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_espanhol.grid(row=1, column=0)

        if self.idioma == "Sueco":
            self.texto = sueco

            root_sueco = Toplevel()

            bandeira = Label(root_sueco, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_sueco = Label(root_sueco, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_sueco.grid(row=1, column=0)

        if self.idioma == "Tailandês":
            self.texto = tailandes

            root_tailandes = Toplevel()

            bandeira = Label(root_tailandes, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_tailandes = Label(root_tailandes, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_tailandes.grid(row=1, column=0)

        if self.idioma == "Turco":
            self.texto = turco

            root_turco = Toplevel()

            bandeira = Label(root_turco, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_turco = Label(root_turco, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_turco.grid(row=1, column=0)

        if self.idioma == "Ucraniano":
            self.texto = ucraniano

            root_ucraniano = Toplevel()

            bandeira = Label(root_ucraniano, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_ucraniano = Label(root_ucraniano, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_ucraniano.grid(row=1, column=0)

        if self.idioma == "Vietnamita":
            self.texto = vietnamita

            root_vietnamita = Toplevel()

            bandeira = Label(root_vietnamita, image=self.bandeira)
            bandeira.grid(row=0, column=0)

            letreiro_vietnamita = Label(root_vietnamita, text=self.texto, font=("Arial", 36, "bold"))
            letreiro_vietnamita.grid(row=1, column=0)

