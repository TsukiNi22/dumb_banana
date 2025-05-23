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
def argument_handler(generate, dataset, column, neuron, layer,
        start_variance, end_variance, variance_decrease, training_round,
        bias_min, bias_max, coef_min, coef_max, k,
        display):

    # init the neuron network
    dumb = DumbBanana(generate, dataset, column, neuron, layer,
        start_variance, end_variance, variance_decrease, training_round,
        bias_min, bias_max, coef_min, coef_max, k,
        display)

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
    if (generate == "neuron" and not isinstance(start_variance, float)):
        print("The given start variance is not a float value.")
        exit(1)
    if (generate == "neuron" and not isinstance(end_variance, float)):
        print("The given end variance is not a float value.")
        exit(1)
    if (generate == "neuron" and not isinstance(variance_decrease, float)):
        print("The given variance decrease is not a float value.")
        exit(1)
    if (generate == "neuron" and not isinstance(training_round, int)):
        print("The given variance time decrease is not a int value.")
        exit(1)
    if (generate == "neuron" and not isinstance(bias_min, float)):
        print("The given bias min is not a float value.")
        exit(1)
    if (generate == "neuron" and not isinstance(bias_max, float)):
        print("The given bias max is not a float value.")
        exit(1)
    if (generate == "neuron" and not isinstance(coef_min, float)):
        print("The given coef min is not a float value.")
        exit(1)
    if (generate == "neuron" and not isinstance(coef_max, float)):
        print("The given coef max is not a float value.")
        exit(1)
    if (generate == "neuron" and not isinstance(k, float)):
        print("The given k is not a float value.")
        exit(1)
    if (generate == "neuron" and not isinstance(display, bool)):
        print("The given display is not a boolean value.")
        exit(1)

    if (generate == "neuron"):
        if (dumb.init_neuron()):
            return None
    else:
        if (dumb.init_column()):
            return None
    return dumb
