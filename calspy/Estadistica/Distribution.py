from math import sqrt

class Distribution:
    def __init__(self,values:list,probabilities:list):
        self.values = values
        self.probabilities = probabilities
        self.check_types()
        self.check_probabilities()

    def check_types(self):
        band_1 = all(isinstance(i, (int, float, str)) for i in self.values)
        band_2 = all(isinstance(i, (int, float)) for i in self.probabilities)
        self.is_valid_types = band_1 and band_2
        return self.is_valid_types
    
    def check_probabilities(self):
        value_sum = sum(self.probabilities)
        self.is_valid_check_probabilities = ((value_sum/3) == (1/3)) 
        return self.is_valid_check_probabilities
    
    def probability_independent_events(self,position_one:int,distribution:object,position_two:int):
        if isinstance(distribution,Distribution) and isinstance(position_one,int) and isinstance(position_two,int):
            if self.check_probabilities() and self.check_types() and distribution.check_probabilities() and distribution.check_types():
                probability_one = self.probabilities[position_one]
                probability_two = distribution.probabilities[position_two]
                return probability_one * probability_two
        return 0

    def distribution_function(self):
        if self.check_probabilities() and self.check_types():
            self.list_distribution_function = list()
            self.list_distribution_function.append(self.probabilities[0])
            for i in range(len(self.probabilities) - 1):
                prior_probability = self.list_distribution_function[i]
                current_probability = self.probabilities[i+1]
                self.list_distribution_function.append(prior_probability + current_probability)
            return self.list_distribution_function
        return list()
    
    def calculate_mean(self):
        if self.check_probabilities() and self.check_types():
            self.mean = 0
            for i in range(len(self.probabilities)):
                self.mean += (self.probabilities[i] * self.values[i])
            return self.mean
        return 0
    
    def calculate_variance(self):
        if self.check_probabilities() and self.check_types():
            self.calculate_mean()
            self.variance = 0
            for i in range(len(self.probabilities)):
                self.variance += (self.probabilities[i] * (self.values[i] ** 2))
            self.variance = self.variance - (self.mean ** 2)
            return self.variance
        return 0
    
    def calculate_standard_deviation(self):
        if self.check_probabilities() and self.check_types():
            self.calculate_variance()
            self.standard_deviation = sqrt(self.variance)
            return self.standard_deviation



probability = (1/6)
a = Distribution([1, 2, 3,4,5,6],[probability for i in range(6)])
b = Distribution([1, 2, 3,4,5,6],[probability for i in range(6)])

print(a.probabilities)
print(a.values)
print(a.check_probabilities())
print(a.check_types())
print(a.probability_independent_events(1,b,1))
print(a.distribution_function())
print(a.calculate_mean())
print(a.calculate_variance())
print(a.calculate_standard_deviation())
