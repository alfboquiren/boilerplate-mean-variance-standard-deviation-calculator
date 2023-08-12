import numpy as np

def calculate(list):
    if(len(list) == 9):
      list = np.array(list).reshape((3, 3))
      mean_axis1 = list.mean(0).tolist()
      mean_axis2 = list.mean(1).tolist()
      mean_flattened = list.mean()
      variance_axis1 = list.var(0).tolist()
      variance_axis2 = list.var(1).tolist()
      variance_flattened = list.var()
      standard_deviation_axis1 = list.std(0).tolist()
      standard_deviation_axis2 = list.std(1).tolist()
      standard_deviation_flattened = list.std()
      max_axis1 = list.max(0).tolist()
      max_axis2 = list.max(1).tolist()
      max_flattened = list.max()
      min_axis1 = list.min(0).tolist()
      min_axis2 = list.min(1).tolist()
      min_flattened = list.min()
      sum_axis1 = list.sum(0).tolist()
      sum_axis2 = list.sum(1).tolist()
      sum_flattened = list.sum()
      calculations = {
        'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [variance_axis1, variance_axis2, variance_flattened],
        'standard deviation': [standard_deviation_axis1, standard_deviation_axis2, standard_deviation_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened]
      }
      return calculations
    else:
      raise ValueError('List must contain nine numbers.')