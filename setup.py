#!/usr/bin/python3

import os
from distutils.ccompiler import get_default_compiler
from setuptools import setup
from setuptools.command.build_ext import build_ext
from setuptools.extension import Extension

source_files = [os.path.join("src", x) for x in os.listdir("src") if x.lower().endswith(".cpp")]

# As of July 2026, setuptools doesn't seem to include its own method to add compiler flags dependent
# on the specific compiler (I legitimately don't understand how extra_compile_args is supposed to
# work normally). But it does provide distutils' interface for checking what the compiler is, which
# should work in a stable way until they add their own way.
# See https://setuptools.pypa.io/en/latest/userguide/interfaces.html for info on stability tiers.
# See https://setuptools.pypa.io/en/latest/userguide/extension.html for the recommendation to
# inherit from existing commands to augment build functionality.
# See https://github.com/pypa/setuptools/issues/2806 for people asking for an upgrade path for many
# things related to creating and detecting compilers.
# Especially this comment: https://github.com/pypa/setuptools/issues/2806#issuecomment-1367674526
class build_ext_with_compiler_flags(build_ext):
    def finalize_options(self):
        super().finalize_options()

        extra_compile_args = []
        extra_link_args = []
        
        compiler_type = None
        if self.compiler is None:
            compiler_type = get_default_compiler()
        else:
            compiler_type = self.compiler

        if compiler_type == 'msvc':
            extra_compile_args.append('/std:c++17')
            extra_compile_args.append('/D_SILENCE_CXX17_CODECVT_HEADER_DEPRECATION_WARNING')
        else:
            extra_compile_args.append('-std=c++11')
        
        for ext in self.extensions:
            ext.extra_compile_args.extend(extra_compile_args)
            ext.extra_link_args.extend(extra_link_args)

setup(name="ccscript",
    version="1.500",
    description="ccscript",
    url="http://starmen.net/pkhack/ccscript",
    ext_modules=[
        Extension("ccscript",
                  source_files,
                  language="c++"
                  )
    ],
    cmdclass={'build_ext': build_ext_with_compiler_flags}
    )