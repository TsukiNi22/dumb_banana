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
# start_variance            -> float    -> Manage the value at start for the variance
# end_variance              -> float    -> Manage the value at end for the variance
# variance_decrease         -> float    -> Manage the decrease of the variance
# training_round            -> int      -> Number of round to set the bias and coef
# bias_min  -> float                    -> The minimun value of the bias to be generated
# bias_max  -> float                    -> The maxmimun value of the bias to be generated
# coef_min  -> float                    -> The minimun value of the coef to be generated
# coef_max  -> float                    -> The maxmimun value of the coef to be generated
# k         -> float                    -> define the slope of the weight function
def dumb_banana(generate, dataset, column, neuron, layer = [], start_variance = .1, end_variance = .1 / 100, variance_decrease = 10.0, training_round = 1000, bias_min = .0, bias_max = 1., coef_min = .1, coef_max = 1., k = 5.):

    # init and check the given argument
    dumb = argument_handler(generate, dataset, column, neuron, layer, start_variance, end_variance, variance_decrease, training_round, bias_min, bias_max, coef_min, coef_max, k)

    if (dumb == None):
        print("Dumb Banana have been stoped.")
        return

    if (dumb.generate == "neuron"):
        neuron_adjustement(dumb)
        dumb.save_neuron()
    elif (dumb.generate == "column"):
        variations = []
        for i in range(len(dumb.dataset[dumb.column])):
            estimation = dumb.estimation(i)
            variations.append(dumb.dataset[dumb.column][i] - estimation)
        variation = sum(variations) / len(variations)
        print(f"{variation}")
        pass
