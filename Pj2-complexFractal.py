# -*- coding: utf-8 -*-
# Fractal functions collection

import matplotlib.pyplot as plt
import numpy as np
import numba

def mandelbrotFra():
   def mandelbrot( h,w, maxit=20 ):
      '''Crea el grafico del fractal de Mandelbrot del tamaño (h,w).'''
      y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
      c = x+y*1j
      z = c
      divtime = maxit + np.zeros(z.shape, dtype=int)
      
      for i in range(maxit):
         z  = z**2 + c
         diverge = z*np.conj(z) > 2**2         
         div_now = diverge & (divtime==maxit)  
         divtime[div_now] = i                  
         z[diverge] = 2                        
         
      return divtime

   plt.figure(figsize=(8,8))
   plt.imshow(mandelbrot(2000,2000))
   plt.show()
def juliaF():
   def py_julia_fractal(z_re, z_im, j):
      '''Crea el grafico del fractal de Julia.'''
      for m in range(len(z_re)):
         for n in range(len(z_im)):
               z = z_re[m] + 1j * z_im[n]
               for t in range(256):
                  z = z ** 2 - 0.05 + 0.68j
                  if np.abs(z) > 2.0:
                     j[m, n] = t
                     break
                     
   jit_julia_fractal = numba.jit(nopython=True)(py_julia_fractal)
   N = 1024
   j = np.zeros((N, N), np.int64)
   z_real = np.linspace(-1.5, 1.5, N)
   z_imag = np.linspace(-1.5, 1.5, N)
   jit_julia_fractal(z_real, z_imag, j)

   fig, ax = plt.subplots(figsize=(8, 8))
   ax.imshow(j, cmap=plt.cm.RdBu_r, extent=[-1.5, 1.5, -1.5, 1.5])
   ax.set_xlabel("$\mathrm{Re}(z)$", fontsize=18)
   ax.set_ylabel("$\mathrm{Im}(z)$", fontsize=18)
   plt.show()

if __name__=="__main__":
   x=input("""- Elige 1 si deseas ver un fractal mandelbrot
- Elige 2 si deseas ver un fractal julia:
""")
   if x=="1":
      mandelbrotFra()
   elif x=="2":
      juliaF()
   else:
      print("Porfavor use una opcion valida")
   