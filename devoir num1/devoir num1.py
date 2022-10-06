M=float(input("donner la valeur du masse volumique du mercure : "))
M1=float(input("donner la valeur du masse volumique du platine : "))
M2=float(input("donner la valeur du masse volumique de zinc : "))
min=((M1-M)/(M-M2))
print("la valeur minimalde h1/h2 est :",min,"m")
import numpy as np
coeff=[1,-2.4,-3.62]
sol=np.roots(coeff)
print(sol[0].real)