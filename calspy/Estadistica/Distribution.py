from math import sqrt,factorial,pow
from collections import Counter

class Distribution:
    def __init__(self,values:list,probabilities:list):
        self.values = values
        self.probabilities = probabilities
        self.list_distribution_function = list()
        self.mean = 0
        self.variance = 0
        self.standard_deviation = 0
        self.deviation_mean = 0
        self.check_types()
        self.check_probabilities()
        

    def check_types(self):
        band_1 = all(isinstance(i, (int, float)) for i in self.values)
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
        return 0
        
    def calculate_list_deviation_mean(self):
        if self.check_probabilities() and self.check_types():
            self.calculate_mean();
            list_deviation_mean = list()
            deviation_mean = 0
            for i in range(len(self.values)):
                deviation_mean =  self.values[i] - self.mean
                list_deviation_mean.append(deviation_mean)
            return list_deviation_mean
        return 0
    
    def calculate_deviation_mean(self):
        if self.check_probabilities() and self.check_types():
            self.calculate_mean();
            self.deviation_mean = 0
            for i in range(len(self.values)):
                self.deviation_mean +=  abs(self.values[i] - self.mean)
            self.deviation_mean = (self.deviation_mean / len(self.values))
            return self.deviation_mean
        return 0


class Distribution_Binomial (Distribution):
    def __init__ (self,value_success,value_failure,probability_success,probability_failure):
        values = [value_success, value_failure]
        probabilities = [probability_success,probability_failure]
        super().__init__(values,probabilities)
    
    def distribution_bernoulli(self,num_experiments:int,num_successes:int,kind:str):
        if super().check_probabilities() and super().check_types():
            numerator = factorial(num_experiments)
            denominator = factorial(num_successes) * factorial(num_experiments - num_successes)
            combinatorial_number = numerator / denominator
            probability_success = self.probabilities[0] ** num_successes
            probability_failure = self.probabilities[1] ** (num_experiments - num_successes)
            bernoulli = combinatorial_number * probability_success * probability_failure
            if (kind == "success"):
                return bernoulli
            elif (kind == "failure"):
                return (1 - bernoulli)
            else:
                return 0
        return 0
    
    def calculate_mean(self,num_experiments:int):
        if super().check_probabilities() and super().check_types():
            self.mean = num_experiments * self.probabilities[0]
            return self.mean
        return 0
    
    def calculate_variance(self,num_experiments:int):
        if super().check_probabilities() and super().check_types():
            self.variance = num_experiments * self.probabilities[0] * self.probabilities[1]
            return self.variance
        return 0
    
    def calculate_standard_deviation(self,num_experiments:int):
        if super().check_probabilities() and super().check_types():
            self.standard_deviation = sqrt(self.calculate_variance(num_experiments))
            return self.standard_deviation
        return 0
class Distribution_without_probability(Distribution):
    def __init__(self,values:list):
        super().__init__(values,[1])
        self.rango = 0
        self.geometric_mean = 0

    def calculate_rango(self):
        if super().check_types() and super().check_probabilities():
            self.rango = max(self.values) - min(self.values)
            return self.rango
        return 0
    
    def calculate_mean(self):
        if super().check_types() and super().check_probabilities():
            self.mean = 0
            for i in range(len(self.values)):
                self.mean += self.values[i]
            self.mean = self.mean / len(self.values)
            return self.mean
        return 0
    
    def calculate_geometric_mean(self):
        if super().check_types() and super().check_probabilities():
            self.geometric_mean = 1
            for i in range(len(self.values)):
                self.geometric_mean *= self.values[i]
            self.geometric_mean = pow(self.geometric_mean,1/len(self.values))
            return self.geometric_mean
        return 0
    
    def calculate_variance(self):
        if super().check_types() and super().check_probabilities():
            self.calculate_mean()
            values_2 = [i ** 2 for i in self.values]
            self.variance = (sum(values_2) / len(self.values)) - (self.mean ** 2)   
            return self.variance
        return 0
    
    def calculate_standard_deviation(self):
        if super().check_probabilities() and super().check_types():
            self.calculate_variance()
            self.standard_deviation = sqrt(self.variance) 
            return self.standard_deviation
        return 0
    
    def calculate_dictionary_absolute_frequency(self):
        if super().check_probabilities() and super().check_types():
            sort_values = sorted(self.values)
            return dict(Counter(sort_values))
        return dict()
    
    def calculate_dictionary_relative_frequency(self):
        if super().check_probabilities() and super().check_types():
            dictionary_relative_frequency = self.calculate_dictionary_absolute_frequency();
            total = len(self.values)
            for key in dictionary_relative_frequency:
                dictionary_relative_frequency[key] = dictionary_relative_frequency[key] / total
            return dictionary_relative_frequency
        return dict()
    
    def calculate_dictionary_cumulative_frequency(self):
        if super().check_probabilities() and super().check_types():
            dictionary_cumulative_frequency = self.calculate_dictionary_absolute_frequency()
            sum_value = 0
            for key in dictionary_cumulative_frequency:
                dictionary_cumulative_frequency[key] += sum_value
                sum_value = dictionary_cumulative_frequency[key]
            return dictionary_cumulative_frequency
        return dict()

    def calculate_dictionary_cumulative_relative_frequency(self):
        if super().check_probabilities() and super().check_types():
            dictionary_cumulative_relative_frequency = self.calculate_dictionary_relative_frequency()
            sum_value = 0
            for key in dictionary_cumulative_relative_frequency:
                dictionary_cumulative_relative_frequency[key] += sum_value
                sum_value = dictionary_cumulative_relative_frequency[key]
            return dictionary_cumulative_relative_frequency
        return dict()
    
    def calculate_list_mode(self):
        dictionary_absolute_frequency = self.calculate_dictionary_absolute_frequency()
        maxi = 0
        list_mode = []
        mode = 0
        mode_2 = 0 
        for key in dictionary_absolute_frequency:
            if dictionary_absolute_frequency[key] > maxi:
                maxi = dictionary_absolute_frequency[key]
                list_mode.clear()
                list_mode.append(key)
            elif dictionary_absolute_frequency[key] == maxi:
                list_mode.append(key)
        return list_mode
    
    def calculate_median(self):
        dictionary_cumulative_frequency = self.calculate_dictionary_cumulative_frequency()
        last_index = len(dictionary_cumulative_frequency) - 1
        total_frequency = dictionary_cumulative_frequency[last_index]
        mean = 0
        mean_2 = 0
        median = 0
        median_2 = 0
        is_pair = (total_frequency % 2) == 0
        if is_pair:
            mean = total_frequency/2
            mean_2 += 1
        else:
            total_frequency += 1
            mean = total_frequency/2
        list_keys = dictionary_cumulative_frequency.keys();

        for i in range(len(list_keys) - 1):
            key = list_keys[i]
            key_2 = list_keys[i+1]
            value = (dictionary_cumulative_frequency[key])
            velue_2 = (dictionary_cumulative_frequency[key_2])
            if value >= mean and velue_2 < mean:
                median = key
                break;

        if is_pair:
            for i in range(len(list_keys) - 1):
                key = list_keys[i]
                key_2 = list_keys[i+1]
                value = (dictionary_cumulative_frequency[key])
                velue_2 = (dictionary_cumulative_frequency[key_2])
                if value >= mean_2 and velue_2 < mean_2:
                    median_2 = key
                    break;
            return (median + median_2)/2
        else:
            return median

class Distribution_Grouped(Distribution):
    def __init__(self,valuesGroup:list,frequency:list):
        self.frequency = frequency
        self.values = list()
        self.valuesGroup = valuesGroup
        band = self.check_list_of_lists()
        if band:
            for i in range(len(valuesGroup)):
                self.values.append((valuesGroup[i][0] + valuesGroup[i][1]) / 2)
            super().__init__(self.values,[1])

    def check_list_of_lists(self):
        band_1 = all(isinstance(i, (list)) for i in self.valuesGroup)
        band_2 = True
        for i in range(len(self.valuesGroup)):
            band_2 = len(self.valuesGroup[i]) == 2
            if not(band_2):
                break
        return (band_1 and band_2)
    
    def calculate_mean(self):
        if super().check_types() and super().check_probabilities() and self.check_list_of_lists():
            self.mean = 0
            for i in range(len(self.frequency)):
                self.mean += self.values[i] * self.frequency[i]
            self.mean = self.mean / sum(self.frequency)
            return self.mean

    def calculate_list_deviation_mean(self):
        if super().check_types() and super().check_probabilities() and self.check_list_of_lists():
            self.calculate_mean();
            list_deviation_mean = list()
            deviation_mean = 0
            for i in range(len(self.frequency)):
                deviation_mean =  abs(self.values[i] - self.mean) * self.frequency[i]
                list_deviation_mean.append(deviation_mean)
            return list_deviation_mean
        return 0
    
    def calculate_deviation_mean(self):
        if super().check_types() and super().check_probabilities() and self.check_list_of_lists():
            list_deviation_mean = self.calculate_list_deviation_mean()
            self.deviation_mean = sum(list_deviation_mean) / sum(self.frequency)
            return self.deviation_mean
        return 0
    
    def calculate_list_variance(self):
        if super().check_types() and super().check_probabilities() and self.check_list_of_lists():
            list_variance = list()
            variance = 0
            for i in range(len(self.frequency)):
                variance =  (self.values[i] ** 2) * self.frequency[i]
                list_variance.append(variance)
            return list_variance
        return 0
    
    def calculate_variance(self):
        if super().check_types() and super().check_probabilities() and self.check_list_of_lists():
            self.calculate_mean();
            list_variance = self.calculate_list_variance()
            self.variance = (sum(list_variance) / sum(self.frequency)) - (self.mean ** 2)
            return self.variance
        return 0
    
    def calculate_standard_deviation(self):
        if super().check_probabilities() and super().check_types() and self.check_list_of_lists():
            self.calculate_variance()
            self.standard_deviation = sqrt(self.variance) 
            return self.standard_deviation
        return 0
class Distribution_Normal (Distribution):
    pass



probability = (1/6)
a = Distribution([1, 2, 3,4,5,6],[probability for i in range(6)])
b = Distribution([1, 2, 3,4,5,6],[probability for i in range(6)])
c = Distribution_Binomial(1,2,0.5,0.5)

print(a.probabilities)
print(a.values)
print(a.check_probabilities())
print(a.check_types())
print(a.probability_independent_events(1,b,1))
print(a.distribution_function())
print(a.calculate_mean())
print(a.calculate_variance())
print(a.calculate_standard_deviation())
print(a.calculate_list_deviation_mean())
print(a.calculate_deviation_mean())

print("-------------------------------------")

print(c.distribution_bernoulli(10,8,"success"))
print(c.distribution_bernoulli(10,8,"failure"))
print(c.distribution_bernoulli(10,8,"success") + c.distribution_bernoulli(10,8,"failure"))
print(c.calculate_mean(10))
print(c.calculate_variance(10))
print(c.calculate_standard_deviation(10))

print("-------------------------------------")

d = Distribution_without_probability([0,2,4,5,8,10,10,15,38])
e = Distribution_without_probability([8,7,9,8,8,10,9,7,4,9])
f = Distribution_without_probability([0,2,4,5,8,10,10,15,38])

print(d.calculate_rango())
print(d.calculate_mean())
print(d.calculate_list_deviation_mean())
print(d.calculate_deviation_mean())

print("-------------------------------------")

print(e.calculate_mean())
print(e.calculate_deviation_mean())

print("-------------------------------------")

print(f.calculate_mean())
print(f.calculate_list_deviation_mean())
print(f.calculate_deviation_mean())
print(f.calculate_variance())

print("-------------------------------------")

valuesGroup = [[160,170],[170,180],[180,190],[190,200],[200,210]]
frequency = [1,2,4,3,2] 
g = Distribution_Grouped(valuesGroup, frequency)
print(g.calculate_mean())
print(g.calculate_list_deviation_mean())
print(g.calculate_deviation_mean())
print(g.calculate_list_variance())
print(g.calculate_variance())
print(g.calculate_standard_deviation())

print("-------------------------------------")

h = Distribution_without_probability([1,1,2,0,3,2,1,4,2,3,1,0,0,1,2])
print(h.calculate_dictionary_absolute_frequency())
print(h.calculate_dictionary_relative_frequency())
print(h.calculate_dictionary_cumulative_frequency())
print(h.calculate_dictionary_cumulative_relative_frequency())
print(h.calculate_list_mode())

print("-------------------------------------")

i = Distribution_without_probability([2,2,4])
print(i.calculate_geometric_mean())