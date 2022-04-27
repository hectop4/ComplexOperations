def operaciones(z1,z2):
   x=input("""Ahora para poder realizar una operacion con los numeros 
usados anteriormente Ingrese el numero respectivo de la operacions
   1- Suma
   2- Resta
   3- Multiplicacion
   4- Division:
""")
   if x=="1":
      print("z1+z2  =  "+str(z1+z2))
   elif x=="2":
      print("z1-z2  =  "+str(z1-z2))
   elif x=="3":
      print("z1*z2  =  "+str(z1*z2))
   elif x=="4":
      if z2==0:
         print("Indeterminado")
      else:
         print("z1/z2=  "+str(z1/z2))
   else:
      print("Por favor ingrese una opcion valida")
      operaciones(z1,z2)

if __name__=="__main__":
   print("""               Recuerde que el formato de numeros complejos es:


                   a+bj      Siendo a,b numeros Reales

   """)
   
   z1=complex(input("Ingrese un numero complejo 1 (cambie la 'i' por una 'j'):"))
   z2=complex(input("Ingrese un numero complejo 2 (cambie la 'i' por una 'j'):"))

   operaciones(z1,z2)
#test
