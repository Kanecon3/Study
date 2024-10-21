cmake_minimum_required(VERSION 3.1)
project(mylib
    VERSION 1.0.0
    DESCRIPTION "library"
    LANGUAGES CXX)
add_library(Calculation STATIC src/Calculate1.cpp)
target_compile_features(Calculation PUBLIC cxx_std_11)
target_include_directories(Calculation PRIVATE include)
set_target_properties(Calculation
    PROPERTIES
    VERSION ${mylib_VERSION})

