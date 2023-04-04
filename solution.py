from scipy.stats import expon
import numpy as np

chat_id = 1219503064 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    time = 62
    distances = x.copy()
    distances /= ((time**2)/2)
    added = 10000
    distances+=added
    alpha = 1 - p
    n = len(distances)
    min = distances.min()
    zquant1 = expon.ppf(alpha/2)
    zquant2 = expon.ppf(1-alpha/2)
    left = zquant1 / (n*min)
    right = zquant2 / (n*min)
    mean = distances.mean()
    return (mean - left - added, mean + right - added)
