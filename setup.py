#!/usr/bin/python3

import os
import platform
from setuptools import setup
from setuptools.extension import Extension

source_files = [os.path.join("src", x) for x in os.listdir("src") if x.lower().endswith(".cpp")]

extra_compile_args = []
extra_link_args = []

if platform.python_compiler().startswith('MSC '):
    extra_compile_args.append("/std:c++17")
    extra_compile_args.append("/D_SILENCE_CXX17_CODECVT_HEADER_DEPRECATION_WARNING")
else:
    extra_compile_args.append("-std=c++17")

setup(name="ccscript",
    version="1.500",
    description="ccscript",
    url="http://starmen.net/pkhack/ccscript",
    ext_modules=[
        Extension("ccscript",
                  source_files,
                  language="c++",
                  extra_compile_args=extra_compile_args,
                  extra_link_args=extra_link_args
                  )
    ])
