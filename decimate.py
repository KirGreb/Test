import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import decimate, butter, filtfilt

def decimate_signal(signal, factor=2, cutoff_freq=None, fs=100):
    """
    Понижает частоту дискретизации сигнала в factor раз с предварительной фильтрацией.
    
    signal: входной сигнал (массив numpy)
    factor: коэффициент понижения (например, 2)
    cutoff_freq: частота среза фильтра (Гц), по умолчанию - половина новой частоты дискретизации
    fs: исходная частота дискретизации (Гц)
    """
    # Если частота среза не указана, берем половину новой частоты дискретизации
    if cutoff_freq is None:
        cutoff_freq = fs / (2 * factor)  # чтобы избежать алиасинга
    
    # Создаем низкочастотный фильтр Баттерворта
    nyq = 0.5 * fs
    normal_cutoff = cutoff_freq / nyq
    b, a = butter(N=4, Wn=normal_cutoff, btype='low')
    
    # Фильтрация сигнала
    filtered_signal = filtfilt(b, a, signal)
    
    # Децимация — выборка каждого второго образца
    downsampled_signal = filtered_signal[::factor]
    
    return downsampled_signal

# Создаем пример сигнала
fs = 100  
t = np.linspace(0, 1, fs, endpoint=False)
signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 40 * t)  

# Понижение частоты дискретизации в 2 раза
new_signal = decimate_signal(signal, factor=2, fs=fs)

# Новая частота дискретизации
new_fs = fs // 2
t_new = np.linspace(0, 1, len(new_signal), endpoint=False)

# Визуализация
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal, label='Исходный сигнал')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t_new, new_signal, 'o-', label='Децимированный сигнал')
plt.legend()

plt.xlabel('Время, с')
plt.tight_layout()
plt.show()
