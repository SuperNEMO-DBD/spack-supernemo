from spack import *

class Qt5svg(Package):
    """Qt5 SVG Library
    """

    homepage = "http://qt-project.org/"
    url = "http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qtsvg-everywhere-src-5.10.1.tar.xz"
    version('5.10.1', sha256="00e00c04abcc8363cf7d94ca8b16af61840995a4af23685d49fa4ccafa1c7f5a")

    # Must match versions
    depends_on('qt5base@5.10.1', when='@5.10.1')

    def install(self, spec, prefix):
      qmake('PREFIX={0}'.format(prefix))
      make('install')
