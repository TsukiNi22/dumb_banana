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
        self.generated_neuron = []
        self.generated_column = []

    def get_neuron(self):
        try:
            with open(self.neuron, "r") as file:
                self.layer = load(file)
        except PermissionError:
            print(f"Invalid permission, can't get the neuron in '{self.neuron}'.")
            exit(1)
    
    def save_neuron(self):
        try:
            with open(self.neuron, "w") as file:
                dump(self.generated_neuron, file)
        except PermissionError:
            print(f"Invalid permission, can't save the generated neuron at '{self.neuron}'.")
            exit(1)

    def init_neuron(self):
        keys = list(self.dataset.keys())
        
        # check the dictionary value and the asked column
        if (not self.column in keys):
            print(f"Can't found the column '{self.column}' in the dictionary keys.")
            exit(1)
        for key in keys:
            if (not all(isinstance(val, int) for val in self.dataset[key]):
                print(f"Invalid value in the dictionary at the column '{key}', can only be int or float.")
                exit(1)

        # setup the neuron file
        dirs = path.dirname(self.neuron)
        if not path.exists(dirs):
            try:
                makedirs(dirs)
            except PermissionError:
                print(f"Invalid permission, can't create the dirs: '{dirs}'")
                exit(1)
        if not path.isfile(self.neuron):
                res = str(input("The file '{self.neuron}' already exit, do you want to overwrite the file (y/n)?"))
            if (res == "N"  or res == "n" or res == "No" or res == "no" or res == "NO" or res == "nO"):
                return True

        # setup generated neuron list
        for neuron_nb in len(self.layer):
            layer = []
            for i in range(neuron_nb):
                layer.append(1)
            self.generated_neuron.append(layer)

        return False

    def init_column(self):
        if (path.isfile(neuron)):
            print(f"The given neuron network path is not a valid path: {neuron}")
            exit(1)
