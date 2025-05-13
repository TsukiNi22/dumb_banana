"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

 ██╗  ██╗ █████╗ ██████╗ ████████╗ █████╗ ███╗   ██╗██╗ █████╗ 
 ╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██║██╔══██╗
  ╚███╔╝ ███████║██████╔╝   ██║   ███████║██╔██╗ ██║██║███████║
  ██╔██╗ ██╔══██║██╔══██╗   ██║   ██╔══██║██║╚██╗██║██║██╔══██║
 ██╔╝ ██╗██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║██║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝

Edition:
##  13/05/2025 by Tsukini

File Name:
##  accuracy_class.py

File Description:
##  Class for the accuracy testing
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
try:
    import numpy as np
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Class """
class Accuracy():

    def __init__(self, generated_values, testing_values):
        # setup parametre
        self.generated_values = generated_values
        self.testing_values = testing_values
    
    def r2(self):
        arr_test = np.array(self.testing_values)
        arr_gene = np.array(self.generated_values)
        ss_res = np.sum((arr_test - arr_gene) ** 2)
        ss_tot = np.sum((arr_test - np.mean(arr_test)) ** 2)
        return 1 - (ss_res / ss_tot)

    def mae(self):
        arr_test = np.array(self.testing_values)
        arr_gene = np.array(self.generated_values)
        difference = np.abs(arr_test - arr_gene)
        return np.mean(difference)
    
    #def (self):
    #    pass
