from tkinter import *
from tkinter import filedialog
import pygame

# se programen los metodos y botones:
class musica:
    def __init__(self,ventana):
        ventana.geometry("270x270")
        ventana.title("Reproductor")
        ventana.config(bg = "#1E1E1E",relief = RIDGE,bd = "25")
        ventana.resizable(False,False)

        # Establecer el icono de la ventana

        # definiendo los botones:
        abrir = Button(ventana,text = "ABRIR",bg = "blue",width = 10, relief = "groove", bd = 4, command = self.abrir)
        abrir.place(x=60,y=15)
        pausar = Button(ventana,text = "PAUSAR",bg = "blue",width = 10, relief = "groove", bd = 3, command = self.pausar )
        pausar.place(x=60,y=55)
        reanudar = Button(ventana,text = "REANUDAR",bg = "blue",width = 10, relief = "groove", bd = 3, command = self.reanudar )
        reanudar.place(x=60,y=95)
        detener = Button(ventana,text = "DETENER",bg = "blue",width = 10, relief = "groove", bd = 4, command = self.detener )
        detener.place(x=60,y=135)
        reproducir = Button(ventana,text = "REPRODUCIR",bg = "blue",width = 10, relief = "groove", bd = 4, command = self.reproducir )
        reproducir.place(x=60,y=175)

        self.abrir_musica = False
        self.reproducir_musica = True
        self.posicion_pausa = 0

        # inisializando pygame
        pygame.init()

        # definiendo funciones
    def abrir(self):
        self.abrir_musica = filedialog.askopenfilename()
        Sound = pygame.mixer.Sound(self.abrir_musica)
        Sound.play()
        self.reproducir_musica = True

    def pausar(self):
        if self.reproducir_musica:
            pygame.mixer.pause()
            self.reproducir_musica = False
        
    def reanudar(self):
        if self.reproducir_musica == False:
            pygame.mixer.unpause()
            self.reproducir_musica = True

    def detener(self):
        pygame.mixer.stop()

    def reproducir(self):
        if self.abrir_musica:
            Sound = pygame.mixer.Sound(self.abrir_musica)
            Sound.play()
            self.reproducir_musica = True

ventana_principal = Tk()
reproductor = musica(ventana_principal)
ventana_principal.mainloop()

