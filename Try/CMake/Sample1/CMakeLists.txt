# cmakeの最低バージョン
cmake_minimum_required(VERSION 3.1)

# プロジェクト名 言語
project(Sample1 CXX)

# 実行ファイル名 コンパイルするファイル
# NOTE:最低限この項目があればcmakeできるっぽい
add_executable(main_app main.cpp)
