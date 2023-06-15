-- Premake5 script for creating a development enviroment
-- (Mainly intended to be used on windows to create a solution)
-- 
-- NGX (Nana) C++ Library (https://nana-ngx.com)
-- (C) Copyright 2023 Moxibyte GmbH
--
-- Distributed under the Boost Software License, Version 1.0.
-- See accompanying LICENSE file

include "../../install-dev/conandeps.premake5.lua"

-- Folder detection
function nana_is_windows()
    ds = package.config:sub(1,1)
    return ds == "\\"
end
function nana_discover_subfolders_win(folder)
    return io.popen("dir \"" .. folder .. "\" /b /ad"):lines()
end
function nana_discover_subfolders_linux(folder)
    return io.popen("find \"./" .. folder .. "\" -maxdepth 1 -type d -printf '%f\n'" ):lines()
end
function nana_discover_subfolders(folder)
    if nana_is_windows() then
        return nana_discover_subfolders_win(folder)
    else
        return nana_discover_subfolders_linux(folder)
    end
end

-- Default cpp setup
function nana_defaultsetup()
    language "C++"
    cppdialect "C++17" 

    flags { "MultiProcessorCompile" }

    targetdir "%{wks.location}/build-dev/%{cfg.architecture}-%{cfg.buildcfg}/bin/"
    objdir    "%{wks.location}/build-dev/%{cfg.architecture}-%{cfg.buildcfg}/obj/%{prj.name}/"

    defines {
        "NANA_ENABLE_AUDIO",
        "NANA_ENABLE_JPEG", "USE_LIBJPEG_FROM_OS",
        "NANA_ENABLE_PNG", "USE_LIBPNG_FROM_OS",
    }

    filter { "configurations:Debug" }
        defines { "DEBUG" }
        symbols "On"
    filter {}

    filter { "configurations:Release" }
        defines { "NDEBUG" }
        optimize "On"
    filter {}
end

-- Template for examples
function nana_example(folder)
    project(folder)
        nana_defaultsetup()

        location("../../examples/" .. folder .. "/")
        kind "ConsoleApp"

        debugdir "%{wks.location}/examples"

        files {
            "%{prj.location}/**.c", "%{prj.location}/**.cc", "%{prj.location}/**.cpp", "%{prj.location}/**.cxx",
            "%{prj.location}/**.h", "%{prj.location}/**.hh", "%{prj.location}/**.hpp", "%{prj.location}/**.hxx",
        }

        includedirs {
            "%{prj.location}",
            "%{wks.location}/nana/include",
        }

        links { "nana" }
        conan_setup()
end

-- Global configuration
workspace "nana"
    location "../../"

    architecture "x64"
    configurations { "Debug", "Release" }

-- Create nana as static lib
project "nana"
    nana_defaultsetup()

    location "../../nana"
    kind "StaticLib"

    files {
        "%{prj.location}/include/**",
        "%{prj.location}/source/**",
    }

    includedirs {
        "%{prj.location}/include/",
    }

    conan_setup_build()

-- We will now find all examples and add them as projects :-)
group "examples"
    for dir in nana_discover_subfolders("../../examples/")
    do
        nana_example(dir)
    end
group ""
