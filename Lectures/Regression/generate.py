import numpy as np

def get_data():
    X = np.random.randn(500,30)
    
    X[:,0] = 2000*X[:,0] + 5000
    X[:,1] = 100*X[:,1] - 20
    X[:,7] = 50*X[:,7]+120 - 10*X[:,3]
    
    y = 2*X[:,0] - 3*X[:,1] + X[:,7] + 20*np.random.randn(500)
    
    return X,y

def give_how_generated():
    print("""The data was generated using the following code.
    X = np.random.randn(500,30)
    
    X[:,0] = 2000*X[:,0] + 5000
    X[:,1] = 100*X[:,1] - 20
    X[:,7] = 50*X[:,7]+120 - 10*X[:,3]
    
    y = 2*X[:,0] - 3*X[:,1] + X[:,7] + 20*np.random.randn(500)""")