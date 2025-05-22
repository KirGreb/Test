import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def interpolate_signal(signal, factor=2, method='linear'):
    """
    Интерполирует входной сигнал, увеличивая его частоту дискретизации в factor раз.
    
    signal: исходный сигнал (массив numpy)
    factor: коэффициент повышения частоты дискретизации
    method: тип интерполяции ('linear', 'cubic', 'quadratic' и т.д.)
    """
    n_points = len(signal)
    # Создаем исходные точки по индексу
    original_indices = np.arange(n_points)
    
    # Создаем новые точки с увеличенной плотностью
    new_points = np.linspace(0, n_points - 1, n_points * factor)
    
    # Создаем интерполяционный объект
    interpolator = interp1d(original_indices, signal, kind=method)
    
    # Получаем интерполированный сигнал
    interpolated_signal = interpolator(new_points)
    
    return interpolated_signal

# Исходный сигнал
fs = 100  # исходная частота дискретизации
t = np.linspace(0, 1, fs, endpoint=False)
original_signal = np.sin(2 * np.pi * 10 * t)  # синусоида 10 Гц

# Интерполяция в 2 раза
new_signal = interpolate_signal(original_signal, factor=2, method='cubic')

# Временные оси для визуализации
t_new = np.linspace(0, 1, len(new_signal), endpoint=False)

# Визуализация
plt.plot(t, original_signal, 'o-', label='Исходный сигнал')
plt.plot(t_new, new_signal, '.', label='Интерполированный сигнал')
plt.legend()
plt.xlabel('Время, с')
plt.ylabel('Амплитуда')
plt.title('Интерполяция сигнала в 2 раза')
plt.show()
