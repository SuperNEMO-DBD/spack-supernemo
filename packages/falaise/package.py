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
#     spack install falaise
#
# You can edit this file again by typing:
#
#     spack edit falaise
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Falaise(CMakePackage):
    """SuperNEMO simulation and reconstruction software
    """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/SuperNEMO-DBD/Falaise"
    url      = "https://github.com/SuperNEMO-DBD/Falaise/archive/v3.3.0.tar.gz"

    version('3.3.0', sha256='62ebadd9dab94297d727fe27ac0e2c5f64d657b77af2e785a329d4d5ee7733c2')

    variant('cxxstd',
            default='11',
            values=('11', '14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('cmake@3.3:', type='build')

    # Like before, just depend on Bayeux, see how it goes...
    for x in (11, 14, 17):
      depends_on('bayeux@3.3.0+qt+geant4 cxxstd={0}'.format(x), when='@3.3.0 cxxstd={0}'.format(x))

    def cmake_args(self):
        spec = self.spec
        args = [
            '-DFALAISE_COMPILER_ERROR_ON_WARNING=OFF',
            '-DFALAISE_WITH_DOCS=OFF',
            '-DFALAISE_CXX_STANDARD={0}'.format(spec.variants['cxxstd'].value)
            ]
        return args
