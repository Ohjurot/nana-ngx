cmake_minimum_required(VERSION 3.15)
project(01_HelloWorld CXX)

find_package(NANA REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} nana::nana)
