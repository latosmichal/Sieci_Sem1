import numpy as np

class Hopfield:


    def __init__(self, w, x0):
        self.w = w
        self.x = []
        self.x.append(x0)


    def activation(self,val):
        return 1 if val > 0 else -1

    
    def step_async(self):
        for i in range(12):
            val = np.dot(self.w[i%3],np.array(self.x[-1]))
            new_x = self.x[-1].copy()            
            new_x[i%3] = self.activation(val)
            self.x.append(new_x)             


    def print_steps(self):
        self.step_async()
        print('Asynchroniczne')
        print(self.x[0])
        step = 0
        for i in range(1,len(self.x)):            
            if i % 3 == 1:
                step += 1
                print(f'---KROK {step} ---')
            print(self.x[i])

    def step_sync(self):
        print('Synchroniczne')
        for i in range(12):
            val = np.dot(w, np.array(self.x[-1].copy()))
            val[0] = self.activation(val[0])
            val[1] = self.activation(val[1])
            val[2] = self.activation(val[2])     
            if (val == self.x[-1]).all():
                break       
            self.x.append(val)
            

    def print_sync(self):
        self.step_sync()
        for i in self.x:
            print(i)

           
   

w = np.array([[0, -2/3, 2/3], [-2/3, 0, -2/3], [2/3, -2/3, 0]])
x = [1, 1, 1]


hop = Hopfield(w,x)
hop.print_steps()

print()

hop2 = Hopfield(w,x)
hop2.print_sync()
# print(hop2.x)