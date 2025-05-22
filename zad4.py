import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import decimate, resample

# Параметры сигнала
Fs = 1000  # исходная частота дискретизации (Гц)
T = 1.0    # длительность сигнала (сек)
t = np.linspace(0, T, int(Fs*T), endpoint=False)

# Функция сигнала (синусоида)
def generate_signal(f, t):
    return np.sin(2 * np.pi * f * t)

# Функция для измерения ошибки
def compute_error(original, reconstructed):
    return np.linalg.norm(original - reconstructed) / np.linalg.norm(original)

# Частоты для тестирования
frequencies = np.linspace(50, 400, 8)  # от 50 до 400 Гц
M = 4  # фактор децимирования

errors = []

for f in frequencies:
    # Генерируем исходный сигнал
    signal = generate_signal(f, t)

    # Децимация (уменьшение частоты)
    decimated_signal = decimate(signal, M, ftype='fir')

    # Новая частота дискретизации после децимации
    Fs_new = Fs / M

    # Интерполяция (восстановление сигнала)
    # Используем resample для изменения числа точек
    reconstructed_signal = resample(decimated_signal, len(signal))

    # Вычисляем ошибку между исходным и восстановленным сигналом
    error = compute_error(signal, reconstructed_signal)
    errors.append(error)

    # Вывод для каждого f
    print(f"f = {f} Гц, Ошибка = {error:.4f}")

# Визуализация ошибок
plt.plot(frequencies, errors, marker='o')
plt.xlabel('Частота сигнала (Гц)')
plt.ylabel('Отношение ошибки')
plt.title('Ошибка восстановления сигнала в зависимости от частоты')
plt.grid(True)
plt.show()


'''
- При низких частотах (значительно ниже половины новой частоты дискретизации после дециматора) ошибка будет очень маленькой, так как альясинг практически отсутствует, и интерполяция успешно восстанавливает сигнал.
- При приближении к половине частоты дискретизации (крайней границе, где возможен альясинг), ошибка начинает расти, так как искажения становятся заметными.
- При частотах выше половины частоты дискретизации (недопустимых для данного сигнала) возникает сильный альясинг, и восстановление сигнала становится невозможным, что приводит к значительной ошибке.
'''
