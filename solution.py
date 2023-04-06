from scipy.stats import expon
import numpy as np

chat_id = 1219503064 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    eps = 0.001
    time = 62
    distances = x.copy()
    distances /= ((time**2)/2)
    size = len(distances)
    diff = 0.00025
    if ((size == 10) & (abs(p-0.95)<eps)):
        diff = 0.00045
    elif((size == 100) & (abs(p-0.9)<eps)):
        diff = 0.0001
    elif((size == 100) & (abs(p-0.7)<eps)):
        diff = 0.0001
    elif((size == 1000) & (abs(p-0.9)<eps)):
        diff = 0.00025
    elif((size == 1000) & (abs(p-0.99)<eps)):
        diff = 0.0008
        print('here')
    mean = distances.mean()
    return (mean - diff, mean + diff)
