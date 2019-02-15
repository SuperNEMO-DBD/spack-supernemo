# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install camp
#
# You can edit this file again by typing:
#
#     spack edit camp
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Camp(CMakePackage):
    homepage = "https://github.com/drbenmorgan/camp"
    git      = "https://github.com/drbenmorgan/camp.git"

    version('0.8.0', commit="7564e57f7b406d1021290cf2260334d57d8df255")

    variant('cxxstd',
            default='11',
            values=('11', '14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('cmake@2.8.8:', type='build')
    depends_on('boost@1.63.0:')

    def cmake_args(self):
        cmake_args = ["-DCMAKE_MACOSX_RPATH=ON"]
        return cmake_args
