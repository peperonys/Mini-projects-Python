"""
Разложение Таккера
"""

from tensorly.decomposition import tucker

# Выполняем Tucker-разложение
ranks = [5, 5, 5]
core, factors = tucker(tensor, rank=ranks)

# Восстанавливаем тензор
reconstructed_tensor = tl.tucker_to_tensor((core, factors))

error = np.linalg.norm(tensor - reconstructed_tensor)
print(f"Ошибка реконструкции: {error}")

