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
##  duba_class.py

File Description:
##  Class for the neuron network
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
try:
    from os import path, makedirs
    from json import load, dump
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Class """
class DumbBanana():
    
    def __init__(self, generate, dataset, column, neuron, layer):
        # given argument
        self.generate = generate
        self.dataset = dataset
        self.column = column
        self.neuron = neuron
        self.layer = layer

        # generated value
        self.neuron_network = []
        self.neuron_values = []

    def get_neuron(self):
        try:
            with open(self.neuron, "r") as file:
                self.neuron_network = load(file)
        except PermissionError:
            print(f"Invalid permission, can't get the neuron network in '{self.neuron}'.")
            exit(1)
    
    def save_neuron(self):
        try:
            with open(self.neuron, "w") as file:
                dump(self.neuron_network, file)
        except PermissionError:
            print(f"Invalid permission, can't save the generated neuron at '{self.neuron}'.")
            exit(1)

    def init_neuron(self):
        # check the dictionary value and the asked column
        keys = list(self.dataset.keys())
        if (not self.column in keys):
            print(f"Can't found the column '{self.column}' in the dictionary keys.")
            exit(1)
        for key in keys:
            if (not all(isinstance(val, int) or isinstance(val, float) for val in self.dataset[key])):
                print(f"Invalid value in the dictionary at the column '{key}', can only be int or float.")
                exit(1)

        # setup the neuron file
        dirs = path.dirname(self.neuron)
        if not path.exists(dirs) and dirs != "":
            try:
                makedirs(dirs)
            except PermissionError:
                print(f"Invalid permission, can't create the dirs: '{dirs}'")
                exit(1)
        if path.isfile(self.neuron):
            res = str(input(f"The file '{self.neuron}' already exit, do you want to overwrite the file (y/n)? "))
            if (res == "N"  or res == "n" or res == "No" or res == "no" or res == "NO" or res == "nO"):
                return True

        # setup the neuron network
        if (not all(isinstance(val, int) for val in self.layer)):
            print(f"Invalid value type in the given layer, can only be int.")
        # add the neuron for the input
        layer_links = []
        layer_values = []
        for i in range(len(keys) - 1):
            layer_links.append([])
            layer_values.append(0)
        self.neuron_network.append(layer_links)
        self.neuron_values.append(layer_values)
        # add the neuron of the chosen layer
        for neuron_nb in self.layer:
            layer_links = []
            layer_values = []
            for i in range(neuron_nb):
                layer_links.append([])
                layer_values.append(0)
            self.neuron_network.append(layer_links)
            self.neuron_values.append(layer_values)
        # add the last neuron who synthetise all
        self.neuron_values.append([0])

        return False

    def init_column(self):
        # check the dictionary value
        keys = list(self.dataset.keys())
        if (self.column in keys):
            res = str(input(f"The column '{self.column}' already exit, do you want to overwrite the column values (y/n)? "))
            if (res == "N"  or res == "n" or res == "No" or res == "no" or res == "NO" or res == "nO"):
                return True
        for key in keys:
            if (not all(isinstance(val, int) or isinstance(val, float) for val in self.dataset[key])):
                print(f"Invalid value in the dictionary at the column '{key}', can only be int or float.")
                exit(1)

        # setup the neuron network
        if (not path.isfile(self.neuron)):
            print(f"The given neuron network path is not a valid path: {self.neuron}")
            exit(1)
        self.get_neuron()
        for i in range(len(self.neuron_network)):
            layer_values = []
            for j in range(len(self.neuron_network[i])):
                layer_values.append(0)
            self.neuron_values.append(layer_values)
        self.neuron_values.append([0])
        
        return False
