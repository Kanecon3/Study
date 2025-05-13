# cmakeの最低バージョン
cmake_minimum_required(VERSION 3.1)

# プロジェクト名 言語
project(mylib CXX)

# 作成するライブラリ名(自動的に"Libライブラリ名"になる) 静的ライブラリ コンパイルするファイル
add_library(Calculation STATIC src/Calculate1.cpp)

# include
target_include_directories(Calculation PRIVATE include)
