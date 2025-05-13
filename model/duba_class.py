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
##  duba_class.py

File Description:
##  Class for the neuron network
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Import """
try:
    from os import path, makedirs
    from json import load, dump
    from numpy import linspace, exp, random, clip
except ImportError as e:
    print(f"Import Error: {e}")
    exit(1)

""" Class """
class DumbBanana():
    
    def __init__(self, generate, dataset, column, neuron, layer, start_variance, end_variance, variance_decrease, training_round, bias_min, bias_max, coef_min, coef_max, k):
        # given argument
        self.generate = generate
        self.dataset = dataset
        self.column = column
        self.neuron = neuron

        # option
        self.k = k
        self.bias_min = bias_min
        self.bias_max = bias_max
        self.coef_min = coef_min
        self.coef_max = coef_max
        self.layer = layer
        self.start_variance = start_variance
        self.end_variance = end_variance
        self.variance_decrease = variance_decrease
        self.training_round = training_round

        # neuron data
        self.variation = None
        self.neuron_network = [] # [bias, coef, coef, ...] = neuron | [neuron, ...] = layer | [layer, ...] = neuron_network
        self.neuron_values = []
        self.neuron_percent = []

        # setup variance array
        x_start = self.start_variance
        x_end = self.end_variance
        steepness = self.variance_decrease
        T = self.training_round
        t = linspace(0, 1, T)
        self.variance_array = x_end + (x_start - x_end) * (1 - 1 / (1 + exp(-steepness * (t - 0.5))))
        self.variance = self.variance_array[0]

    def estimation(self, row):
        # reset the value stored in neuron_values
        for i in range(len(self.neuron_values)):
            for j in range(len(self.neuron_values[i])):
                # Commented for the bias desactivation
                #self.neuron_values[i][j] = self.neuron_network[i][j][0]
                self.neuron_values[i][j] = 0

        # get the line value from the dataset row
        data = []
        keys = list(self.dataset.keys())
        keys.pop(keys.index(self.column))
        try:
            for key in keys:
                data.append(self.dataset[key][row])
        except IndexError as e:
            print(f"All the column of the dataset must be at least of the '{self.column}' column size.")
            exit(1)

        # setup the data for the first neuron row
        for i in range(len(data)):
            self.neuron_values[0][i] = data[i]

        # make the calculation from the row of data
        for i in range(len(self.neuron_network) - 1):
            layer = self.neuron_network[i]
            for j in range(len(layer)):
                neuron = layer[j]
                for k in range(len(neuron) - 1):
                    coef = neuron[k + 1]
                    self.neuron_values[i + 1][k] += self.neuron_values[i][j] * coef

        return self.neuron_values[-1][0]

    def adjust(self, variation, round_nb, row):
        
        # set the value in percent
        total = 0
        for layer in self.neuron_values:
            for n in layer:
                total += n
        for i in range(len(self.neuron_values)):
            for j in range(len(self.neuron_values[i])):
                self.neuron_percent[i][j] = self.neuron_values[i][j] / total
        
        # calcul the weight of the variation
        if (self.variation == None or self.variation < abs(variation)):
            self.variation = abs(variation)
        weight = normalized_exp_growth(abs(variation), self.variation, self.k)

        # modifie the coef value due to the weight calculated just above
        signe = 1
        if (variation < 0):
            signe = -1
        for i in range(len(self.neuron_network) - 1):
            layer = self.neuron_network[i]
            for j in range(len(layer)):
                neuron = layer[j]
                # Commented for the bias
                #diff = []
                for k in range(len(neuron) - 1):
                    #diff.append(neuron[k + 1])
                    neuron[k + 1] += neuron[k + 1] * self.variance * self.neuron_percent[i][j] * self.neuron_percent[i + 1][k] * signe
                    #diff[-1] = 1 - (neuron[k + 1] / diff[-1])
                #layer[j][0] += layer[j][0] * (sum(diff) / len(diff)) * signe
        self.variance = self.variance_array[round_nb]

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
            exit(1)
        self.layer.append(1)
        # add the neuron for the input
        layer_links = []
        layer_values = []
        layer_percent = []
        for i in range(len(keys) - 1):
            layer_links.append([random.uniform(self.bias_min, self.bias_max)])
            for j in range(self.layer[0]):
                layer_links[-1].append(random.uniform(self.coef_min, self.coef_max))
            layer_values.append(0)
            layer_percent.append(0)
        self.neuron_network.append(layer_links)
        self.neuron_values.append(layer_values)
        self.neuron_percent.append(layer_percent)
        # add the neuron of the chosen layer
        for i in range(len(self.layer)):
            layer_links = []
            layer_values = []
            layer_percent = []
            for j in range(self.layer[i]):
                layer_links.append([random.uniform(self.bias_min, self.bias_max)])
                if (i + 1 < len(self.layer)):
                    for k in range(self.layer[i + 1]):
                        layer_links[-1].append(random.uniform(self.coef_min, self.coef_max))
                layer_values.append(0)
                layer_percent.append(0)
            self.neuron_network.append(layer_links)
            self.neuron_values.append(layer_values)
            self.neuron_percent.append(layer_percent)

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
        
        return False

def normalized_exp_growth(x, n_max, k = 5):
    x = clip(x, 0, n_max)
    raw = 1 - exp(-k * x / n_max)
    max_val = 1 - exp(-k)
    return raw / max_val
