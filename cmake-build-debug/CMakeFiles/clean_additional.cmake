# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\vc418_client_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\vc418_client_autogen.dir\\ParseCache.txt"
  "vc418_client_autogen"
  )
endif()
