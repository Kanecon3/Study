# CMakeコマンドリファレンス

このドキュメントのCMakeの最低バージョンは 3.22 とします。

## 目次 <!-- omit in toc -->

- [cmake\_minimum\_required](#cmake_minimum_required)
- [project](#project)
- [add\_executable](#add_executable)
- [add\_library](#add_library)
- [target\_link\_libraries](#target_link_libraries)
- [find\_package](#find_package)
- [set](#set)
- [target\_include\_directories](#target_include_directories)
- [target\_compile\_definitions](#target_compile_definitions)
- [option](#option)
- [if/elseif/endif](#ifelseifendif)
- [add\_subdirectory](#add_subdirectory)
- [message](#message)
- [add\_custom\_command](#add_custom_command)
- [cmake\_policy](#cmake_policy)
- [configure\_file](#configure_file)
- [set\_property](#set_property)

## cmake_minimum_required

**基本構文**:

```cmake
cmake_minimum_required(VERSION major.minor[.patch[.tweak]])
```

**主な用途**:

- 必要なCMakeの最小バージョンを指定
- これより古いバージョンでの実行を防ぐ

**使用例**:

```cmake
cmake_minimum_required(VERSION 3.22)
```

## project

**基本構文**:

```cmake
project(ProjectName 
        [VERSION major[.minor[.patch[.tweak]]]]
        [LANGUAGES languages...])
```

**主な用途**:

- プロジェクト名の設定
- プロジェクトのバージョン設定
- 使用する言語の指定

**使用例**:

```cmake
project(myapp VERSION 1.17.0 LANGUAGES CXX)
```

**変数**:

`project`コマンドを実行すると、以下の変数が自動的に設定されます：

- `${PROJECT_NAME}` - 設定したプロジェクト名
- `${PROJECT_VERSION}` - プロジェクトのバージョン（設定した場合）
- `${PROJECT_VERSION_MAJOR}` - メジャーバージョン
- `${PROJECT_VERSION_MINOR}` - マイナーバージョン
- `${PROJECT_VERSION_PATCH}` - パッチバージョン
- `${PROJECT_VERSION_TWEAK}` - トゥイークバージョン

**使用例**:

```cmake
project(myapp VERSION 1.17.0 LANGUAGES CXX)
message(STATUS "Building ${PROJECT_NAME} version ${PROJECT_VERSION}")
```

## add_executable

**基本構文**:

```cmake
add_executable(<name> [WIN32] [MACOSX_BUNDLE]
              [EXCLUDE_FROM_ALL]
              [source1] [source2 ...])
```

**主な用途**:

- 実行可能ファイルのターゲットを作成
- ソースファイルとターゲットの関連付け

**使用例**:

```cmake
add_executable(myapp main.cpp)
```

```cmake
add_executable(${PROJECT_NAME} WIN32 main.cpp)
```

## add_library

**基本構文**:

```cmake
add_library(<name> [STATIC | SHARED | MODULE]
           [EXCLUDE_FROM_ALL]
           [source1] [source2 ...])
```

**主な用途**:

- ライブラリターゲットの作成
- 静的/動的ライブラリの生成

**使用例**:

```cmake
add_library(mylib STATIC source1.cpp source2.cpp)
```

```cmake
add_library(mylib SHARED source1.cpp source2.cpp)
```

## target_link_libraries

**基本構文**:

```cmake
target_link_libraries(<target>
                     <PRIVATE|PUBLIC|INTERFACE> <item>...
                     [<PRIVATE|PUBLIC|INTERFACE> <item>...]...)
```

**主な用途**:

- ターゲットとライブラリの依存関係設定
- リンクするライブラリの指定

**使用例**:

```cmake
target_link_libraries(myapp PRIVATE mylib)
```

```cmake
target_link_libraries(myapp 
    PRIVATE
        OpenGL::GL
        SDL2::SDL2
)
```

## find_package

**基本構文**:

```cmake
find_package(<PackageName> [version] [EXACT] [QUIET] [MODULE]
             [REQUIRED] [[COMPONENTS] [components...]]
             [OPTIONAL_COMPONENTS components...]
             [NO_POLICY_SCOPE])
```

**主な用途**:

- 外部パッケージ/ライブラリの検索
- 依存関係の解決

**使用例**:

```cmake
find_package(OpenGL REQUIRED)
```

```cmake
find_package(Qt5 COMPONENTS Core Widgets REQUIRED)
```

## set

**基本構文**:

```cmake
set(variable value... [CACHE type docstring [FORCE]])
```

**主な用途**:

- 変数の定義と値の設定
- キャッシュ変数の設定
- コンパイラフラグの設定

**使用例**:

```cmake
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(SOURCE_FILES main.cpp helper.cpp)
set(DEBUG_MODE ON CACHE BOOL "Enable debug mode")
```

## target_include_directories

**基本構文**:

```cmake
target_include_directories(<target> [SYSTEM] [BEFORE]
                         <PRIVATE|PUBLIC|INTERFACE> [items1...]
                         [<PRIVATE|PUBLIC|INTERFACE> [items2...] ...])
```

**主な用途**:

- ターゲット固有のインクルードディレクトリ設定
- ヘッダーファイルの検索パス指定

**使用例**:

```cmake
target_include_directories(myapp PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${CMAKE_CURRENT_BINARY_DIR}
)
```

## target_compile_definitions

**基本構文**:

```cmake
target_compile_definitions(<target>
                         <PRIVATE|PUBLIC|INTERFACE> [items1...]
                         [<PRIVATE|PUBLIC|INTERFACE> [items2...] ...])
```

**主な用途**:

- ターゲット固有のプリプロセッサマクロ定義
- スコープ付きのコンパイル定義

**使用例**:

```cmake
target_compile_definitions(myapp PRIVATE DEBUG=1)
```

```cmake
target_compile_definitions(mylib PUBLIC API_EXPORT)
```

## option

**基本構文**:

```cmake
option(OPTION_NAME "Description" [initial value])
```

**主な用途**:

- ブール値オプションの定義
- ビルド設定のカスタマイズ

**使用例**:

```cmake
option(BUILD_TESTS "Build test programs" OFF)
```

```cmake
option(USE_OPENGL "Use OpenGL renderer" ON)
```

## if/elseif/endif

**基本構文**:

```cmake
if(condition)
    # commands
elseif(condition)
    # commands
else()
    # commands
endif()
```

**主な用途**:

- 条件分岐の制御
- プラットフォーム固有の設定

**使用例**:

```cmake
if(MSVC)
    add_definitions(/W4)
elseif(UNIX)
    add_definitions(-Wall)
endif()
```

## add_subdirectory

**基本構文**:

```cmake
add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL])
```

**主な用途**:

- サブディレクトリのCMakeListsを処理
- プロジェクトの階層構造の構築

**使用例**:

```cmake
add_subdirectory(src)
add_subdirectory(tests EXCLUDE_FROM_ALL)
```

## message

**基本構文**:

```cmake
message([<mode>] "message text" ...)
```

**主な用途**:

- ビルド時のメッセージ表示
- デバッグ情報の出力

**使用例**:

```cmake
message(STATUS "Configuring project...")
message(WARNING "Deprecated feature used")
```

## add_custom_command

**基本構文**:

```cmake
add_custom_command(TARGET <target>
                  PRE_BUILD | PRE_LINK | POST_BUILD
                  COMMAND command1 [ARGS] [args1...]
                  [COMMAND command2 [ARGS] [args2...] ...]
                  [WORKING_DIRECTORY dir]
                  [COMMENT comment] [VERBATIM])
```

**主な用途**:

- ビルドプロセス中のカスタムコマンド実行
- ファイルのコピーや生成

**使用例**:

```cmake
add_custom_command(
    TARGET myapp POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy 
            ${CMAKE_SOURCE_DIR}/config.ini
            ${CMAKE_BINARY_DIR}/config.ini
)
```

## cmake_policy

**基本構文**:

```cmake
cmake_policy(SET CMP<NNNN> NEW|OLD)
```

```cmake
cmake_policy(VERSION major[.minor[.patch[.tweak]]])
```

**主な用途**:

- CMakeポリシーの設定
- 特定のCMakeバージョンのポリシー設定の適用

**使用例**:

```cmake
cmake_policy(SET CMP0079 NEW)
cmake_policy(VERSION 3.22)
```

## configure_file

**基本構文**:

```cmake
configure_file(input output
              [COPYONLY] [ESCAPE_QUOTES] [@ONLY])
```

**主な用途**:

- テンプレートファイルから設定ファイルを生成
- バージョン情報などの動的な値の埋め込み

**使用例**:

```cmake
configure_file(
    "${PROJECT_SOURCE_DIR}/config.h.in"
    "${PROJECT_BINARY_DIR}/config.h"
)
```

## set_property

**基本構文**:

```cmake
set_property(TARGET targets...
            PROPERTY property value...)
```

**主な用途**:

- ターゲットのプロパティ設定
- グローバルプロパティの設定

**使用例**:

```cmake
set_property(GLOBAL PROPERTY USE_FOLDERS ON)
```

```cmake
set_property(TARGET mylib PROPERTY VERSION 1.0)
```
