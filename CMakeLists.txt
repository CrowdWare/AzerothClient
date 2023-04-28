cmake_minimum_required(VERSION 3.4...3.18)
project(azerothlib)

add_library(mymath STATIC lib/mymath.cpp lib/calculator.cpp)
set_target_properties(mymath PROPERTIES POSITION_INDEPENDENT_CODE ON)

add_subdirectory(pybind11)
pybind11_add_module(azerothlib bind/binder.cpp)
target_link_libraries(azerothlib PRIVATE mymath)
