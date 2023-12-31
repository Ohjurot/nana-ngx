"""
    Runs one example with properly setup execution dirs (CMake)
    
	NGX (Nana) C++ Library (https://nana-ngx.com)
	(C) Copyright 2023 Moxibyte GmbH

	Distributed under the Boost Software License, Version 1.0.
	See accompanying LICENSE file
"""

import sys
import os.path
import subprocess

if __name__ == "__main__":
    # Select example
    if(len(sys.argv) < 2):
        print("Please specify the example to be build!")
        exit()
    example = sys.argv[1]

    # Check if example exists
    example_dir = f"./examples/{example}/"
    if not os.path.exists(example_dir):
        print(f"Example '{example}' not found!")
        exit()

    # Run example
    exe_path = f"{example_dir}build/Release/{example}.exe"
    if os.path.exists(exe_path):
        subprocess.run(args=(exe_path), cwd="./examples")
    else:
        print(f"The example '{example}' has not been build yet! Please run 'python ./scripts/build_example.py {example}'")

