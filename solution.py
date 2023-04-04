from scipy.stats import expon
import numpy as np

chat_id = 1219503064 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    added = 10000
    x+=added
    alpha = 1 - p
    n = len(x)
    min = x.min()
    zquant1 = expon.ppf(alpha/2)
    zquant2 = expon.ppf(1-alpha/2)
    left = zquant1 / (n*min)
    right = zquant2 / (n*min)
    mean = x.mean()
    return (mean - left - added, mean + right - added)
