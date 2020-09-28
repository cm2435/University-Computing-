import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import curve_fit as cf 


dataset = np.genfromtxt("2bv1.txt", skip_header =1, delimiter = ",")

print(dataset)

frequency=(dataset[:,0])

V_out_real=(dataset[:,1])
V_out_imaginary=(dataset[:,2])

def V_out_args (V_out_real ,V_out_imaginary):
    return ((V_out_real**2)+(V_out_imaginary**2))**0.5

V_out_arg = []
for i in range(len(dataset)):
    V_out_arg.append(V_out_args(V_out_real[i], V_out_imaginary[i]))



print (V_out_real)

plt.plot(frequency, V_out_real, "r", label = "Real V out: " )
plt.plot(frequency, V_out_imaginary, "g", label = "Imaginary V out: " )
plt.plot(frequency, V_out_arg, "b", label = "Argument of V out: " )

plt.xscale("log")
plt.xlabel("frequency /Hz")
plt.ylabel("Voltage /v")
plt.title("AC output for V_in and V_out against time")
plt.legend()

