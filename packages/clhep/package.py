# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
from spack.pkg.builtin.clhep import Clhep as ClhepSpack

class Clhep(ClhepSpack):
    version('2.1.3.1', sha256='5d3e45b39a861731fe3a532bb1426353bf62b54c7b90ecf268827e50f925642b')
    patch('clang-inline.patch', when='@2.1.3.1%clang')

    def cmake_args(self):
        args = super(ClhepSpack, self).cmake_args()
        args.append("-DCMAKE_MACOSX_RPATH=ON")
        return args
