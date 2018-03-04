# En este archivo se encuentra toda las clases del dominio del
# programa de Entrenamiento Mental
# 
# Desarrollado por: Guis
import random
import os

# Clase que tiene la informacion acerca del juego:
# su nombre, la dificultad y la descripcion
class JuegoInfo():
   def __init__(self, id, nombre, dificultad):
      self.id = id
      self.nombre = nombre
      self.dificultad = dificultad
      self.descripcion = ""
   # Mensaje de bienvenida al juego    
   def opening(self):
      print("Bienvenido a {:s} - Dificultad: {:s}".format(self.nombre, self.dificultad))

# Clase abstracta que representa a un juego que se esta ejecuntando
class Juego():
   def __init__(self, juegoInfo):
      self.juegoInfo = juegoInfo
      self.jugador = None
      self.detallesJuego = []

   # Metodo que contiene toda la logica del juego
   # y que se sobrescribe al implementar un juego 
   # en especifico
   def logicaDeJuego(self):
      raise NotImplementedError("Metodo abstracto")

   # Metodo que se llama para jugar al juego
   def jugar(self):
      # Si no se introducido un jugador el juego no arranca
      if self.jugador != None: 
         # Llama al opening del juego
         self.juegoInfo.opening()
         # Llama a la logica del juego
         # Aqui implementamos el patron Metodo Template
         self.logicaDeJuego()
      else:
         raise Exception("No existe el jugador")

# Juego que te pide sumar dos numero de 6 cifras 
# Hereda de la clase Juego
class OperacionesGrandes(Juego):

   # Constructor
   def __init__(self):
      # Se crea el objeto JuegoInfo con la información del juego
      juegoInfo = JuegoInfo(1,"OperacionesGrandes","Facil")
      # Llama al constructor de la clase Juego
      super(OperacionesGrandes, self).__init__(juegoInfo)

   # Logica del juego
   def logicaDeJuego(self):
      # Respuesta del usuario si desea continuar el juego
      continuar = "s"
      # Acumulador de puntaje
      puntaje = 0
      while continuar == "s":
         # Numero uno para sumar
         num1 = random.randrange(100000, 999999)
         # Numero dos para sumar
         num2 = random.randrange(100000, 999999)
         # Calculo de la respuesta
         rptaCorrecta = num1 + num2
         
         # Muestra al usuario la operación que se desea
         print(num1)
         print("{:d} +".format(num2))
         print("----------")

         # Pide la respuesta al usuario
         rptaUsuario = int(input("Respuesta: "))

         # Compara si las respuestas son iguales
         if rptaCorrecta == rptaUsuario:
            print("Respuesta Correcta, + 2")
            puntaje += 2
         else:
            print("Respuesta Incorrecta -1")
            print("La respuesta correcta era: {:d}".format(rptaCorrecta))
            puntaje -= 1
         
         # Pregunta si desea continuar
         continuar = input("¿Continuar? (s/n): ")
         os.system("cls")

      self.detallesJuego.append(DetalleJuego(self.jugador, self.juegoInfo, puntaje))
      print(DetalleJuego(self.jugador, self.juegoInfo, puntaje))

# Clase jugador, con los datos de quien esta jugando
class Jugador():
   def __init__(self, username):
      self.username = username
      self.nombres = ""
      self.apellidos = ""

# Detalle juego, contiene el juego y el puntaje para ese juego del jugador
class DetalleJuego():
   def __init__(self, jugador, juego, puntaje):
      self.jugador = jugador
      self.juego = juego
      self.puntaje = puntaje

   def __str__(self):
      return "Jugador:{:s}\nPuntaje:{:d}".format(self.jugador.username, self.puntaje)
