cmake_minimum_required(VERSION 3.23)

project(Chess)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(Qt6_DIR "~/Qt/6.11.2/gcc_64/lib/cmake/Qt6")

find_package(Qt6 REQUIRED COMPONENTS Widgets)

qt_standard_project_setup()

qt_add_executable(Chess
  chess.cpp
)

target_link_libraries(Chess PRIVATE Qt6::Widgets)

set_target_properties(Chess PROPERTIES
  WIN32_EXECUTABLE ON
  MACOSX_BUNDLE ON
)
