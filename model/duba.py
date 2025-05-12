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
    from model.neuron import neuron_adjustement
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
# variance  -> float                    -> Manage the value at start for the variance to be rectified
# variance_time_decrease    -> float    -> Manage the time for the variance to decrease
# training_round            -> int      -> Number of round to set the bias and coef
def dumb_banana(generate, dataset, column, neuron, layer = [], variance = .1, variance_time_decrease = 1.0, training_round = 1000):

    # init and check the given argument
    dumb = argument_handler(generate, dataset, column, neuron, layer, variance, variance_time_decrease, training_round)

    if (dumb == None):
        print("Dumb Banana have been stoped.")
        return

    if (dumb.generate == "neuron"):
        neuron_adjustement(dumb)
        dumb.save_neuron()
    elif (dumb.generate == "column"):
        pass
