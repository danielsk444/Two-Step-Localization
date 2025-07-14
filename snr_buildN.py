#https://arxiv.org/pdf/1610.03567
from random import random
import numpy as np
import cmath
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad


#plt.loglog(f1, C)
#plt.show()
MPc2m=3.08567758e22
G = 6.6743e-11
c = 3e8
M_sun = 1.989e30
m1 = 1.4 * M_sun
m2 = 1.4 * M_sun
t_c = 350
i = cmath.sqrt(-1)
M_t = m1 + m2
miu = m1 * m2 / M_t
M_c = (miu ** (3 / 5)) * (M_t ** (2 / 5))
eta = miu / M_t

cos_theta = -1 +2* random()
theta=np.arccos(cos_theta)/2
phi = np.deg2rad(360 * random())
psi = np.deg2rad(360 * random())
cos_I = -1 + 2 * random()
I = np.arccos(cos_I)/2
def find_closest_index(array, x):


    closest_index = 0
    smallest_diff = abs(array[0] - x)

    for i in range(1, len(array)):
        current_diff = abs(array[i] - x)
        if current_diff < smallest_diff:
            smallest_diff = current_diff
            closest_index = i

    return closest_index

def integrand(f,D,A):

    #phi_gw=-(2/5)*((c**3)/(G*M_t))*(Theta**(-3/8))()

    niu=(np.pi*M_t*f*G/c**3)**(1/3)
    #h_p=(4/r)*((G*M_c/c**2)**(5/3))*((np.pi*f/c)**(2/3))*0.5*(1+(np.cos(I))**2)*np.cos(phi_gw)

    Psi_f=2*np.pi*f*t_c-2*psi-np.pi/4+(3/(128*eta))*(niu**(-5)+(3715/756+(55/9)*eta)*niu**(-3)-16*np.pi*niu**(-2)+(15293365/508032+(27145/504)*eta+(3085/72)*eta**2)*niu**(-1))
    h_f=(1/D)*A*f**(-7/6)*np.exp(-i*Psi_f)
    #Theta_t=((c**3)*eta/(5*G*M_t))(t_c-t)
    #f_t=(c**3)/(8*np.pi*G*M_t)*Theta_t**(-3/8)
    #print('D',D)
    return np.real(h_f * np.conj(h_f))


#@profile
def snr_buildN(t_pre_merge,rMPc,run):
    print('snr_buildN')
    F_p=0.5*(1+(np.cos(theta))**2)*np.cos(2*phi)*np.cos(2*psi)-np.cos(theta)*np.sin(2*phi)*np.sin(2*psi)
    F_c=0.5*(1+(np.cos(theta))**2)*np.cos(2*phi)*np.sin(2*psi)+np.cos(theta)*np.sin(2*phi)*np.cos(2*psi)
    #F_c=1/5
    #F_p = 1 / 5
    #I=45
    #print(F_c,F_p)
    r = rMPc * MPc2m

    D = r / np.sqrt((F_p ** 2) * (0.5 * (1 + (np.cos(I)) ** 2)) ** 2 + (F_c ** 2) * (np.cos(I)) ** 2)
    A = -((5 / (24 * np.pi)) ** 0.5) * (G * M_sun / c ** 2) * ((np.pi * G * M_sun / c ** 3) ** (-1 / 6)) * ((M_c / M_sun) ** (-5 / 6))
    eta=miu/M_t
    SNRs=[]
    if run==3:
        df = pd.read_csv('NoiseO3.txt', delimiter=' ')
        df.columns = ['a', 't', 'b']
    if run == 4:
        df = pd.read_csv('NoiseO4.txt', delimiter=' ')
        df.columns = ['a', 'b']

    if run==5:
        df = pd.read_csv('NoiseO5.txt', delimiter=' ')
        df.columns = ['a', 't', 'b']

    f1 = np.asarray((df.loc[349:3001, 'a']))
    C = np.asarray((df.loc[349:3001, 'b']))

    f_0 = 10
    print(f1)
    k_i=find_closest_index(f1, f_0)

    for i in range(len(t_pre_merge)):
        t=t_c-t_pre_merge[i]

        Theta_t=((c**3)*eta/(5*G*M_t))*(t_c-t)
        f_t=(c**3)/(8*np.pi*G*M_t)*np.real(Theta_t)**(-3/8)
        SNR=0
        k_f=0
        for k in range(len(C)):
            if f_0<f1[k]<f_t:
                SNR=SNR+integrand(f1[k],D,A)/(C[k]**2)
                k_f=k
        print('f1',f1)

        print('SNR',SNR,(f_t-f_0)/(k_f-k_i),f_t,f_0,k_f,k_i,t_pre_merge[i])
        SNR=SNR*(f_t-f_0)/(k_f-k_i)
        print('SNR',SNR)
        #plt.plot(2,2)
        #plt.show()
        SNRs.append(SNR)

    return theta,phi,psi,I,SNRs,D

