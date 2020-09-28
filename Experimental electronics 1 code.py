import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import curve_fit as cf 



dataset = np.genfromtxt("ltspice1.txt", skip_header =1, delimiter = "\t")

print(dataset)
time= dataset[:,0]
v_out= dataset[:,1]


def Vexp (x, b):
    return 0.5*np.exp(-b * x) 

popt1, pcov1 = cf(Vexp, time, v_out)

print(popt1)

bVal1= str(round(popt1[0], 3))
eq1= "0.5 * EXP (-" + bVal1 + "x)"






plt.plot(time, v_out, "r", label = "V_out" +eq1)

plt.xlabel("time /t")
plt.ylabel("Voltage /v")
plt.title("TIme against Voltagge at Different Parts of the Current")
plt.legend()
