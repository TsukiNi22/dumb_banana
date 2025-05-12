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
##  duba.py

File Description:
##  Main file of the model
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
try:
    pass
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Program """
if __name != "model":
    print("duba is a module, can only be imported!")
    exit(1)

# generate  -> True/False               -> Generate neurones or column value
# dataset   -> dictionaire (int, float) -> dictionaire of int and float value
# column    -> str                      -> column of the dictionaire to generate or train
# neurones  -> file_path                -> file to save or use the neurones
# layer     -> list                     -> With generate=True neurones number to set per layer
def dumb_banana(generate, dataset, column, neurones, layer = []):
    pass
