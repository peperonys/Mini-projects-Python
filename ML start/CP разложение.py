#запускать в колабе https://colab.research.google.com/drive/1tqmca9FwAs43m3gEGU04eN21cTW0xpAE?usp=sharing
import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac

# Создаем случайный тензор
tensor = np.random.random((10, 20, 30))

# Выполняем CP-разложение
rank = 5
factors = parafac(tensor, rank=rank)

# Восстанавливаем тензор из факторов
reconstructed_tensor = tl.cp_to_tensor(factors)

# Проверяем ошибку реконструкции
error = np.linalg.norm(tensor - reconstructed_tensor)
print(f"Ошибка реконструкции: {error}")