# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 13:03:07 2025

@author: Анна
"""
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.datasets import co2, sunspots

# Загрузка данных (примеры: CO2 и Sunspots)
data_co2 = co2.load_pandas().data
data_sunspots = sunspots.load_pandas().data

# Если есть пропуски, можно интерполировать или заполнить средним
data_co2 = data_co2.fillna(data_co2.mean())

# Построение графиков
plt.figure(figsize=(12, 6))

# График CO2
plt.subplot(2, 1, 1)
plt.plot(data_co2.index, data_co2['co2'], label='CO2 Concentration', color='blue')
plt.title('Динамика концентрации CO2')
plt.xlabel('Год')
plt.ylabel('Концентрация (ppm)')
plt.legend()
plt.grid()

# График солнечных пятен
plt.subplot(2, 1, 2)
plt.plot(data_sunspots['YEAR'], data_sunspots['SUNACTIVITY'], label='Sunspots', color='red')
plt.title('Динамика солнечной активности')
plt.xlabel('Год')
plt.ylabel('Количество пятен')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()