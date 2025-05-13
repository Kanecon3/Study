#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
シンプルな分類のサンプル
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

## シンプルなデータを生成
# 特徴量（説明変数）: [身長(cm), 体重(kg)]
# ラベル（目的変数）: 0: 痩せ型, 1: 普通, 2: 肥満
body_measurements = np.array([
    [160, 45],  # 痩せ型
    [165, 50],
    [170, 55],
    [175, 60],  # 普通
    [170, 65],
    [165, 70],
    [180, 75],  # 肥満
    [175, 80],
    [170, 85]
])
body_types = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])

## 決定木分類器の作成と学習
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(body_measurements, body_types)

## 予測
target_person = np.array([[170, 60]])  # 身長170cm、体重60kgの人
predicted_type = model.predict(target_person)[0]
type_names = ['痩せ型', '普通', '肥満']

print("=== 予測結果 ===")
print(f"身長: {target_person[0][0]}cm, 体重: {target_person[0][1]}kg")
print(f"体型の予測: {type_names[predicted_type]}")

## グラフの描画
plt.rcParams['font.family'] = 'MS Gothic'  # Windowsの場合の日本語フォントの設定
plt.figure(figsize=(8, 6))
colors = ['blue', 'green', 'red']
for i in range(3):
    plt.scatter(body_measurements[body_types == i, 0], 
                body_measurements[body_types == i, 1], 
                color=colors[i], label=type_names[i])
plt.scatter(target_person[0][0], target_person[0][1], 
           color='black', s=200, marker='*', label='予測対象')
plt.title('身長と体重による体型分類')
plt.xlabel('身長 (cm)')
plt.ylabel('体重 (kg)')
plt.grid(True)
plt.legend()
plt.savefig('body_type.png')
plt.show()
