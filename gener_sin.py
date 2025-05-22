import numpy as np
import matplotlib.pyplot as plt

def sine_wave_generator(f_start=0, f_end=50, fs=100, duration=1):
    """
    Генератор синусоидальных сигналов с частотами от f_start до f_end.
    
    f_start: Начальная частота (Гц)
    f_end: Конечная частота (Гц)
    fs: Частота дискретизации (Гц)
    duration: Длительность сигнала (сек)
    """
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    for f in np.linspace(f_start, f_end, num=100):  
        
        signal = np.sin(2 * np.pi * f * t)
        yield f, signal

generator = sine_wave_generator()

for freq, wave in generator:
    print(f"Частота: {freq:.2f} Гц, Первое значение сигнала: {wave [0] :.3f}")
    plt.plot(wave)
    plt.title(f"Синусоида при {freq:.2f} Гц")
    plt.xlabel("Образцы")
    plt.ylabel("Амплитуда")
    plt.show()