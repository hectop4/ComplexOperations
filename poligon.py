# import matplotlib.pyplot as plt
# import numpy as np

import cmath

c= complex(input('Ingrese un complejo: Recuerde que de se denotado como a+bj siendo j la unidad imaginaria   '))
raiz_in=int(input('Ingrese el numero de la raiz que quiera que quiere obtener del numero complejo (Entero)   '))

raiz=1/(raiz_in)

magnitud=abs(c)
fase=cmath.phase(c)
r=magnitud**raiz


for i in range(0,raiz_in,1):

   
   real=cmath.cos((fase+2*cmath.pi*i)/raiz_in)
   img=cmath.sin((fase+2*cmath.pi*i)/raiz_in)
   

   resul=complex((r)*(complex(real,img)))

   print(str(resul))

