# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Geant4(CMakePackage):
    """Geant4 is a toolkit for the simulation of the passage of particles
    through matter. Its areas of application include high energy, nuclear
    and accelerator physics, as well as studies in medical and space
    science."""

    homepage = "http://geant4.cern.ch/"
    url = "http://geant4.cern.ch/support/source/geant4.9.6.p04.tar.gz"

    version('9.6.p04', sha256='997220a5386a43ac8f533fc7d5a8360aa1fd6338244d17deeaa583fb3a0f39fd')

    patch('https://files.warwick.ac.uk/supernemo/files/Cadfael/distfiles/geant4-9.6.4-data-export.patch',
          sha256='6d7b50f504b53c924dfae28562726b839e191c4c78139dfa33040dfd460aebed',
          when='@9.6.p04')
    patch('https://files.warwick.ac.uk/supernemo/files/Cadfael/distfiles/geant4-9.6.4-xcode.patch',
          sha256='0efa7f5b6c25f20493a3268dbd492ee3334f7839d2008554d57584ec9e4e7617',
          when='@9.6.p04')
    patch('https://files.warwick.ac.uk/supernemo/files/Cadfael/distfiles/geant4-9.6.4-c11.patch',
          sha256='c99f760125f185f436a9191c5cdbad7053e7c41aaac0f6ccbacab392787f39a9',
          when='@9.6.p04')
    patch('https://files.warwick.ac.uk/supernemo/files/Cadfael/distfiles/geant4-9.6.4-xercesc-include.patch',
          sha256='668d78b7c24efe9065a4e1aadd5441c129a454113eae96812c77a2c8861bfa64',
          when='@9.6.p04')
    patch('https://files.warwick.ac.uk/supernemo/files/Cadfael/distfiles/geant4-9.6.4-infinite-recursion.patch',
          sha256='7ee817311d36f0b49f7af9dd5e024c406210e58cc2868e2a49387eb04c99400e',
          when='@9.6.p04')

    variant('cxxstd',
            default='11',
            values=('11','14','17'),
            multi=False,
            description='Compile against the specified C++ Standard.')

    depends_on("clhep@2.1.3.1", when="@9.6.p04")

    depends_on('cmake@3.3:', type='build')
    depends_on("expat@2.1.0:")
    depends_on("xerces-c")

    def cmake_args(self):
        spec = self.spec

        options = [
            '-DGEANT4_USE_GDML=ON',
            '-DGEANT4_USE_SYSTEM_CLHEP=ON',
            '-DGEANT4_USE_SYSTEM_EXPAT=ON',
            '-DGEANT4_USE_SYSTEM_ZLIB=OFF',
            '-DGEANT4_INSTALL_DATA=ON',
            '-DGEANT4_BUILD_TLS_MODEL=global-dynamic',
            '-DXERCESC_ROOT_DIR:STRING=%s' %
            spec['xerces-c'].prefix, ]

        options.append('-DGEANT4_BUILD_CXXSTD=c++{0}'.format(
                       spec.variants['cxxstd'].value))

        return options

    def url_for_version(self, version):
        """Handle Geant4's unusual version string."""
        return ("http://geant4.cern.ch/support/source/geant4.%s.tar.gz" % version)
