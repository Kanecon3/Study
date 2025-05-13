# 概要

業務で Python を最近触りだしてみているので、Python のユニットテストをやってみました。  

ユニットテスト用のフレームワークはいくつかあるようなのですが、今回は標準の `unittest` を使って試してみました。  
なお、このドキュメントの内容は 2024/08/19 に試しています。  

# 環境

Ubuntu 20.04  
Python 3.8

# コード

階層構造：
```
Test1
├── calculator
│   └── calculator1.py
└── tests
    └── test_calculator.py
```

calculator1.py  
テスト対象のクラスとします：
```
class Calculator1:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("The divisor must be a non-zero number.")
        return a / b
```

test_calculator.py  
テストコード：
```
import unittest
import sys
import os

# calculator モジュールへのパスを追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator.calculator1 import Calculator1

class TestCalculator(unittest.TestCase):
    """
    TestCaseを継承したユニットテスト用のクラス
    """

    @classmethod
    def setUpClass(cls):
        """
        テストクラスが初期化される際に一度だけ呼ばれる
        """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """
        テストクラスが解放される際に一度だけ呼ばれる
        """
        print("tearDownClass")

    def setUp(self):
        """
        テストメソッドを実行するたびに呼ばれる
        """
        print("setUp")
        self.calc = Calculator1()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-1, 1), -1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

# NOTE: python -m unittest で実行する場合は下記は必要ない
if __name__ == '__main__':
    unittest.main()
```

# 実行

テストコードの場所に移動します。  
```
$ cd Test1/tests
```

実行します。  
```
$ python -m unittest
```
エラーが無ければ成功です！  

なお  
```
if __name__ == '__main__':
    unittest.main()
```
が書いてある場合は下記でも実行できます。  
```
$ python test_calculator.py
```

# お約束

- テストコードのファイル名にはプレフィックスで `test_` を付ける
- テストコードのメソッドにもプレフィックスで `test_` を付ける
- テストコードを格納するディレクトリ名は `tests` にする

