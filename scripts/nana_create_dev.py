"""
This script will create the "nana/dev" package with
"""

import subprocess
import shutil

if __name__ == "__main__":
    # Copy the license for package creation
    shutil.copyfile("./LICENSE", "./nana/LICENSE")

    # Create the package
    subprocess.run((
        "conan", "create", "./nana", 
        "-o", "nana/*:enable_jpeg=True",
        "-o", "nana/*:enable_png=True",
        "-o", "nana/*:enable_audio=True", 

        "-s", "build_type=Release",
        "-s", "compiler.cppstd=17",
    ))

    # Install the package locally with full_deploy for consumption via examples.
    subprocess.run((
        "conan", "install", 
        "--requires", "nana/dev",

        "-b", "missing",
        "-g", "CMakeDeps",
        "-d", "full_deploy",
        "-of", "./install",

        "-o", "nana/*:enable_jpeg=True",
        "-o", "nana/*:enable_png=True",
        "-o", "nana/*:enable_audio=True", 

        "-s", "build_type=Release",
        "-s", "compiler.cppstd=17",
    ))
