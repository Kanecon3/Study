
# cmake サンプル1 README

cmakeの簡単なサンプルです。

## 目次

- [cmake サンプル1 README](#cmake-サンプル1-readme)
  - [目次](#目次)
  - [cmakeの実行](#cmakeの実行)
    - [方法1](#方法1)
    - [方法2](#方法2)

## cmakeの実行

### 方法1

準備：

```
mkdir build
cd build
```

構成の生成：

```
// buildフォルダで実行する
cmake ..
```

ビルド：

```
// buildフォルダで実行する
cmake --build .
```

### 方法2

buildフォルダ生成と構成の生成：

```
cmake -Bbuild -H.
```

ビルド：

```
cmake --build build
```
