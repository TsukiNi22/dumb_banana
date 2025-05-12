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
    from model.argument import argument_handler
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Program """
if __name__ != "model.duba":
    print("duba is a module, can only be imported!")
    exit(1)

# generate  -> "neuron" / "column"      -> Generate neurones or column value
# dataset   -> dictionaire (int, float) -> dictionaire of int and float value
# column    -> str                      -> column of the dictionaire to generate or train
# neuron    -> file_path                -> file to save or use the neuron
# layer     -> list                     -> With generate=True, neurones number to set per layer
def dumb_banana(generate, dataset, column, neuron, layer = []):

    # init and check the given argument
    dumb = argument_handler(generate, dataset, column, neuron, layer)

    if (dumb == None)
        print("Dumb Banana have been stoped!!!")
        return None
