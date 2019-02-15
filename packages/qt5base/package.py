from spack import *
import sys

class Qt5base(Package):
    """Qt5 Core Libraries
    """

    homepage = "http://qt-project.org/"
    url = "http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qtbase-everywhere-src-5.10.1.tar.xz"

    version('5.10.1', sha256='d8660e189caa5da5142d5894d328b61a4d3ee9750b76d61ad74e4eee8765a969')

    # What about QtSVG? resource? or add packages as extensions?
    resource(
        name='qt5svg',
        url="http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qtsvg-everywhere-src-5.10.1.tar.xz",
        sha256="00e00c04abcc8363cf7d94ca8b16af61840995a4af23685d49fa4ccafa1c7f5a",
        destination='qt5svg',
        placement='qt5svg'
        )

    # Need to understand this, but follow main spack recipe
    use_xcode = True

    # In homebrew, we have deps:
    depends_on('pkgconfig', type='build')
    depends_on('freetype')
    depends_on('libjpeg')
    depends_on('libpng')
    depends_on("openssl@1.0:")
    # PCRE2/sqlite doen't seem to work yet...
    #depends_on('pcre')
    #depends_on('sqlite')
    depends_on('zlib')
    # -qt-xcb, fontconfig on linux
    #

    def patch(self):
        # Patch for https://bugreports.qt.io/browse/QTBUG-67545
        filter_file(r'return QFixed\:\:QFixed\(int\(CTFontGetUnitsPerEm\(ctfont\)\)\);',
                    r'return QFixed(int(CTFontGetUnitsPerEm(ctfont)));',
                    'src/platformsupport/fontdatabases/mac/qfontengine_coretext.mm')

    # Configure first?
    def configure(self):
        config_args = [
            '-prefix', self.prefix,
            '-v',
            '-opensource',
            '-confirm-license',
            '-release', '-strip',
            '-shared', '-no-static',
            '-no-pch',
            '-no-avx',
            '-no-avx2',
            '-nomake', 'examples',
            '-nomake', 'tests',
            '-pkg-config',
            '-no-sql-mysql',
            '-no-sql-psql',
            #'-sqlite',
            '-openssl-linked',
            '-system-libpng',
            '-system-libjpeg',
            '-system-freetype',
            '-system-zlib'
        ]

        # Portable binaries for kernels < 3.17 cannot be created without
        # these flags. In particular, they are required to allow modern
        # containers to run on older systems.
        if sys.platform == 'linux':
            config_args.extend(["-no-feature-renameat2", "-no-feature-getentropy"])

        configure(*config_args)

    def install(self, spec, prefix):
        self.configure()
        make()
        make("install")

    @run_after('install')
    def install_qt5svg(self):
        qmake = Executable(join_path(self.spec.prefix.bin, 'qmake'))
        with working_dir('qt5svg/qt5svg'):
            qmake()
            make("install")

