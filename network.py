import numpy as np
from math import *

class Neural:
    

    def __init__(self, x, w2, w3, x_g):
        self.x = x
        self.w = np.array(w2 + [w3])   
        self.x_good = x_g
        self.delta_w = np.array([[0,0,0],[0,0,0],[0,0,0]],float)
        self.table_z = [0,0,0]
        self.table_fi = [0,0,0]
        self.table_d_fi = [0,0,0]

    def fi(self, t):
        return 1/(1+e**(-t))
    def d_fi(self,t):
        return self.fi(t)*(1-self.fi(t))
    # def calc_dist(self, x):
    #     return 1 if x[1] != x[2] else 0
    def calc_dist(self, x):
        item = self.x.index(x)
        return self.x_good[item]


    def calc_tables(self, x):
        iter = 0
        for i in range(3):
            if i == 2:                
                self.table_z[i] = np.dot(np.array([1,self.table_fi[0], 
                self.table_fi[1]]),self.w[iter])
                self.table_fi[i] = self.fi(self.table_z[i])
                self.table_d_fi[i] = self.d_fi(self.table_z[i])
                break
            self.table_z[i] = np.dot(np.array(x),self.w[iter])
            self.table_fi[i] = self.fi(self.table_z[i])
            self.table_d_fi[i] = self.d_fi(self.table_z[i])
            iter += 1 
        self.const_dist = self.table_fi[2] - self.calc_dist(x)     
    
    def calc_delta_table_2nd_layer(self):        
        x = [1, self.table_fi[0], self.table_fi[1]]
        self.first = self.const_dist * self.table_d_fi[2]
        for item in range(3):
            y = self.first * x[item]            
            self.delta_w[2][item] = y
    def calc_delta_table_1st_layer(self, counter):
        self.calc_delta_table_2nd_layer()
        for neuron in range(2):
            second = self.w[2][neuron+1] * self.table_d_fi[neuron]
            for iter in range(3):
                y = self.first * second * self.x[counter][iter]
                self.delta_w[neuron][iter] = y
    def make_algo(self,n):
        for j in range(2000):
            for i in range(len(self.x)):
                self.calc_tables(self.x[i])
                self.calc_delta_table_1st_layer(i)            
                self.w += self.delta_w*(-n)
                print(f'Wektor: {self.x[i]}, wartośc końcowa: {round(self.table_fi[2],4)}')
        



w2 = [[.86,-.16,.28],
      [.83, -.51, -.86]]
w3 = [.04, -.43, .48]

x = [[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
y= [[1,0,1], [1,1,0],[1,0,0],[1,1,1]]
z = [[1,0,0],[1,1,1],[1,0,1],[1,1,0]]
x_g = [0,1,1,0]
n = 0.5
neural = Neural(x, w2, w3, x_g)
print('Macierz wag początkowa:')
print(neural.w)
print('Macierz wag końcowa:')
print(neural.w)
neural.make_algo(n)

print(neural.table_d_fi)
print(neural.table_fi)
print(neural.table_z)

# neural.calc_tables([0,1,1])
# print(neural.tab)


