cmake_minimum_required(VERSION 3.4...3.18)
project(azerothlib_wrapper)

add_library(mymath STATIC lib/mymath.cpp lib/calculator.cpp)
set_target_properties(mymath PROPERTIES POSITION_INDEPENDENT_CODE ON)
add_subdirectory(AzerothLib)
add_subdirectory(pybind11)
pybind11_add_module(azerothlib_wrapper bind/binder.cpp)
target_link_libraries(azerothlib_wrapper PRIVATE mymath)
