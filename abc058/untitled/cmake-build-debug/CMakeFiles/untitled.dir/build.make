# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.7

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/e155755/Documents/Competitive_programming/Atcoder/AtCoder_Beginner_Contest_058/untitled

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/e155755/Documents/Competitive_programming/Atcoder/AtCoder_Beginner_Contest_058/untitled/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/untitled.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/untitled.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/untitled.dir/flags.make

CMakeFiles/untitled.dir/library.c.o: CMakeFiles/untitled.dir/flags.make
CMakeFiles/untitled.dir/library.c.o: ../library.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/e155755/Documents/Competitive_programming/Atcoder/AtCoder_Beginner_Contest_058/untitled/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/untitled.dir/library.c.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/untitled.dir/library.c.o   -c /Users/e155755/Documents/Competitive_programming/Atcoder/AtCoder_Beginner_Contest_058/untitled/library.c

CMakeFiles/untitled.dir/library.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/untitled.dir/library.c.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/e155755/Documents/Competitive_programming/Atcoder/AtCoder_Beginner_Contest_058/untitled/library.c > CMakeFiles/untitled.dir/library.c.i

CMakeFiles/untitled.dir/library.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/untitled.dir/library.c.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/e155755/Documents/Competitive_programming/Atcoder/AtCoder_Beginner_Contest_058/untitled/library.c -o CMakeFiles/untitled.dir/library.c.s

CMakeFiles/untitled.dir/library.c.o.requires:

.PHONY : CMakeFiles/untitled.dir/library.c.o.requires

CMakeFiles/untitled.dir/library.c.o.provides: CMakeFiles/untitled.dir/library.c.o.requires
	$(MAKE) -f CMakeFiles/untitled.dir/build.make CMakeFiles/untitled.dir/library.c.o.provides.build
.PHONY : CMakeFiles/untitled.dir/library.c.o.provides

CMakeFiles/untitled.dir/library.c.o.provides.build: CMakeFiles/untitled.dir/library.c.o


# Object files for target untitled
untitled_OBJECTS = \
"CMakeFiles/untitled.dir/library.c.o"

# External object files for target untitled
untitled_EXTERNAL_OBJECTS =

libuntitled.a: CMakeFiles/untitled.dir/library.c.o
libuntitled.a: CMakeFiles/untitled.dir/build.make
libuntitled.a: CMakeFiles/untitled.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/e155755/Documents/Competitive_programming/Atcoder/AtCoder_Beginner_Contest_058/untitled/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C static library libuntitled.a"
	$(CMAKE_COMMAND) -P CMakeFiles/untitled.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/untitled.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/untitled.dir/build: libuntitled.a

.PHONY : CMakeFiles/untitled.dir/build

CMakeFiles/untitled.dir/requires: CMakeFiles/untitled.dir/library.c.o.requires

.PHONY : CMakeFiles/untitled.dir/requires

CMakeFiles/untitled.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/untitled.dir/cmake_clean.cmake
.PHONY : CMakeFiles/untitled.dir/clean

CMakeFiles/untitled.dir/depend:
	cd /Users/e155755/Documents/Competitive_programming/Atcoder/AtCoder_Beginner_Contest_058/untitled/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/e155755/Documents/Competitive_programming/Atcoder/AtCoder_Beginner_Contest_058/untitled /Users/e155755/Documents/Competitive_programming/Atcoder/AtCoder_Beginner_Contest_058/untitled /Users/e155755/Documents/Competitive_programming/Atcoder/AtCoder_Beginner_Contest_058/untitled/cmake-build-debug /Users/e155755/Documents/Competitive_programming/Atcoder/AtCoder_Beginner_Contest_058/untitled/cmake-build-debug /Users/e155755/Documents/Competitive_programming/Atcoder/AtCoder_Beginner_Contest_058/untitled/cmake-build-debug/CMakeFiles/untitled.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/untitled.dir/depend
