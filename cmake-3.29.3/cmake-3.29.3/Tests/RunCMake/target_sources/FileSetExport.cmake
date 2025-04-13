enable_language(C)

add_library(lib1 STATIC lib1.c)
target_sources(lib1
  PUBLIC FILE_SET HEADERS BASE_DIRS ${CMAKE_CURRENT_SOURCE_DIR} FILES error.c
  PRIVATE FILE_SET a TYPE HEADERS BASE_DIRS ${CMAKE_CURRENT_SOURCE_DIR} FILES h1.h
  PUBLIC FILE_SET b TYPE HEADERS BASE_DIRS ${CMAKE_CURRENT_SOURCE_DIR} FILES h2.h
  INTERFACE FILE_SET c TYPE HEADERS BASE_DIRS "$<1:${CMAKE_CURRENT_SOURCE_DIR}/dir>" FILES "$<1:dir/dir.h>"
  INTERFACE FILE_SET d TYPE HEADERS BASE_DIRS FILES "${CMAKE_CURRENT_SOURCE_DIR}/$<IF:$<CONFIG:Debug>,debug,release>/empty.h"
  INTERFACE FILE_SET e TYPE HEADERS BASE_DIRS "${CMAKE_CURRENT_SOURCE_DIR}/$<IF:$<CONFIG:Debug>,debug,release>" FILES "${CMAKE_CURRENT_SOURCE_DIR}/$<IF:$<CONFIG:Debug>,debug,release>/empty2.h"
  INTERFACE FILE_SET f TYPE HEADERS BASE_DIRS "${CMAKE_CURRENT_SOURCE_DIR}" FILES "${CMAKE_CURRENT_SOURCE_DIR}/empty3.h"
  INTERFACE FILE_SET g TYPE HEADERS BASE_DIRS "${CMAKE_CURRENT_SOURCE_DIR}/dir1" "${CMAKE_CURRENT_SOURCE_DIR}/dir2" FILES "${CMAKE_CURRENT_SOURCE_DIR}/dir1/file1.h" "${CMAKE_CURRENT_SOURCE_DIR}/dir2/file2.h"
  INTERFACE FILE_SET dir3 TYPE HEADERS BASE_DIRS "${CMAKE_CURRENT_SOURCE_DIR}/dir3" FILES dir3/dir3.h
  )

install(TARGETS lib1 EXPORT export FILE_SET HEADERS FILE_SET a FILE_SET b FILE_SET c DESTINATION include/dir FILE_SET d FILE_SET e FILE_SET f DESTINATION include/$<IF:$<CONFIG:Debug>,debug,release> FILE_SET g FILE_SET dir3 DESTINATION include/dir3)
install(EXPORT export FILE export.cmake NAMESPACE install:: DESTINATION lib/cmake)
export(EXPORT export FILE export.cmake NAMESPACE export::)

add_library(lib2 STATIC lib2.c)
target_link_libraries(lib2 PRIVATE lib1)
