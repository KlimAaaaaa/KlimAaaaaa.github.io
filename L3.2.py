# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 13:03:07 2025

@author: Анна
"""
import matplotlib.pyplot as plt
from statsmodels.datasets import co2, sunspots

# Загрузка данных (примеры: CO2 и Sunspots)
data_co2 = co2.load_pandas().data
data_sunspots = sunspots.load_pandas().data

# Фильтрация CO2 (1958–1980)
co2_start = '1958-03-29'  # Первая дата в наборе CO2
co2_end = '1980-12-31'
data_co2_filtered = data_co2[co2_start:co2_end]

# Фильтрация солнечных пятен (1990–2008)
sunspots_start = 1990
sunspots_end = 2008
data_sunspots_filtered = data_sunspots[
    (data_sunspots['YEAR'] >= sunspots_start) & 
    (data_sunspots['YEAR'] <= sunspots_end)
]

# Построение графиков
plt.figure(figsize=(12, 6))

# График CO2
plt.subplot(2, 1, 1)
plt.plot(data_co2_filtered.index, data_co2_filtered['co2'], color='blue')
plt.title(f'Концентрация CO2 ({co2_start[:4]}–{co2_end[:4]})')
plt.xlabel('Год')
plt.ylabel('CO2 (ppm)')
plt.grid()

# График солнечных пятен
plt.subplot(2, 1, 2)
plt.plot(data_sunspots_filtered['YEAR'], data_sunspots_filtered['SUNACTIVITY'], color='red')
plt.title(f'Солнечная активность ({sunspots_start}–{sunspots_end})')
plt.xlabel('Год')
plt.ylabel('Число пятен')
plt.grid()

plt.tight_layout()
plt.show()