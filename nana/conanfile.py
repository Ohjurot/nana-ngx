"""
CONANFILE NOT TO BE PUBLISHED...

YES THIS IS UGLY MAINTAINING BOTH FILES BUT THIS ONE
SHALL NEVER BE PUBLISHED TO CONAN INDEX!

The conan index file is NOT tracked here! Visit the conan-center-index repo!

INFORMATION FOR LINUX USERS:
  Make sure to install xorg/system once as root! After that non root user will be able
  to use the lib / it's x11 dependencies!
  > conan install --requires=xorg/system -c tools.system.package_manager:mode=install
"""

from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.build import check_min_cppstd
from conan.tools.files import copy

import os.path

class NanaRecipe(ConanFile):
    name = "nana"
    version = "dev"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {
        # Conan CMake defaults
        "shared": [True, False], 
        "fPIC": [True, False],
        # Nana options
        "enable_audio": [True, False],
        "enable_jpeg": [True, False],
        "enable_png": [True, False],
    }
    default_options = {
        "shared": False, 
        "fPIC": True,
        "enable_audio": False,
        "enable_jpeg": False,
        "enable_png": False,
    }

    # Development sources are here
    exports_sources = "CMakeLists.txt", "LICENSE", "cmake/*", "source/*", "include/*"

    def validate(self):
        check_min_cppstd(self, "17")

    def requirements(self):
        # Linux requirements
        if self.settings.os == "Linux":
            self.requires("xorg/system")
            # libxft is not conan2 compatible... 
            # See: https://github.com/conan-io/conan-center-index/pull/17485
            self.requires("libxft/2.3.6") 

        # Option based requirements
        if self.options.enable_jpeg:
            self.requires("libjpeg/9e")
        if self.options.enable_png:
            self.requires("libpng/1.6.39")

    def build_requirements(self):
        self.build_requires("cmake/3.26.4")
        if self.settings.os == "Linux":
            self.tool_requires("pkgconf/1.9.3")

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()

        tc = CMakeToolchain(self)

        # Enable the use of the conan configuration header 
        # (required for all following options)
        tc.variables["NANA_CMAKE_ENABLE_CONF"] = True
        # Use os like include paths (but the libs will be provided by conan)
        tc.variables["NANA_CMAKE_LIBJPEG_FROM_OS"] = True
        tc.variables["NANA_CMAKE_LIBPNG_FROM_OS"] = True
        # Make cmake install work 
        tc.variables["NANA_CMAKE_INSTALL"] = True 

        # Set vars for optional features
        tc.variables["NANA_CMAKE_ENABLE_AUDIO"] = self.options.enable_audio
        tc.variables["NANA_CMAKE_ENABLE_JPEG"] = self.options.enable_jpeg
        tc.variables["NANA_CMAKE_ENABLE_PNG"] = self.options.enable_png
        
        # Static runtime for msvc
        compiler = self.settings.get_safe("compiler")
        if compiler and str(compiler).lower() == "msvc":
            compiler_runtime = self.settings.get_safe("compiler.runtime")
            tc.variables["MSVC_USE_STATIC_RUNTIME"] = (
                compiler_runtime != None and (compiler_runtime).lower() == "static"
                )
            
        # Shared lib (only set when enabled and on windows)
        if self.options.shared and self.settings.os == "Windows":
            tc.variables["CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS"] = True

        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        copy(self, "LICENSE", src=self.source_folder, dst=os.path.join(self.package_folder, "licenses"))

    def package_info(self):
        self.cpp_info.libs = ["nana"]

        # Add defines based on options
        if self.options.enable_audio:
            self.cpp_info.defines.append("NANA_ENABLE_AUDIO")
        if self.options.enable_jpeg:
            self.cpp_info.defines.extend(("NANA_ENABLE_JPEG", "USE_LIBJPEG_FROM_OS"))
        if self.options.enable_png:
            self.cpp_info.defines.extend(("NANA_ENABLE_PNG", "USE_LIBPNG_FROM_OS"))
