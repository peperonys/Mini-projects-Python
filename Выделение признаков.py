"""
Выделение признаков
"""

from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
import numpy as np
import tenserly as tl 

# Предположим, у нас есть тензор данных shape (n_samples, n_features, n_time)
data_tensor = np.random.random((100, 50, 10))

# Развернем тензор в матрицу
unfolded = tl.unfold(data_tensor, mode=0)

# Применим SVD для снижения размерности
svd = TruncatedSVD(n_components=10)
features = svd.fit_transform(unfolded)

# Используем полученные признаки для кластеризации
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(features)

print(f"Форма признаков: {features.shape}")
print(f"Кластеры: {clusters}")

