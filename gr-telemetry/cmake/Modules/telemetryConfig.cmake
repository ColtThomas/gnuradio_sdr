INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_TELEMETRY telemetry)

FIND_PATH(
    TELEMETRY_INCLUDE_DIRS
    NAMES telemetry/api.h
    HINTS $ENV{TELEMETRY_DIR}/include
        ${PC_TELEMETRY_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    TELEMETRY_LIBRARIES
    NAMES gnuradio-telemetry
    HINTS $ENV{TELEMETRY_DIR}/lib
        ${PC_TELEMETRY_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(TELEMETRY DEFAULT_MSG TELEMETRY_LIBRARIES TELEMETRY_INCLUDE_DIRS)
MARK_AS_ADVANCED(TELEMETRY_LIBRARIES TELEMETRY_INCLUDE_DIRS)

