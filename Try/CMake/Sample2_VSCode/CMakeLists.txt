# cmakeの最低バージョン
cmake_minimum_required(VERSION 3.1)

# compile_commands.jsonを出力する
# NOTE:compile_commands.jsonをc_cpp_properties.jsonで設定するとインテリセンスの設定になる
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# プロジェクト名 言語
project(Sample2 CXX)

# ビルド対象にサブディレクトリを追加する
add_subdirectory(calculation)

# includeのパス
target_include_directories(Calculation INTERFACE calculation/include)

# 実行ファイル名 コンパイルするファイル
add_executable(main_app Main.cpp)

# リンクする際に使用するライブラリやフラグを指定
target_link_libraries(main_app Calculation)
