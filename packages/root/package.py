# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import sys


class Root(CMakePackage):
    """ROOT is a data analysis framework."""

    homepage = "https://root.cern.ch"
    url      = "https://root.cern/download/root_v6.14.00.source.tar.gz"

    # ###################### Versions ##########################

    # Master branch
    version('master', git="https://github.com/root-project/root.git",
        branch='master')

    # Production version
    version('6.16.00', sha256='2a45055c6091adaa72b977c512f84da8ef92723c30837c7e2643eecc9c5ce4d8', preferred=True)

    # ###################### Compiler variants ########################
    variant('cxxstd',
            default='11',
            values=('11', '14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('cmake@3.4.3:', type='build')
    depends_on('pkgconfig', type='build')

    # Always required deps
    depends_on('freetype')
    # Not on macOS? weird conflicts with system...
    #depends_on('libpng')
    depends_on('lz4',    when='@6.13.02:')
    depends_on('ncurses')
    depends_on('pcre')
    depends_on('intel-tbb')
    depends_on('xrootd')
    depends_on('xxhash', when='@6.13.02:')
    depends_on('xz')
    depends_on('zlib')

    # Components we need for SNemo
    depends_on('gsl')
    depends_on('libxml2')
    depends_on('openssl')
    depends_on('sqlite')
    depends_on('python@3: +shared', type=('build', 'run'))

    def cmake_args(self):
        options = []
        # Disable/Enable needed defaults and builtins
        options = [
            '-Ddavix=OFF',
            '-Dfftw3=OFF',
            '-Dfitsio=OFF',
            '-Dfortran=OFF',
            '-Dgfal=OFF',
            '-Dgviz=OFF',
            '-Dhdfs=OFF',
            '-Dmysql=OFF',
            '-Doracle=OFF',
            '-Dpgsql=OFF',
            '-Dpythia6=OFF',
            '-Dpythia8=OFF',
            '-Dpython=OFF',
            '-Dqt=OFF',
            '-Drfio=OFF',
            '-Dsqlite=OFF',
            '-Dssl=OFF',
            '-Dtmva-cpu=OFF',
            '-Dtmva-gpu=OFF',
            '-Dtmva-pymva=OFF',
            '-Dunuran=OFF',
            '-Dvdt=OFF'
            ]

        # Core and builtin things we want
        options.extend([
            '-Dcxx{0}=ON'.format(self.spec.variants['cxxstd'].value),
            '-Dexplicitlink=ON',
            '-Dsoversion=ON',
            '-Drpath=ON',
            '-Dshared=ON',
            '-Dfail-on-missing=ON',
            '-Dsqlite=ON',
            '-Dssl=ON',
            '-Dbuiltin_openssl=OFF',
            '-Dxrootd=ON',
            '-Dbuiltin_xrootd=OFF',
            '-Dtmva=ON',
            '-Dpython=ON',
            ])

        return options

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PYTHONPATH', self.prefix.lib)

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        spack_env.set('ROOTSYS', self.prefix)
        spack_env.set('ROOT_VERSION', 'v{0}'.format(self.version.up_to(1)))
        spack_env.prepend_path('PYTHONPATH', self.prefix.lib)
