import numpy as np


def calculate(number_list):
    if len(number_list) != 9:
        return "ValueError, List must contain nine numbers."
    calculations = {}
    number_list_array = np.array(([number_list[:3]], [number_list[3:6]], [number_list[6:]]))
    mean = [np.mean(number_list_array, axis=0),np.mean(number_list_array, axis=2), np.mean(number_list_array)]
    variance = [np.var(number_list_array, axis=0),np.var(number_list_array, axis=2), np.var(number_list_array)]
    stddev = [np.std(number_list_array, axis=0), np.std(number_list_array, axis=2), np.std(number_list_array)]
    Max = [np.max(number_list_array, axis=0),np.max(number_list_array, axis=2),np.max(number_list_array)]
    Min = [np.min(number_list_array,axis=0),np.min(number_list_array, axis=2),np.min(number_list_array)]
    Sum = [np.sum(number_list_array,axis=0), np.sum(number_list_array, axis=2), np.sum(number_list_array)]
    calculations["Mean"] = mean
    calculations["Variance"] = variance
    calculations['Standard deviation'] = stddev
    calculations['Max'] = Max
    calculations['Min'] = Min
    calculations['Sum'] = Sum

    return calculations
