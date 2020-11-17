
import numpy as np

def mean_absolute_error(predictions, ground_truth):

    return np.mean(np.abs(predictions-ground_truth))


def root_mean_squared_error(predictions,ground_truth):
    
    return np.sqrt(np.mean(np.power(predictions-ground_truth,2)))