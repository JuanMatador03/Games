# Juego del ahorcado
#@JuanJaraba
"""
1. Elegir aleatoriamente una palabra de una lista de palabras.
2. Mostrar el dibujo de una horca.
3. Mostrar un guion bajo por cada letra de la palabra.
4. Pedir al usuario que introduzca una letra: Si no es una única letra indicarlo. Si ya se ha dicho tambien indicarlo.
5. Comprobar si esa letra está contenida en la palabra elegida.
6. Si está: Volver a mostrar el dibujo de la horca como la ultima vez.
Sustituir el guipin correspondiente por la letra dicha.
7. Si la palabra no está: Vamos a mostrar el dibujo de la horca al que se añade una parte
8. Si se falla 6 veces entonces se completa el dibujo del ahorcado.
9. Si se acierta todas las letras de la palabra: Gano!
"""

import random
import os

palabras = ["CHECHIK", "SOPHIE","GIANNA", "ANGELA", "ABELLA", "MIA", "KHALIFA","RHOADES", "JORDI", "LANA", "RILEY"]

palabra = random.choice(palabras)

fallo0 = """
          !===N
              N
              N
              N
              N
      ========= 
"""
fallo1 = """
          !===N
          O   N
              N
              N
              N
      ========= 
"""
fallo2 = """
          !===N
         _O   N
              N
              N
              N
      ========= 
"""
fallo3 = """
          !===N
         _O_  N
              N
              N
              N
      ========= 
"""
fallo4 = """
          !===N
         _O_  N
          |   N
              N
              N
      ========= 
"""
fallo5 = """
          !===N
         _O_  N
          |   N
          03  N
           \  N
      ========= 
"""
fallo6 = """
          !===N
         _O_  N
          |   N
          03  N
         / \  N
      ========= 
"""
letras_correctas = "" #Letras correctas dichas por el usuario
letras_todas = "" #Todas las letras dichas por el usuario
fallos = 0

while True:
  os.system("cls")
  print("*******************************")
  print("*******************************")
  print("***ADIVINA A TU HUB FAVORITA***")
  print("*******************************")
  print("*******************************")
  if fallos == 0:
    print(fallo0)
  elif fallos == 1:
    print(fallo1)
  elif fallos == 2:
    print (fallo2)
  elif fallos == 3:
    print (fallo3)
  elif fallos == 4:
    print (fallo4)
  elif fallos == 5:
    print (fallo5)
  elif fallos == 6:
    print (fallo6)

  print()
  
  # Mostramos las letras acertadas y guiones bajos en las no acertadas

  resultado =""

  for letra in palabra:
    if letra in letras_correctas:
      resultado += letra
    else:
      resultado +="_"
  print("      {}".format(resultado))
  print()
  print()

    #Comprobamos si se ha acertado la palabra o se han     terminado los intentos.

  if resultado==palabra:
     print("+++Has ganado+++")
     break
  if fallos>5:
     print("La palabra es:", palabra)
     print("***Has perdido***")
     break

    #Bucle para que el usuario teclee una letra que cumpla los requisitos. Comprobamos si la letra dicha por el usuario está en letra
    
  while True:
    letra_usuario_sin_formato = input("Dime una letra:")
    letra_usuario= letra_usuario_sin_formato.upper()
    if len(letra_usuario) < 1 or len(letra_usuario)>1:
      print("introduce una letra")
    elif letra_usuario in letras_todas:
      print("Esa letra ya la has dicho")
    elif not letra_usuario.isalpha():
      print("introduce una letra")
    else:
      letras_todas += letra_usuario
      break
      
  #Comprobamos si la letra dicha por el usuario está en letra
  if letra_usuario not in palabra:
      fallos+=1
  else:
      letras_correctas += letra_usuario
      



      
  
  

