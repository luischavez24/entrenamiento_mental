from model.domainEntities import *
import os

# Metodo que devuelve el puntaje para que se 
# pueda ordenar la lista por puntaje
def sorterDetalles(detalleJuego):
   return detalleJuego.puntaje

# Main
def main():

   # Comienza el juego
   os.system("cls")
   continuar = "n"
   # Crea el juego
   juego = OperacionesGrandes()

   # Bucle para jugar
   while continuar == "n":
      # Recibe el nombre del jugador
      nombreJugador = input("Nombre de usuario: ")
      # Crea al jugador
      jugador = Jugador(nombreJugador)
      # Establece el jugador para el juego
      juego.jugador = jugador
      # Comienza el juego
      juego.jugar()
      continuar = input("¿Desea salir del programa? (s/n): ")
      os.system("cls")

   # Muestra las puntuaciones más altas
   print("Puntuaciones más altas:")

   detJuegoOrd = sorted(juego.detallesJuego, key = sorterDetalles, reverse=True)

   for detalleJuego in detJuegoOrd:
      print(detalleJuego)

# Ejecuta el programa prinicipal
main()
