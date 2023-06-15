"""
    This script will create a development environment
	
	NGX (Nana) C++ Library (https://nana-ngx.com)
	(C) Copyright 2023 Moxibyte GmbH

	Distributed under the Boost Software License, Version 1.0.
	See accompanying LICENSE file
"""

import os
import sys
import json
import zipfile
import tarfile
import subprocess
import urllib.request

def GetCodepage():
    return "".join(filter(str.isalnum, subprocess.getoutput('chcp').split(':')[-1].strip()))
    
def FindLatestVisualStudio():
    vswhere = os.getenv('programfiles(x86)') + '\\Microsoft Visual Studio\\Installer\\vswhere.exe'
    out = subprocess.check_output((vswhere, '-latest', '-nocolor', '-format', 'json'))
    return json.loads(out.decode(f'cp{GetCodepage()}'))

def GetVisualStudioYearNumber(vswhere):
    installationVersion = vswhere[0]['installationVersion'].split('.')[0]
    if installationVersion == '17':
        return '2022'
    if installationVersion == '16':
        return '2019'
    if installationVersion == '15':
        return '2017'

def GetVisualStudioPath(vswhere):
    return vswhere[0]['installationPath']

def GetExecutable(exe):
    if sys.platform.startswith('linux'):
        return exe
    else:
        return f'{exe}.exe'

def GetPremakeGenerator():
    if sys.platform.startswith('linux'):
        return 'gmake2'
    else:
        vswhere = FindLatestVisualStudio()
        vsversion = GetVisualStudioYearNumber(vswhere)
        return f'vs{vsversion}'

def GetPremakeDownloadUrl(version):
    baseUrl = f'https://github.com/premake/premake-core/releases/download/v{version}/premake-{version}'
    if sys.platform.startswith('linux'):
        return baseUrl + '-linux.tar.gz'
    else:
        return baseUrl + '-windows.zip'

def DownloadPremake(version = '5.0.0-beta2'):
    premakeDownloadUrl = GetPremakeDownloadUrl(version)
    premakeTargetFolder = './install-dev/premake5'
    premakeTargetZip = f'{premakeTargetFolder}/premake5.tmp'
    premakeTargetExe = f'{premakeTargetFolder}/{GetExecutable("premake5")}'

    if not os.path.exists(premakeTargetExe):
        print('Downloading premake5...')
        os.makedirs(premakeTargetFolder, exist_ok=True)
        urllib.request.urlretrieve(premakeDownloadUrl, premakeTargetZip)

        if premakeDownloadUrl.endswith('zip'):
            with zipfile.ZipFile(premakeTargetZip, 'r') as zipFile:
                zipFile.extract('premake5.exe', premakeTargetFolder)
        else:
            with tarfile.open(premakeTargetZip, 'r') as tarFile:
                tarFile.extract('./premake5', premakeTargetFolder)

def ConanBuild(conf):
    subprocess.run((
        "conan", "install", 

        "--requires", "libjpeg/9e",
        "--requires", "libpng/1.6.39",

        "-b", "missing",
        "-g", "PremakeDeps",
        "-d", "full_deploy",
        "-of", "./install-dev",

        "-s", f"build_type={conf}",
        "-s", "compiler.cppstd=17",
    ))

if __name__ == "__main__":
     # Download tool applications
    DownloadPremake()

    # Generate conan project
    ConanBuild('Debug')
    ConanBuild('Release')

    # Run premake5
    premakeGenerator = GetPremakeGenerator()
    subprocess.run(('./install-dev/premake5/premake5', '--file=./scripts/devenv.d/premake5.lua', premakeGenerator))
