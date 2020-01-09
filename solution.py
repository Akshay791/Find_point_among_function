Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
from scipy import optimize,stats
def main3(x,y):
    ''' A is used to store 99 values of a from solving 99 pair of linear eqs'''
    A = np.zeros(0) 
    ''' B is used to store 99 values of b from solving 99 pair of linear eqs'''
    B = np.zeros(0) 
    '''m used to store values intermediate values used for solving pair of linear eqs'''
    m = 0 
    ''' n used to store values intermediate values used for solving pair of linear eqs'''
    n = 0 
    ''' a used to store exact values of a from using mode function to A matrix'''
    a = 0
    ''' b used to store exact values of b from using mode function to B matrix'''
    b = 0 

    for i in range (99):
        m = [[ x_data[i]*x_data[i], -y_data[i]] , [ x_data[i+1] * x_data[i+1], -y_data[i+1]] ]
        n = [1,1]
        [c,d] = np.linalg.solve(m,n)
        a = np.sqrt(c/d)
        b = np.sqrt(1/d)
        A = np.append(A,a)
        B = np.append(B,b)
        
    a = stats.mode(A)[0][0]
    b = stats.mode(B)[0][0]
    
    '''Estimating predicted value using parameters found '''
    
    y_hat = np.square(a*x)-np.square(b)  
    
    ''' Calculating error between predicted and actual values'''
    
    error = np.absolute((y-y_hat)/y) 
    
    ''' Finding the index with max error'''
    
    index_max_error = np.argmax(error) + 1 
    
    return index_max_error
''' assume x for example'''
x_data = np.linspace(0, 5, num=99) 
''' considered y according to given function'''
y_data = np.square(10*x_data)-np.square(5)
''' inserting wrong point at a index of 29 (28 index according to python indexing)'''
x_data = np.insert(x_data, 24, 6)
y_data = np.insert(y_data, 24, 200 )

index = main3(x_data,y_data)
index
