# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Bayeux(CMakePackage):
    """SuperNEMO Core Data/Geometry/EventGen library
    """

    homepage = "https://github.com/SuperNEMO-DBD/Bayeux"
    url      = "https://github.com/SuperNEMO-DBD/Bayeux/archive/3.3.0.tar.gz"

    version('3.3.0', sha256='6468251da50214e744651260770bf252f677a8f9b9f822085c38dc69d71b52a9')
    version('3.1.2', sha256='2bf6b887e654fadbb7373fbea550ec14adc8836758fb029bf56c76bb5177827d')

    variant('cxxstd',
            default='11',
            values=('11', '14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    variant('geant4', default=False, description='Build mctools Geant4 module')
    variant('qt', default=False, description='Build datatools/variant browser')

    depends_on('cmake@3.3:', type='build')
    depends_on('boost@1.63:+icu')
    depends_on('camp@0.8.0')
    depends_on('clhep@2.1.3.1')
    depends_on('gsl@2.4:')
    depends_on('readline')
    depends_on('root@6.12:')

    # optional geant4/qt
    depends_on('geant4@:9.6 cxxstd=11', when='+geant4 cxxstd=11')
    depends_on('qt5base', when='+qt')



    def cmake_args(self):
        spec = self.spec
        args = [
            '-DBAYEUX_COMPILER_ERROR_ON_WARNING=OFF',
            '-DBAYEUX_ENABLE_TESTING=OFF',
            '-DBAYEUX_WITH_DOCS=OFF',
            '-DBAYEUX_CXX_STANDARD={0}'.format(spec.variants['cxxstd'].value)
            ]

        if spec.satisfies('+geant4'):
            args.append('-DBAYEUX_WITH_GEANT4_MODULE=ON')
        else:
            args.append('-DBAYEUX_WITH_GEANT4_MODULE=OFF')

        if spec.satisfies('+qt'):
            args.append('-DBAYEUX_WITH_QT_GUI=ON')
        else:
            args.append('-DBAYEUX_WITH_QT_GUI=OFF')

        return args
