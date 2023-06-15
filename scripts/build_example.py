"""
    Script for building one specific example using CMake
    
	NGX (Nana) C++ Library (https://nana-ngx.com)
	(C) Copyright 2023 Moxibyte GmbH

	Distributed under the Boost Software License, Version 1.0.
	See accompanying LICENSE file
"""

import os.path
import subprocess
import sys

if __name__ == "__main__":
    # Select example
    if(len(sys.argv) < 2):
        print("Please specify the example to be build!")
        exit()
    example = sys.argv[1]

    # Check if example exists
    source_dir = f"./examples/{example}/"
    if not os.path.exists(source_dir):
        print(f"Example '{example}' not found!")
        exit()
    
    # Create build directory
    build_dir = f"{source_dir}build/"
    os.makedirs(build_dir, exist_ok=True)

    # Generate cmake files
    subprocess.run((
        "cmake", 
        "-G", "Visual Studio 17 2022",
        "-A", "x64",
        "-DCMAKE_TOOLCHAIN_FILE=../../install/conan_toolchain.cmake",
        "-DCMAKE_BUILD_TYPE=Release",
        "-B", build_dir,
        "-S", source_dir,
    ))

    # Build with cmake
    subprocess.run((
        "cmake", 
        "--build",
        build_dir,
        "--config", "Release",
    ))
