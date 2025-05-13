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
    from model.neuron import neuron_adjustement, column_generation
    from numpy import random, sort, arange, delete
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
def dumb_banana(generate, dataset, column, neuron, layer = [], start_variance = .1, end_variance = .1 / 100, variance_decrease = 10.0, training_round = 1000, bias_min = .0, bias_max = 1., coef_min = .1, coef_max = 1., k = 50.):

    # init and check the given argument
    dumb = argument_handler(generate, dataset, column, neuron, layer, start_variance, end_variance, variance_decrease, training_round, bias_min, bias_max, coef_min, coef_max, k)

    if (dumb == None):
        print("Dumb Banana have been stoped.")
        return

    if (dumb.generate == "neuron"):
        neuron_adjustement(dumb)
        dumb.save_neuron()
    elif (dumb.generate == "column"):
        column_generation(dumb)

# dataset   -> dictionaire (int, float) -> dictionaire of int and float value
# column    -> str                      -> column of the dictionaire who will be trained
# percent   -> float                    -> percent to use in the generation of the neuron network
def duba_dataset(dataset, column, percent = .5):

    # check of the argument
    if (not isinstance(dataset, dict)):
        print("The given dataset is not a dictionary.")
        exit(1)
    if (not isinstance(neuron, str)):
        print("The given neuron path is not a str.")
        exit(1)
    if (not isinstance(percent, float)):
        print("The given percent is not a float.")
        exit(1)
    keys = dataset.keys()
    if (not column in keys):
        print("The given column is not in the dataset.")
        exit(1)
    if (percent < .0 or percent > 1.):
        print(f"The given percent is not between 0.0 and 1.0: {percent}")
        exit(1)
    
    # setup of the set
    trainingset = {}
    testingset = {}
    testing_column = []
    size = len(dataset[column])
    training_index = sort(random.choice(size - 1, size = int(size * percent), replace = False))
    testing_index = sort(delete(arange(size - 1), training_index))

    for index in rdm_index:
        for key in keys:
            trainingset[key] = []
            if (key != column):
                testset[key] = []
        for i in training_index:
            for key in keys:
                trainingset[key].append(dataset[key][i])
        for i in testing_index:
            for key in keys:
                if (key == column):
                    testset[key].append(dataset[key][i])
                else:
                    testing_column.append(dataset[key][i])

    return trainingset, testingset, testing_values

# generated_values  -> list                     -> list of the value generated
# testing_values    -> list                     -> list of the real value
def duba_accuracy(generated_values, testing_values):

    # check of the argument
    if (not isinstance(generated_values, list)):
        print("The given generated values is not a list.")
        exit(1)
    if (not isinstance(testing_values, list)):
        print("The given testing values is not a list.")
        exit(1)

    # return the class that can be call for some value
    return Accuracy(generated_values, testing_values)
