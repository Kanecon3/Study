#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
シンプルな線形回帰のサンプル
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

## シンプルなデータを生成

# 特徴量（説明変数）: 生徒の勉強時間（時間）
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
# ラベル（目的変数）: テストの点数（点）
test_scores = np.array([30, 45, 60, 75, 90, 100, 95, 85, 80, 70])

# 線形回帰モデルの作成と学習
model = LinearRegression()
model.fit(study_hours, test_scores)

## 学習結果の表示
print("=== 学習結果 ===")
print(f"傾き（勉強時間1時間あたりの点数上昇）: {model.coef_[0]:.1f}点")
print(f"切片（勉強時間0時間の時の点数）: {model.intercept_:.1f}点")

## 予測
target_study_hours = 5.5  # 5時間30分勉強した場合
predicted_score = model.predict([[target_study_hours]])[0]
print(f"\n=== 予測 ===")
print(f"勉強時間 {target_study_hours}時間の場合の予測点数: {predicted_score:.1f}点")

## グラフの描画
plt.rcParams['font.family'] = 'MS Gothic'  # Windowsの場合の日本語フォントの設定
plt.figure(figsize=(8, 6))
plt.scatter(study_hours, test_scores, color='blue', label='実際のデータ')
plt.plot(study_hours, model.predict(study_hours), color='red', label='予測直線')
plt.scatter(target_study_hours, predicted_score, color='green', s=100, label='予測値')
plt.title('勉強時間とテストの点数の関係')
plt.xlabel('勉強時間（時間）')
plt.ylabel('テストの点数（点）')
plt.grid(True)
plt.legend()
plt.savefig('study_score.png')
plt.show()
