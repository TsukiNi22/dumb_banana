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
    for round_nb in range(dumb.training_round):
        variations = []
        for i in range(len(dumb.dataset[dumb.column])):
            estimation = dumb.estimation(i)
            variations.append(dumb.dataset[dumb.column][i] - estimation)
            dumb.adjust(dumb.dataset[dumb.column][i] - estimation, round_nb, i)
        variation = sum(variations) / len(variations)
        print(f"{variation:.16F}\t|\t{dumb.variance:.16F}")
