import numpy as np

chat_id = 1219503064 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    from math import log
    # Время в секундах, за которое машина преодолела путь
    time = 62 
    # Размер выборки
    n = len(x) 
    # Квантиль
    z = - np.log(1-p)/n 
    # Доверительный интервал
    return ( 2*(-(-x).min() - 1/2)/(time**2), 
             2*(z - (-x).min() - 1/2)/(time**2) ) 

