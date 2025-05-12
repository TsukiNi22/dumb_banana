"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

 ██╗  ██╗ █████╗ ██████╗ ████████╗ █████╗ ███╗   ██╗██╗ █████╗ 
 ╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██║██╔══██╗
  ╚███╔╝ ███████║██████╔╝   ██║   ███████║██╔██╗ ██║██║███████║
  ██╔██╗ ██╔══██║██╔══██╗   ██║   ██╔══██║██║╚██╗██║██║██╔══██║
 ██╔╝ ██╗██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║██║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝

Edition:
##  12/05/2025 by Tsukini

File Name:
##  neuron.py

File Description:
##  Adjust the bias and coef of the neuron
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
try:
    from os import path, makedirs
    from json import load, dump
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Program """
def neuron_adjustement(dumb):
    #for round_nb in range(dumb.training_round):
    for round_nb in range(1):
        for i in range(len(dumb.dataset[dumb.column])):
            estimation = dumb.estimation(i)
            print(f"n°{i} = {estimation} | {dumb.dataset[dumb.column][i]}")
