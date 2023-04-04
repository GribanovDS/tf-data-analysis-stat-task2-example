from scipy.stats import chi2, expon
import numpy as np

chat_id = 1219503064 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    time = 62
    distances = x.copy()
    distances = 0.5 - distances
    distances /= ((time**2)/2)
    alpha = 1 - p
    n = len(distances)
    df = 2 * n
    sum = 0
    for elem in distances:
        sum+=elem
    chi2_value_1 = chi2.ppf(alpha / 2, df)
    chi2_value_2 = chi2.ppf(1 - alpha / 2, df)
    left = 2 * sum / chi2_value_1 
    right = 2 * sum / chi2_value_2
    return (left, right)
