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
##  argument.py

File Description:
##  Check argument given
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
try:
    from model.duba_class import DumbBanana
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Program """
def argument_handler(generate, dataset, column, neuron, layer, variance, variance_time_decrease, training_round):
    # init the neuron network
    dumb = DumbBanana(generate, dataset, column, neuron, layer, variance, variance_time_decrease, training_round)

    # check the type of the argument passed
    if (generate != "neuron" and generate != "column"):
        print("Generate can only be a 'neuron' or 'column'.")
        exit(1)
    if (not isinstance(dataset, dict)):
        print("The given dataset is not a dictionary.")
        exit(1)
    if (not isinstance(neuron, str)):
        print("The given neuron path is not a str.")
        exit(1)
    if (generate == "neuron" and not isinstance(layer, list)):
        print("The given layer is not a list of int value.")
        exit(1)
    if (generate == "neuron" and not isinstance(variance, int)):
        print("The given variance is not a int value.")
        exit(1)
    if (generate == "neuron" and not isinstance(variance_time_decrease, int)):
        print("The given variance time decrease is not a int value.")
        exit(1)
    if (generate == "neuron" and not isinstance(training_round, int)):
        print("The given variance time decrease is not a int value.")
        exit(1)

    if (generate == "neuron"):
        if (dumb.init_neuron()):
            return None
    else:
        if (dumb.init_column()):
            return None
    return dumb
