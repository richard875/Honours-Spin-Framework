# system configuration generated and used by the sysconfig module
build_time_vars = {'ABIFLAGS': '',
 'AC_APPLE_UNIVERSAL_BUILD': 0,
 'AIX_BUILDDATE': 0,
 'AIX_GENUINE_CPLUSPLUS': 0,
 'ALIGNOF_LONG': 4,
 'ALIGNOF_SIZE_T': 4,
 'ALT_SOABI': 0,
 'ANDROID_API_LEVEL': 0,
 'AR': 'ar',
 'ARFLAGS': 'rcs',
 'BASECFLAGS': '-Wsign-compare -Wunreachable-code',
 'BASECPPFLAGS': '',
 'BASEMODLIBS': '',
 'BINDIR': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/bin',
 'BINLIBDEST': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/lib/python3.11',
 'BLDLIBRARY': 'libpython3.11.a',
 'BLDSHARED': 'ld',
 'BOOTSTRAP_HEADERS': '\\',
 'BUILDEXE': '.wasm',
 'BUILDPYTHON': 'python.wasm',
 'BUILD_GNU_TYPE': 'x86_64-pc-linux-gnu',
 'BYTESTR_DEPS': '\\',
 'CC': 'clang --target=wasm32-wasi',
 'CCSHARED': '',
 'CFLAGS': '-Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -g '
           '-D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
           '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
           '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
           '-isystem '
           '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
           '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
           '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
           '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot -g '
           '-D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
           '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
           '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
           '-isystem '
           '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
           '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
           '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
           '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot',
 'CFLAGSFORSHARED': '',
 'CFLAGS_ALIASING': '-fno-strict-aliasing',
 'CFLAGS_NODIST': '',
 'CONFIGFILES': 'configure configure.ac acconfig.h pyconfig.h.in '
                'Makefile.pre.in',
 'CONFIGURE_CFLAGS': '-g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                     '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                     '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                     '-isystem '
                     '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                     '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                     '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                     '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot',
 'CONFIGURE_CFLAGS_NODIST': '-std=c99 -Wextra -Wno-unused-parameter '
                            '-Wno-missing-field-initializers '
                            '-Wstrict-prototypes '
                            '-Werror=implicit-function-declaration '
                            '-fvisibility=hidden',
 'CONFIGURE_CPPFLAGS': '-g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                       '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                       '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                       '-isystem '
                       '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                       '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                       '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                       '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot',
 'CONFIGURE_LDFLAGS': '',
 'CONFIGURE_LDFLAGS_NODIST': '',
 'CONFIGURE_LDFLAGS_NOLTO': '',
 'CONFIG_ARGS': "'--host=wasm32-wasi' '--build=x86_64-pc-linux-gnu' "
                "'--with-build-python=/Users/areese/p/src/github.com/singlestore-labs/python-wasi/cpython/inst/3.11/bin/python3.11' "
                "'--with-ensurepip=no' '--disable-ipv6' "
                "'--enable-big-digits=30' '--with-suffix=.wasm' "
                "'--with-freeze-module=./build/Programs/_freeze_module' "
                "'--prefix=/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python' "
                "'build_alias=x86_64-pc-linux-gnu' 'host_alias=wasm32-wasi' "
                "'CC=clang --target=wasm32-wasi' 'CFLAGS=-g "
                '-D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                '-isystem '
                '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                "--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot' "
                "'LIBS=-Wl,--stack-first -Wl,-z,stack-size=83886080 -L/opt/lib "
                '-L/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix '
                '-lwasix '
                '-L/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/lib/wasm32-wasi '
                '-lwasi-emulated-signal '
                '-L/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/lib '
                "--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot' "
                "'CPPFLAGS=-g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL "
                '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                '-isystem '
                '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                "--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot'",
 'CONFINCLUDEDIR': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/include',
 'CONFINCLUDEPY': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/include/python3.11',
 'COREPYTHONPATH': '',
 'COVERAGE_INFO': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/cpython/coverage.info',
 'COVERAGE_REPORT': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/cpython/lcov-report',
 'COVERAGE_REPORT_OPTIONS': '--no-branch-coverage --title "CPython lcov '
                            'report"',
 'CPPFLAGS': '-I. -I./Include -g -D_WASI_EMULATED_GETPID '
             '-D_WASI_EMULATED_SIGNAL -D_WASI_EMULATED_PROCESS_CLOCKS '
             '-I/opt/include '
             '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
             '-isystem '
             '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
             '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
             '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
             '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot -g '
             '-D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
             '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
             '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
             '-isystem '
             '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
             '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
             '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
             '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot',
 'CXX': 'c++',
 'DECIMAL_CFLAGS': '-I./Modules/_decimal/libmpdec -DCONFIG_32=1 -DANSI=1',
 'DECIMAL_LDFLAGS': '-lm Modules/_decimal/libmpdec/libmpdec.a',
 'DEEPFREEZE_DEPS': './Tools/scripts/deepfreeze.py '
                    './Programs/_freeze_module.py \\',
 'DEEPFREEZE_OBJS': 'Python/deepfreeze/deepfreeze.o',
 'DESTDIRS': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python '
             '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/lib '
             '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/lib/python3.11 '
             '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/lib/python3.11/lib-dynload',
 'DESTLIB': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/lib/python3.11',
 'DESTPATH': '',
 'DESTSHARED': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/lib/python3.11/lib-dynload',
 'DFLAGS': '',
 'DIRMODE': 755,
 'DIST': 'README.rst ChangeLog configure configure.ac acconfig.h pyconfig.h.in '
         'Makefile.pre.in Include Lib Misc Ext-dummy',
 'DISTDIRS': 'Include Lib Misc Ext-dummy',
 'DISTFILES': 'README.rst ChangeLog configure configure.ac acconfig.h '
              'pyconfig.h.in Makefile.pre.in',
 'DLINCLDIR': '.',
 'DLLLIBRARY': '',
 'DOUBLE_IS_ARM_MIXED_ENDIAN_IEEE754': 0,
 'DOUBLE_IS_BIG_ENDIAN_IEEE754': 0,
 'DOUBLE_IS_LITTLE_ENDIAN_IEEE754': 1,
 'DTRACE': '',
 'DTRACE_DEPS': '\\',
 'DTRACE_HEADERS': '',
 'DTRACE_OBJS': '',
 'DYNLOADFILE': 'dynload_stub.o',
 'ENABLE_IPV6': 0,
 'ENSUREPIP': 'no',
 'EXE': '.wasm',
 'EXEMODE': 755,
 'EXPAT_CFLAGS': '-I./Modules/expat',
 'EXPAT_LDFLAGS': '-lm Modules/expat/libexpat.a',
 'EXPERIMENTAL_ISOLATED_SUBINTERPRETERS': 0,
 'EXPORTSFROM': '',
 'EXPORTSYMS': '',
 'EXTRATESTOPTS': '',
 'EXTRA_CFLAGS': '',
 'EXT_SUFFIX': '.cpython-311.so',
 'FILEMODE': 644,
 'FLOAT_WORDS_BIGENDIAN': 0,
 'FREEZE_MODULE': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/cpython/inst/3.11/bin/python3.11 '
                  './Programs/_freeze_module.py',
 'FREEZE_MODULE_BOOTSTRAP': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/cpython/inst/3.11/bin/python3.11 '
                            './Programs/_freeze_module.py',
 'FREEZE_MODULE_BOOTSTRAP_DEPS': './Programs/_freeze_module.py',
 'FREEZE_MODULE_DEPS': './Programs/_freeze_module.py',
 'FROZEN_FILES_IN': '\\',
 'FROZEN_FILES_OUT': '\\',
 'GETPGRP_HAVE_ARG': 0,
 'GITBRANCH': 'git --git-dir ./.git name-rev --name-only HEAD',
 'GITTAG': 'git --git-dir ./.git describe --all --always --dirty',
 'GITVERSION': 'git --git-dir ./.git rev-parse --short HEAD',
 'GNULD': 'no',
 'HAVE_ACCEPT4': 0,
 'HAVE_ACOSH': 1,
 'HAVE_ADDRINFO': 0,
 'HAVE_ALARM': 0,
 'HAVE_ALIGNED_REQUIRED': 1,
 'HAVE_ALLOCA_H': 1,
 'HAVE_ALTZONE': 0,
 'HAVE_ASINH': 1,
 'HAVE_ASM_TYPES_H': 0,
 'HAVE_ATANH': 1,
 'HAVE_BIND_TEXTDOMAIN_CODESET': 0,
 'HAVE_BLUETOOTH_BLUETOOTH_H': 0,
 'HAVE_BLUETOOTH_H': 0,
 'HAVE_BROKEN_MBSTOWCS': 0,
 'HAVE_BROKEN_NICE': 0,
 'HAVE_BROKEN_PIPE_BUF': 0,
 'HAVE_BROKEN_POLL': 0,
 'HAVE_BROKEN_POSIX_SEMAPHORES': 0,
 'HAVE_BROKEN_PTHREAD_SIGMASK': 0,
 'HAVE_BROKEN_SEM_GETVALUE': 1,
 'HAVE_BROKEN_UNSETENV': 0,
 'HAVE_BUILTIN_ATOMIC': 1,
 'HAVE_BZLIB_H': 1,
 'HAVE_CHFLAGS': 0,
 'HAVE_CHMOD': 1,
 'HAVE_CHOWN': 1,
 'HAVE_CHROOT': 0,
 'HAVE_CLOCK': 1,
 'HAVE_CLOCK_GETRES': 1,
 'HAVE_CLOCK_GETTIME': 1,
 'HAVE_CLOCK_NANOSLEEP': 1,
 'HAVE_CLOCK_SETTIME': 0,
 'HAVE_CLOSE_RANGE': 0,
 'HAVE_COMPUTED_GOTOS': 0,
 'HAVE_CONFSTR': 1,
 'HAVE_CONIO_H': 0,
 'HAVE_COPY_FILE_RANGE': 0,
 'HAVE_CRYPT_H': 1,
 'HAVE_CRYPT_R': 1,
 'HAVE_CTERMID': 0,
 'HAVE_CTERMID_R': 0,
 'HAVE_CURSES_FILTER': 0,
 'HAVE_CURSES_H': 0,
 'HAVE_CURSES_HAS_KEY': 0,
 'HAVE_CURSES_IMMEDOK': 0,
 'HAVE_CURSES_IS_PAD': 0,
 'HAVE_CURSES_IS_TERM_RESIZED': 0,
 'HAVE_CURSES_RESIZETERM': 0,
 'HAVE_CURSES_RESIZE_TERM': 0,
 'HAVE_CURSES_SYNCOK': 0,
 'HAVE_CURSES_TYPEAHEAD': 0,
 'HAVE_CURSES_USE_ENV': 0,
 'HAVE_CURSES_WCHGAT': 0,
 'HAVE_DB_H': 0,
 'HAVE_DECL_RTLD_DEEPBIND': 0,
 'HAVE_DECL_RTLD_GLOBAL': 0,
 'HAVE_DECL_RTLD_LAZY': 0,
 'HAVE_DECL_RTLD_LOCAL': 0,
 'HAVE_DECL_RTLD_MEMBER': 0,
 'HAVE_DECL_RTLD_NODELETE': 0,
 'HAVE_DECL_RTLD_NOLOAD': 0,
 'HAVE_DECL_RTLD_NOW': 0,
 'HAVE_DECL_TZNAME': 0,
 'HAVE_DEVICE_MACROS': 0,
 'HAVE_DEV_PTC': 0,
 'HAVE_DEV_PTMX': 0,
 'HAVE_DIRECT_H': 0,
 'HAVE_DIRENT_D_TYPE': 1,
 'HAVE_DIRENT_H': 1,
 'HAVE_DIRFD': 1,
 'HAVE_DLFCN_H': 0,
 'HAVE_DLOPEN': 0,
 'HAVE_DUP2': 0,
 'HAVE_DUP3': 0,
 'HAVE_DYLD_SHARED_CACHE_CONTAINS_PATH': 0,
 'HAVE_DYNAMIC_LOADING': 0,
 'HAVE_ENDIAN_H': 1,
 'HAVE_EPOLL': 0,
 'HAVE_EPOLL_CREATE1': 0,
 'HAVE_ERF': 1,
 'HAVE_ERFC': 1,
 'HAVE_ERRNO_H': 1,
 'HAVE_EVENTFD': 0,
 'HAVE_EXECV': 1,
 'HAVE_EXPLICIT_BZERO': 1,
 'HAVE_EXPLICIT_MEMSET': 0,
 'HAVE_EXPM1': 1,
 'HAVE_FACCESSAT': 1,
 'HAVE_FCHDIR': 0,
 'HAVE_FCHMOD': 1,
 'HAVE_FCHMODAT': 0,
 'HAVE_FCHOWN': 1,
 'HAVE_FCHOWNAT': 0,
 'HAVE_FCNTL_H': 1,
 'HAVE_FDATASYNC': 1,
 'HAVE_FDOPENDIR': 1,
 'HAVE_FDWALK': 0,
 'HAVE_FEXECVE': 0,
 'HAVE_FLOCK': 0,
 'HAVE_FORK': 1,
 'HAVE_FORK1': 0,
 'HAVE_FORKPTY': 0,
 'HAVE_FPATHCONF': 1,
 'HAVE_FSEEK64': 0,
 'HAVE_FSEEKO': 1,
 'HAVE_FSTATAT': 1,
 'HAVE_FSTATVFS': 0,
 'HAVE_FSYNC': 1,
 'HAVE_FTELL64': 0,
 'HAVE_FTELLO': 1,
 'HAVE_FTIME': 1,
 'HAVE_FTRUNCATE': 1,
 'HAVE_FUTIMENS': 1,
 'HAVE_FUTIMES': 0,
 'HAVE_FUTIMESAT': 0,
 'HAVE_GAI_STRERROR': 0,
 'HAVE_GCC_ASM_FOR_MC68881': 0,
 'HAVE_GCC_ASM_FOR_X64': 0,
 'HAVE_GCC_ASM_FOR_X87': 0,
 'HAVE_GCC_UINT128_T': 1,
 'HAVE_GDBM_DASH_NDBM_H': 0,
 'HAVE_GDBM_H': 0,
 'HAVE_GDBM_NDBM_H': 0,
 'HAVE_GETADDRINFO': 0,
 'HAVE_GETC_UNLOCKED': 0,
 'HAVE_GETEGID': 1,
 'HAVE_GETENTROPY': 1,
 'HAVE_GETEUID': 1,
 'HAVE_GETGID': 1,
 'HAVE_GETGRGID': 0,
 'HAVE_GETGRGID_R': 0,
 'HAVE_GETGRNAM_R': 0,
 'HAVE_GETGROUPLIST': 0,
 'HAVE_GETGROUPS': 0,
 'HAVE_GETHOSTBYNAME': 1,
 'HAVE_GETHOSTBYNAME_R': 0,
 'HAVE_GETHOSTBYNAME_R_3_ARG': 0,
 'HAVE_GETHOSTBYNAME_R_5_ARG': 0,
 'HAVE_GETHOSTBYNAME_R_6_ARG': 0,
 'HAVE_GETITIMER': 0,
 'HAVE_GETLOADAVG': 0,
 'HAVE_GETLOGIN': 0,
 'HAVE_GETNAMEINFO': 0,
 'HAVE_GETPAGESIZE': 0,
 'HAVE_GETPEERNAME': 1,
 'HAVE_GETPGID': 0,
 'HAVE_GETPGRP': 0,
 'HAVE_GETPID': 1,
 'HAVE_GETPPID': 1,
 'HAVE_GETPRIORITY': 0,
 'HAVE_GETPWENT': 0,
 'HAVE_GETPWNAM_R': 0,
 'HAVE_GETPWUID_R': 0,
 'HAVE_GETRANDOM': 0,
 'HAVE_GETRANDOM_SYSCALL': 0,
 'HAVE_GETRESGID': 0,
 'HAVE_GETRESUID': 0,
 'HAVE_GETRUSAGE': 0,
 'HAVE_GETSID': 0,
 'HAVE_GETSPENT': 0,
 'HAVE_GETSPNAM': 0,
 'HAVE_GETUID': 1,
 'HAVE_GETWD': 0,
 'HAVE_GLIBC_MEMMOVE_BUG': 0,
 'HAVE_GRP_H': 0,
 'HAVE_HSTRERROR': 0,
 'HAVE_HTOLE64': 1,
 'HAVE_IEEEFP_H': 0,
 'HAVE_IF_NAMEINDEX': 0,
 'HAVE_INET_ATON': 1,
 'HAVE_INET_PTON': 1,
 'HAVE_INITGROUPS': 0,
 'HAVE_INTTYPES_H': 1,
 'HAVE_IO_H': 0,
 'HAVE_IPA_PURE_CONST_BUG': 0,
 'HAVE_KILL': 1,
 'HAVE_KILLPG': 0,
 'HAVE_KQUEUE': 0,
 'HAVE_LANGINFO_H': 1,
 'HAVE_LARGEFILE_SUPPORT': 1,
 'HAVE_LCHFLAGS': 0,
 'HAVE_LCHMOD': 0,
 'HAVE_LCHOWN': 0,
 'HAVE_LIBDB': 0,
 'HAVE_LIBDL': 0,
 'HAVE_LIBDLD': 0,
 'HAVE_LIBGDBM_COMPAT': 0,
 'HAVE_LIBIEEE': 0,
 'HAVE_LIBINTL_H': 0,
 'HAVE_LIBNDBM': 0,
 'HAVE_LIBREADLINE': 0,
 'HAVE_LIBRESOLV': 0,
 'HAVE_LIBSENDFILE': 0,
 'HAVE_LIBUTIL_H': 0,
 'HAVE_LINK': 1,
 'HAVE_LINKAT': 0,
 'HAVE_LINUX_CAN_BCM_H': 0,
 'HAVE_LINUX_CAN_H': 0,
 'HAVE_LINUX_CAN_J1939_H': 0,
 'HAVE_LINUX_CAN_RAW_FD_FRAMES': 0,
 'HAVE_LINUX_CAN_RAW_H': 0,
 'HAVE_LINUX_CAN_RAW_JOIN_FILTERS': 0,
 'HAVE_LINUX_MEMFD_H': 0,
 'HAVE_LINUX_NETLINK_H': 0,
 'HAVE_LINUX_QRTR_H': 0,
 'HAVE_LINUX_RANDOM_H': 0,
 'HAVE_LINUX_SOUNDCARD_H': 0,
 'HAVE_LINUX_TIPC_H': 0,
 'HAVE_LINUX_VM_SOCKETS_H': 0,
 'HAVE_LINUX_WAIT_H': 0,
 'HAVE_LOCKF': 0,
 'HAVE_LOG1P': 1,
 'HAVE_LOG2': 1,
 'HAVE_LONG_DOUBLE': 1,
 'HAVE_LSTAT': 1,
 'HAVE_LUTIMES': 0,
 'HAVE_LZMA_H': 0,
 'HAVE_MADVISE': 0,
 'HAVE_MAKEDEV': 1,
 'HAVE_MBRTOWC': 1,
 'HAVE_MEMFD_CREATE': 0,
 'HAVE_MEMORY_H': 0,
 'HAVE_MEMRCHR': 1,
 'HAVE_MKDIRAT': 0,
 'HAVE_MKFIFO': 1,
 'HAVE_MKFIFOAT': 0,
 'HAVE_MKNOD': 1,
 'HAVE_MKNODAT': 1,
 'HAVE_MKTIME': 1,
 'HAVE_MMAP': 0,
 'HAVE_MREMAP': 0,
 'HAVE_NANOSLEEP': 1,
 'HAVE_NCURSES_H': 0,
 'HAVE_NDBM_H': 0,
 'HAVE_NDIR_H': 0,
 'HAVE_NETCAN_CAN_H': 0,
 'HAVE_NETINET_IN_H': 1,
 'HAVE_NETPACKET_PACKET_H': 1,
 'HAVE_NET_IF_H': 0,
 'HAVE_NICE': 0,
 'HAVE_NON_UNICODE_WCHAR_T_REPRESENTATION': 0,
 'HAVE_OPENAT': 0,
 'HAVE_OPENDIR': 1,
 'HAVE_OPENPTY': 0,
 'HAVE_PATHCONF': 1,
 'HAVE_PAUSE': 0,
 'HAVE_PIPE': 1,
 'HAVE_PIPE2': 0,
 'HAVE_PLOCK': 0,
 'HAVE_POLL': 1,
 'HAVE_POLL_H': 1,
 'HAVE_POSIX_FADVISE': 1,
 'HAVE_POSIX_FALLOCATE': 1,
 'HAVE_POSIX_SPAWN': 0,
 'HAVE_POSIX_SPAWNP': 0,
 'HAVE_PREAD': 1,
 'HAVE_PREADV': 0,
 'HAVE_PREADV2': 0,
 'HAVE_PRLIMIT': 0,
 'HAVE_PROCESS_H': 0,
 'HAVE_PROTOTYPES': 1,
 'HAVE_PTHREAD_CONDATTR_SETCLOCK': 0,
 'HAVE_PTHREAD_DESTRUCTOR': 0,
 'HAVE_PTHREAD_GETCPUCLOCKID': 0,
 'HAVE_PTHREAD_H': 1,
 'HAVE_PTHREAD_INIT': 0,
 'HAVE_PTHREAD_KILL': 0,
 'HAVE_PTHREAD_SIGMASK': 0,
 'HAVE_PTY_H': 0,
 'HAVE_PWRITE': 1,
 'HAVE_PWRITEV': 0,
 'HAVE_PWRITEV2': 0,
 'HAVE_READLINK': 1,
 'HAVE_READLINKAT': 0,
 'HAVE_READV': 1,
 'HAVE_REALPATH': 0,
 'HAVE_RENAMEAT': 0,
 'HAVE_RL_APPEND_HISTORY': 0,
 'HAVE_RL_CATCH_SIGNAL': 0,
 'HAVE_RL_COMPLETION_APPEND_CHARACTER': 0,
 'HAVE_RL_COMPLETION_DISPLAY_MATCHES_HOOK': 0,
 'HAVE_RL_COMPLETION_MATCHES': 0,
 'HAVE_RL_COMPLETION_SUPPRESS_APPEND': 0,
 'HAVE_RL_PRE_INPUT_HOOK': 0,
 'HAVE_RL_RESIZE_TERMINAL': 0,
 'HAVE_RPC_RPC_H': 0,
 'HAVE_RTPSPAWN': 0,
 'HAVE_SCHED_GET_PRIORITY_MAX': 0,
 'HAVE_SCHED_H': 1,
 'HAVE_SCHED_RR_GET_INTERVAL': 0,
 'HAVE_SCHED_SETAFFINITY': 0,
 'HAVE_SCHED_SETPARAM': 0,
 'HAVE_SCHED_SETSCHEDULER': 0,
 'HAVE_SEM_CLOCKWAIT': 0,
 'HAVE_SEM_GETVALUE': 0,
 'HAVE_SEM_OPEN': 0,
 'HAVE_SEM_TIMEDWAIT': 0,
 'HAVE_SEM_UNLINK': 0,
 'HAVE_SENDFILE': 0,
 'HAVE_SETEGID': 0,
 'HAVE_SETEUID': 0,
 'HAVE_SETGID': 0,
 'HAVE_SETGROUPS': 0,
 'HAVE_SETHOSTNAME': 0,
 'HAVE_SETITIMER': 0,
 'HAVE_SETJMP_H': 1,
 'HAVE_SETLOCALE': 1,
 'HAVE_SETPGID': 0,
 'HAVE_SETPGRP': 0,
 'HAVE_SETPRIORITY': 0,
 'HAVE_SETREGID': 0,
 'HAVE_SETRESGID': 0,
 'HAVE_SETRESUID': 0,
 'HAVE_SETREUID': 0,
 'HAVE_SETSID': 0,
 'HAVE_SETUID': 0,
 'HAVE_SETVBUF': 1,
 'HAVE_SHADOW_H': 0,
 'HAVE_SHM_OPEN': 0,
 'HAVE_SHM_UNLINK': 0,
 'HAVE_SHUTDOWN': 0,
 'HAVE_SIGACTION': 0,
 'HAVE_SIGALTSTACK': 0,
 'HAVE_SIGFILLSET': 0,
 'HAVE_SIGINFO_T_SI_BAND': 0,
 'HAVE_SIGINTERRUPT': 0,
 'HAVE_SIGNAL_H': 1,
 'HAVE_SIGPENDING': 0,
 'HAVE_SIGRELSE': 0,
 'HAVE_SIGTIMEDWAIT': 0,
 'HAVE_SIGWAIT': 0,
 'HAVE_SIGWAITINFO': 0,
 'HAVE_SNPRINTF': 1,
 'HAVE_SOCKADDR_ALG': 0,
 'HAVE_SOCKADDR_SA_LEN': 0,
 'HAVE_SOCKADDR_STORAGE': 1,
 'HAVE_SOCKETPAIR': 1,
 'HAVE_SPAWN_H': 0,
 'HAVE_SPLICE': 0,
 'HAVE_SSIZE_T': 1,
 'HAVE_STATVFS': 0,
 'HAVE_STAT_TV_NSEC': 1,
 'HAVE_STAT_TV_NSEC2': 0,
 'HAVE_STDARG_PROTOTYPES': 1,
 'HAVE_STDINT_H': 1,
 'HAVE_STDLIB_H': 1,
 'HAVE_STD_ATOMIC': 1,
 'HAVE_STRFTIME': 1,
 'HAVE_STRINGS_H': 1,
 'HAVE_STRING_H': 1,
 'HAVE_STRLCPY': 1,
 'HAVE_STROPTS_H': 1,
 'HAVE_STRSIGNAL': 1,
 'HAVE_STRUCT_PASSWD_PW_GECOS': 1,
 'HAVE_STRUCT_PASSWD_PW_PASSWD': 1,
 'HAVE_STRUCT_STAT_ST_BIRTHTIME': 0,
 'HAVE_STRUCT_STAT_ST_BLKSIZE': 1,
 'HAVE_STRUCT_STAT_ST_BLOCKS': 1,
 'HAVE_STRUCT_STAT_ST_FLAGS': 0,
 'HAVE_STRUCT_STAT_ST_GEN': 0,
 'HAVE_STRUCT_STAT_ST_RDEV': 1,
 'HAVE_STRUCT_TM_TM_ZONE': 1,
 'HAVE_SYMLINK': 1,
 'HAVE_SYMLINKAT': 0,
 'HAVE_SYNC': 0,
 'HAVE_SYSCONF': 1,
 'HAVE_SYSEXITS_H': 1,
 'HAVE_SYSLOG_H': 0,
 'HAVE_SYSTEM': 1,
 'HAVE_SYS_AUDIOIO_H': 0,
 'HAVE_SYS_BSDTTY_H': 0,
 'HAVE_SYS_DEVPOLL_H': 0,
 'HAVE_SYS_DIR_H': 0,
 'HAVE_SYS_ENDIAN_H': 0,
 'HAVE_SYS_EPOLL_H': 0,
 'HAVE_SYS_EVENTFD_H': 0,
 'HAVE_SYS_EVENT_H': 0,
 'HAVE_SYS_FILE_H': 1,
 'HAVE_SYS_IOCTL_H': 0,
 'HAVE_SYS_KERN_CONTROL_H': 0,
 'HAVE_SYS_LOADAVG_H': 0,
 'HAVE_SYS_LOCK_H': 0,
 'HAVE_SYS_MEMFD_H': 0,
 'HAVE_SYS_MKDEV_H': 0,
 'HAVE_SYS_MMAN_H': 0,
 'HAVE_SYS_MODEM_H': 0,
 'HAVE_SYS_NDIR_H': 0,
 'HAVE_SYS_PARAM_H': 1,
 'HAVE_SYS_POLL_H': 1,
 'HAVE_SYS_RANDOM_H': 1,
 'HAVE_SYS_RESOURCE_H': 0,
 'HAVE_SYS_SELECT_H': 1,
 'HAVE_SYS_SENDFILE_H': 0,
 'HAVE_SYS_SOCKET_H': 1,
 'HAVE_SYS_SOUNDCARD_H': 0,
 'HAVE_SYS_STATVFS_H': 0,
 'HAVE_SYS_STAT_H': 1,
 'HAVE_SYS_SYSCALL_H': 1,
 'HAVE_SYS_SYSMACROS_H': 0,
 'HAVE_SYS_SYS_DOMAIN_H': 0,
 'HAVE_SYS_TERMIO_H': 0,
 'HAVE_SYS_TIMES_H': 1,
 'HAVE_SYS_TIME_H': 1,
 'HAVE_SYS_TYPES_H': 1,
 'HAVE_SYS_UIO_H': 1,
 'HAVE_SYS_UN_H': 1,
 'HAVE_SYS_UTSNAME_H': 1,
 'HAVE_SYS_WAIT_H': 1,
 'HAVE_SYS_XATTR_H': 0,
 'HAVE_TCGETPGRP': 0,
 'HAVE_TCSETPGRP': 0,
 'HAVE_TEMPNAM': 0,
 'HAVE_TERMIOS_H': 0,
 'HAVE_TERM_H': 0,
 'HAVE_TIMEGM': 1,
 'HAVE_TIMES': 0,
 'HAVE_TMPFILE': 0,
 'HAVE_TMPNAM': 0,
 'HAVE_TMPNAM_R': 0,
 'HAVE_TM_ZONE': 1,
 'HAVE_TRUNCATE': 1,
 'HAVE_TTYNAME': 1,
 'HAVE_TZNAME': 0,
 'HAVE_UCS4_TCL': 0,
 'HAVE_UMASK': 1,
 'HAVE_UNAME': 1,
 'HAVE_UNISTD_H': 1,
 'HAVE_UNLINKAT': 1,
 'HAVE_USABLE_WCHAR_T': 0,
 'HAVE_UTIL_H': 0,
 'HAVE_UTIMENSAT': 0,
 'HAVE_UTIMES': 1,
 'HAVE_UTIME_H': 1,
 'HAVE_UUID_CREATE': 0,
 'HAVE_UUID_ENC_BE': 0,
 'HAVE_UUID_GENERATE_TIME_SAFE': 0,
 'HAVE_UUID_H': 1,
 'HAVE_UUID_UUID_H': 0,
 'HAVE_VFORK': 0,
 'HAVE_WAIT': 1,
 'HAVE_WAIT3': 0,
 'HAVE_WAIT4': 0,
 'HAVE_WAITID': 0,
 'HAVE_WAITPID': 1,
 'HAVE_WCHAR_H': 1,
 'HAVE_WCSCOLL': 1,
 'HAVE_WCSFTIME': 1,
 'HAVE_WCSXFRM': 1,
 'HAVE_WMEMCMP': 1,
 'HAVE_WORKING_TZSET': 0,
 'HAVE_WRITEV': 1,
 'HAVE_ZLIB_COPY': 1,
 'HAVE_ZLIB_H': 0,
 'HAVE__GETPTY': 0,
 'HOST_GNU_TYPE': 'wasm32-unknown-wasi',
 'INCLDIRSTOMAKE': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/include '
                   '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/include '
                   '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/include/python3.11 '
                   '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/include/python3.11',
 'INCLUDEDIR': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/include',
 'INCLUDEPY': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/include/python3.11',
 'INSTALL': '/opt/homebrew/bin/ginstall -c',
 'INSTALL_DATA': '/opt/homebrew/bin/ginstall -c -m 644',
 'INSTALL_PROGRAM': '/opt/homebrew/bin/ginstall -c',
 'INSTALL_SCRIPT': '/opt/homebrew/bin/ginstall -c',
 'INSTALL_SHARED': '/opt/homebrew/bin/ginstall -c -m 755',
 'INSTSONAME': 'libpython3.11.a',
 'IO_H': 'Modules/_io/_iomodule.h',
 'IO_OBJS': '\\',
 'LDCXXSHARED': 'ld',
 'LDFLAGS': '',
 'LDFLAGS_NODIST': '',
 'LDLIBRARY': 'libpython3.11.a',
 'LDLIBRARYDIR': '',
 'LDSHARED': 'ld',
 'LDVERSION': '3.11',
 'LIBC': '',
 'LIBDEST': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/lib/python3.11',
 'LIBDIR': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/lib',
 'LIBEXPAT_A': 'Modules/expat/libexpat.a',
 'LIBEXPAT_CFLAGS': '-Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 '
                    '-Wall -g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                    '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-isystem '
                    '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                    '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                    '-g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                    '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-isystem '
                    '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                    '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                    '-std=c99 -Wextra -Wno-unused-parameter '
                    '-Wno-missing-field-initializers -Wstrict-prototypes '
                    '-Werror=implicit-function-declaration '
                    '-fvisibility=hidden  -I./Include/internal -I. -I./Include '
                    '-g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                    '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-isystem '
                    '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                    '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                    '-g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                    '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-isystem '
                    '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                    '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot  '
                    '-I./Modules/expat',
 'LIBEXPAT_HEADERS': '\\',
 'LIBEXPAT_OBJS': '\\',
 'LIBFFI_INCLUDEDIR': '/Library/Developer/CommandLineTools/SDKs/MacOSX12.sdk/usr/include/ffi',
 'LIBM': '-lm',
 'LIBMPDEC_A': 'Modules/_decimal/libmpdec/libmpdec.a',
 'LIBMPDEC_CFLAGS': '-Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 '
                    '-Wall -g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                    '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-isystem '
                    '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                    '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                    '-g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                    '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-isystem '
                    '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                    '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                    '-std=c99 -Wextra -Wno-unused-parameter '
                    '-Wno-missing-field-initializers -Wstrict-prototypes '
                    '-Werror=implicit-function-declaration '
                    '-fvisibility=hidden  -I./Include/internal -I. -I./Include '
                    '-g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                    '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-isystem '
                    '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                    '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                    '-g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                    '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-isystem '
                    '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                    '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                    '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                    '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot  '
                    '-I./Modules/_decimal/libmpdec -DCONFIG_32=1 -DANSI=1',
 'LIBMPDEC_HEADERS': '\\',
 'LIBMPDEC_OBJS': '\\',
 'LIBOBJDIR': 'Python/',
 'LIBOBJS': 'Python/dup2$U.o',
 'LIBPC': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/lib/pkgconfig',
 'LIBPL': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/lib/python3.11/config-3.11',
 'LIBPYTHON': '',
 'LIBRARY': 'libpython3.11.a',
 'LIBRARY_DEPS': 'libpython3.11.a',
 'LIBRARY_OBJS': '\\',
 'LIBRARY_OBJS_OMIT_FROZEN': '\\',
 'LIBS': '-Wl,--stack-first -Wl,-z,stack-size=83886080 -L/opt/lib '
         '-L/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix '
         '-lwasix '
         '-L/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/lib/wasm32-wasi '
         '-lwasi-emulated-signal '
         '-L/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/lib '
         '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
         '-lwasi-emulated-signal -lpthread',
 'LIBSUBDIRS': 'asyncio \\',
 'LINKCC': 'clang --target=wasm32-wasi',
 'LINKFORSHARED': '',
 'LINK_PYTHON_DEPS': 'libpython3.11.a',
 'LINK_PYTHON_OBJS': '\\',
 'LIPO_32BIT_FLAGS': '',
 'LIPO_INTEL64_FLAGS': '',
 'LLVM_PROF_ERR': 'yes',
 'LLVM_PROF_FILE': 'LLVM_PROFILE_FILE="code-%p.profclangr"',
 'LLVM_PROF_MERGER': "'' merge -output=code.profclangd *.profclangr",
 'LN': 'ln',
 'LOCALMODLIBS': '-lm -lm -lm -lm -lm -lm Modules/_decimal/libmpdec/libmpdec.a '
                 '-lz -lbz2 -L/opt/homebrew/Cellar/xz/5.2.5/lib -llzma '
                 '-lz       -lm Modules/expat/libexpat.a              '
                 '-lsqlite3',
 'MACHDEP': 'wasi',
 'MACHDEP_OBJS': '',
 'MACHDESTLIB': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/lib/python3.11',
 'MACOSX_DEPLOYMENT_TARGET': '',
 'MAINCC': 'clang --target=wasm32-wasi',
 'MAJOR_IN_MKDEV': 0,
 'MAJOR_IN_SYSMACROS': 0,
 'MAKESETUP': './Modules/makesetup',
 'MANDIR': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/share/man',
 'MKDIR_P': '/opt/homebrew/bin/gmkdir -p',
 'MODBUILT_NAMES': 'array  _asyncio  _bisect  _contextvars  _csv  _heapq  '
                   '_json  _lsprof  _opcode  _pickle  _queue  _random  '
                   '_struct  _typing  _xxsubinterpreters  _zoneinfo  audioop  '
                   'math  cmath  _statistics  _datetime  _decimal  binascii  '
                   '_bz2  _lzma  zlib  _md5  _sha1  _sha256  _sha512  _sha3  '
                   '_blake2  pyexpat  _elementtree  _codecs_cn  _codecs_hk  '
                   '_codecs_iso2022  _codecs_jp  _codecs_kr  _codecs_tw  '
                   '_multibytecodec  unicodedata  _crypt  _posixsubprocess  '
                   'select  _socket  _sqlite3  _xxtestfuzz  _testbuffer  '
                   '_testinternalcapi  _testcapi  _ctypes_test  atexit  '
                   'faulthandler  posix  _signal  _tracemalloc  _codecs  '
                   '_collections  errno  _io  itertools  _sre  _thread  time  '
                   '_weakref  _abc  _functools  _locale  _operator  _stat  '
                   '_symtable  pwd  xxsubtype',
 'MODDISABLED_NAMES': '',
 'MODLIBS': '-lm -lm -lm -lm -lm -lm Modules/_decimal/libmpdec/libmpdec.a -lz '
            '-lbz2 -L/opt/homebrew/Cellar/xz/5.2.5/lib -llzma -lz       -lm '
            'Modules/expat/libexpat.a              -lsqlite3',
 'MODOBJS': 'Modules/arraymodule.o  Modules/_asynciomodule.o  '
            'Modules/_bisectmodule.o  Modules/_contextvarsmodule.o  '
            'Modules/_csv.o  Modules/_heapqmodule.o  Modules/_json.o  '
            'Modules/_lsprof.o Modules/rotatingtree.o  Modules/_opcode.o  '
            'Modules/_pickle.o  Modules/_queuemodule.o  '
            'Modules/_randommodule.o  Modules/_struct.o  '
            'Modules/_typingmodule.o  Modules/_xxsubinterpretersmodule.o  '
            'Modules/_zoneinfo.o  Modules/audioop.o  Modules/mathmodule.o  '
            'Modules/cmathmodule.o  Modules/_statisticsmodule.o  '
            'Modules/_datetimemodule.o  Modules/_decimal/_decimal.o  '
            'Modules/binascii.o  Modules/_bz2module.o  Modules/_lzmamodule.o  '
            'Modules/zlibmodule.o  Modules/md5module.o  Modules/sha1module.o  '
            'Modules/sha256module.o  Modules/sha512module.o  '
            'Modules/_sha3/sha3module.o  Modules/_blake2/blake2module.o '
            'Modules/_blake2/blake2b_impl.o Modules/_blake2/blake2s_impl.o  '
            'Modules/pyexpat.o  Modules/_elementtree.o  '
            'Modules/cjkcodecs/_codecs_cn.o  Modules/cjkcodecs/_codecs_hk.o  '
            'Modules/cjkcodecs/_codecs_iso2022.o  '
            'Modules/cjkcodecs/_codecs_jp.o  Modules/cjkcodecs/_codecs_kr.o  '
            'Modules/cjkcodecs/_codecs_tw.o  '
            'Modules/cjkcodecs/multibytecodec.o  Modules/unicodedata.o  '
            'Modules/_cryptmodule.o  Modules/_posixsubprocess.o  '
            'Modules/selectmodule.o  Modules/socketmodule.o  '
            'Modules/_sqlite/connection.o Modules/_sqlite/cursor.o '
            'Modules/_sqlite/microprotocols.o Modules/_sqlite/module.o '
            'Modules/_sqlite/prepare_protocol.o Modules/_sqlite/row.o '
            'Modules/_sqlite/statement.o Modules/_sqlite/util.o  '
            'Modules/_xxtestfuzz/_xxtestfuzz.o Modules/_xxtestfuzz/fuzzer.o  '
            'Modules/_testbuffer.o  Modules/_testinternalcapi.o  '
            'Modules/_testcapimodule.o  Modules/atexitmodule.o  '
            'Modules/faulthandler.o  Modules/posixmodule.o  '
            'Modules/signalmodule.o  Modules/_tracemalloc.o  '
            'Modules/_codecsmodule.o  Modules/_collectionsmodule.o  '
            'Modules/errnomodule.o  Modules/_io/_iomodule.o '
            'Modules/_io/iobase.o Modules/_io/fileio.o Modules/_io/bytesio.o '
            'Modules/_io/bufferedio.o Modules/_io/textio.o '
            'Modules/_io/stringio.o  Modules/itertoolsmodule.o  '
            'Modules/_sre.o  Modules/_threadmodule.o  Modules/timemodule.o  '
            'Modules/_weakref.o  Modules/_abc.o  Modules/_functoolsmodule.o  '
            'Modules/_localemodule.o  Modules/_operator.o  Modules/_stat.o  '
            'Modules/symtablemodule.o  Modules/pwdmodule.o  '
            'Modules/xxsubtype.o',
 'MODSHARED_NAMES': '_ctypes_test',
 'MODULE_ARRAY': 'yes',
 'MODULE_ARRAY_LDFLAGS': '',
 'MODULE_ATEXIT_LDFLAGS': '',
 'MODULE_AUDIOOP': 'yes',
 'MODULE_AUDIOOP_LDFLAGS': '-lm',
 'MODULE_BINASCII': 'yes',
 'MODULE_BINASCII_CFLAGS': '-DUSE_ZLIB_CRC32',
 'MODULE_BINASCII_LDFLAGS': '-lz',
 'MODULE_CMATH': 'yes',
 'MODULE_CMATH_DEPS': './Modules/_math.h',
 'MODULE_CMATH_LDFLAGS': '-lm',
 'MODULE_ERRNO_LDFLAGS': '',
 'MODULE_FAULTHANDLER_LDFLAGS': '',
 'MODULE_FCNTL': 'missing',
 'MODULE_GRP': 'missing',
 'MODULE_ITERTOOLS_LDFLAGS': '',
 'MODULE_MATH': 'yes',
 'MODULE_MATH_DEPS': './Modules/_math.h',
 'MODULE_MATH_LDFLAGS': '-lm',
 'MODULE_MMAP': 'missing',
 'MODULE_NIS': 'missing',
 'MODULE_OBJS': '\\',
 'MODULE_OSSAUDIODEV': 'missing',
 'MODULE_POSIX_LDFLAGS': '',
 'MODULE_PWD_LDFLAGS': '',
 'MODULE_PYEXPAT': 'yes',
 'MODULE_PYEXPAT_CFLAGS': '-I./Modules/expat',
 'MODULE_PYEXPAT_DEPS': '\\ Modules/expat/libexpat.a',
 'MODULE_PYEXPAT_LDFLAGS': '-lm Modules/expat/libexpat.a',
 'MODULE_RESOURCE': 'missing',
 'MODULE_SELECT': 'yes',
 'MODULE_SELECT_LDFLAGS': '',
 'MODULE_SPWD': 'missing',
 'MODULE_SYSLOG': 'missing',
 'MODULE_TERMIOS': 'missing',
 'MODULE_TIME': 'yes',
 'MODULE_TIME_LDFLAGS': '',
 'MODULE_UNICODEDATA': 'yes',
 'MODULE_UNICODEDATA_DEPS': './Modules/unicodedata_db.h '
                            './Modules/unicodename_db.h',
 'MODULE_UNICODEDATA_LDFLAGS': '',
 'MODULE_XXLIMITED': 'missing',
 'MODULE_XXLIMITED_35': 'missing',
 'MODULE_XXSUBTYPE_LDFLAGS': '',
 'MODULE_ZLIB': 'yes',
 'MODULE_ZLIB_CFLAGS': '',
 'MODULE_ZLIB_LDFLAGS': '-lz',
 'MODULE__ABC_LDFLAGS': '',
 'MODULE__ASYNCIO': 'yes',
 'MODULE__ASYNCIO_LDFLAGS': '',
 'MODULE__BISECT': 'yes',
 'MODULE__BISECT_LDFLAGS': '',
 'MODULE__BLAKE2': 'yes',
 'MODULE__BLAKE2_DEPS': './Modules/_blake2/impl/blake2-config.h '
                        './Modules/_blake2/impl/blake2-dispatch.c '
                        './Modules/_blake2/impl/blake2-impl.h '
                        './Modules/_blake2/impl/blake2-kat.h '
                        './Modules/_blake2/impl/blake2.h '
                        './Modules/_blake2/impl/blake2b-load-sse2.h '
                        './Modules/_blake2/impl/blake2b-load-sse41.h '
                        './Modules/_blake2/impl/blake2b-ref.c '
                        './Modules/_blake2/impl/blake2b-round.h '
                        './Modules/_blake2/impl/blake2b-test.c '
                        './Modules/_blake2/impl/blake2b.c '
                        './Modules/_blake2/impl/blake2bp-test.c '
                        './Modules/_blake2/impl/blake2bp.c '
                        './Modules/_blake2/impl/blake2s-load-sse2.h '
                        './Modules/_blake2/impl/blake2s-load-sse41.h '
                        './Modules/_blake2/impl/blake2s-load-xop.h '
                        './Modules/_blake2/impl/blake2s-ref.c '
                        './Modules/_blake2/impl/blake2s-round.h '
                        './Modules/_blake2/impl/blake2s-test.c '
                        './Modules/_blake2/impl/blake2s.c '
                        './Modules/_blake2/impl/blake2sp-test.c '
                        './Modules/_blake2/impl/blake2sp.c ./Modules/hashlib.h',
 'MODULE__BLAKE2_LDFLAGS': '',
 'MODULE__BZ2': 'yes',
 'MODULE__BZ2_CFLAGS': '',
 'MODULE__BZ2_LDFLAGS': '-lbz2',
 'MODULE__CODECS_CN': 'yes',
 'MODULE__CODECS_CN_LDFLAGS': '',
 'MODULE__CODECS_HK': 'yes',
 'MODULE__CODECS_HK_LDFLAGS': '',
 'MODULE__CODECS_ISO2022': 'yes',
 'MODULE__CODECS_ISO2022_LDFLAGS': '',
 'MODULE__CODECS_JP': 'yes',
 'MODULE__CODECS_JP_LDFLAGS': '',
 'MODULE__CODECS_KR': 'yes',
 'MODULE__CODECS_KR_LDFLAGS': '',
 'MODULE__CODECS_LDFLAGS': '',
 'MODULE__CODECS_TW': 'yes',
 'MODULE__CODECS_TW_LDFLAGS': '',
 'MODULE__COLLECTIONS_LDFLAGS': '',
 'MODULE__CONTEXTVARS': 'yes',
 'MODULE__CONTEXTVARS_LDFLAGS': '',
 'MODULE__CRYPT': 'yes',
 'MODULE__CRYPT_CFLAGS': '',
 'MODULE__CRYPT_LDFLAGS': '',
 'MODULE__CSV': 'yes',
 'MODULE__CSV_LDFLAGS': '',
 'MODULE__CTYPES_DEPS': './Modules/_ctypes/ctypes.h',
 'MODULE__CTYPES_TEST': 'yes',
 'MODULE__CTYPES_TEST_LDFLAGS': '-lm',
 'MODULE__DATETIME': 'yes',
 'MODULE__DATETIME_LDFLAGS': '-lm',
 'MODULE__DECIMAL': 'yes',
 'MODULE__DECIMAL_CFLAGS': '-I./Modules/_decimal/libmpdec -DCONFIG_32=1 '
                           '-DANSI=1',
 'MODULE__DECIMAL_DEPS': './Modules/_decimal/docstrings.h \\ '
                         'Modules/_decimal/libmpdec/libmpdec.a',
 'MODULE__DECIMAL_LDFLAGS': '-lm Modules/_decimal/libmpdec/libmpdec.a',
 'MODULE__ELEMENTTREE': 'yes',
 'MODULE__ELEMENTTREE_CFLAGS': '-I./Modules/expat',
 'MODULE__ELEMENTTREE_DEPS': './Modules/pyexpat.c \\ Modules/expat/libexpat.a',
 'MODULE__ELEMENTTREE_LDFLAGS': '',
 'MODULE__FUNCTOOLS_LDFLAGS': '',
 'MODULE__GDBM': 'missing',
 'MODULE__HASHLIB': 'missing',
 'MODULE__HASHLIB_DEPS': './Modules/hashlib.h',
 'MODULE__HEAPQ': 'yes',
 'MODULE__HEAPQ_LDFLAGS': '',
 'MODULE__IO': 'yes',
 'MODULE__IO_CFLAGS': '-I./Modules/_io',
 'MODULE__IO_DEPS': './Modules/_io/_iomodule.h',
 'MODULE__IO_LDFLAGS': '',
 'MODULE__JSON': 'yes',
 'MODULE__JSON_LDFLAGS': '',
 'MODULE__LOCALE_LDFLAGS': '',
 'MODULE__LSPROF': 'yes',
 'MODULE__LSPROF_LDFLAGS': '',
 'MODULE__LZMA': 'yes',
 'MODULE__LZMA_CFLAGS': '-I/opt/homebrew/Cellar/xz/5.2.5/include',
 'MODULE__LZMA_LDFLAGS': '-L/opt/homebrew/Cellar/xz/5.2.5/lib -llzma',
 'MODULE__MD5': 'yes',
 'MODULE__MD5_DEPS': './Modules/hashlib.h',
 'MODULE__MD5_LDFLAGS': '',
 'MODULE__MULTIBYTECODEC': 'yes',
 'MODULE__MULTIBYTECODEC_LDFLAGS': '',
 'MODULE__MULTIPROCESSING': 'missing',
 'MODULE__OPCODE': 'yes',
 'MODULE__OPCODE_LDFLAGS': '',
 'MODULE__OPERATOR_LDFLAGS': '',
 'MODULE__PICKLE': 'yes',
 'MODULE__PICKLE_LDFLAGS': '',
 'MODULE__POSIXSHMEM': 'missing',
 'MODULE__POSIXSUBPROCESS': 'yes',
 'MODULE__POSIXSUBPROCESS_LDFLAGS': '',
 'MODULE__QUEUE': 'yes',
 'MODULE__QUEUE_LDFLAGS': '',
 'MODULE__RANDOM': 'yes',
 'MODULE__RANDOM_LDFLAGS': '',
 'MODULE__SCPROXY': 'n/a',
 'MODULE__SHA1': 'yes',
 'MODULE__SHA1_DEPS': './Modules/hashlib.h',
 'MODULE__SHA1_LDFLAGS': '',
 'MODULE__SHA256': 'yes',
 'MODULE__SHA256_DEPS': './Modules/hashlib.h',
 'MODULE__SHA256_LDFLAGS': '',
 'MODULE__SHA3': 'yes',
 'MODULE__SHA3_DEPS': './Modules/_sha3/kcp/KeccakHash.c '
                      './Modules/_sha3/kcp/KeccakHash.h '
                      './Modules/_sha3/kcp/KeccakP-1600-64.macros '
                      './Modules/_sha3/kcp/KeccakP-1600-SnP-opt32.h '
                      './Modules/_sha3/kcp/KeccakP-1600-SnP-opt64.h '
                      './Modules/_sha3/kcp/KeccakP-1600-SnP.h '
                      './Modules/_sha3/kcp/KeccakP-1600-inplace32BI.c '
                      './Modules/_sha3/kcp/KeccakP-1600-opt64-config.h '
                      './Modules/_sha3/kcp/KeccakP-1600-opt64.c '
                      './Modules/_sha3/kcp/KeccakP-1600-unrolling.macros '
                      './Modules/_sha3/kcp/KeccakSponge.c '
                      './Modules/_sha3/kcp/KeccakSponge.h '
                      './Modules/_sha3/kcp/KeccakSponge.inc '
                      './Modules/_sha3/kcp/PlSnP-Fallback.inc '
                      './Modules/_sha3/kcp/SnP-Relaned.h '
                      './Modules/_sha3/kcp/align.h ./Modules/hashlib.h',
 'MODULE__SHA3_LDFLAGS': '',
 'MODULE__SHA512': 'yes',
 'MODULE__SHA512_DEPS': './Modules/hashlib.h',
 'MODULE__SHA512_LDFLAGS': '',
 'MODULE__SIGNAL_LDFLAGS': '',
 'MODULE__SOCKET': 'yes',
 'MODULE__SOCKET_DEPS': './Modules/socketmodule.h',
 'MODULE__SOCKET_LDFLAGS': '',
 'MODULE__SQLITE3': 'yes',
 'MODULE__SQLITE3_CFLAGS': '-I./Modules/_sqlite',
 'MODULE__SQLITE3_DEPS': './Modules/_sqlite/connection.h '
                         './Modules/_sqlite/cursor.h '
                         './Modules/_sqlite/microprotocols.h '
                         './Modules/_sqlite/module.h '
                         './Modules/_sqlite/prepare_protocol.h '
                         './Modules/_sqlite/row.h ./Modules/_sqlite/util.h',
 'MODULE__SQLITE3_LDFLAGS': '-lsqlite3',
 'MODULE__SRE_LDFLAGS': '',
 'MODULE__SSL': 'missing',
 'MODULE__SSL_DEPS': './Modules/_ssl.h ./Modules/_ssl/cert.c '
                     './Modules/_ssl/debughelpers.c ./Modules/_ssl/misc.c '
                     './Modules/_ssl_data.h ./Modules/_ssl_data_111.h '
                     './Modules/_ssl_data_300.h ./Modules/socketmodule.h',
 'MODULE__STATISTICS': 'yes',
 'MODULE__STATISTICS_LDFLAGS': '-lm',
 'MODULE__STAT_LDFLAGS': '',
 'MODULE__STRUCT': 'yes',
 'MODULE__STRUCT_LDFLAGS': '',
 'MODULE__SYMTABLE_LDFLAGS': '',
 'MODULE__TESTBUFFER': 'yes',
 'MODULE__TESTBUFFER_LDFLAGS': '',
 'MODULE__TESTCAPI': 'yes',
 'MODULE__TESTCAPI_DEPS': './Modules/testcapi_long.h',
 'MODULE__TESTCAPI_LDFLAGS': '',
 'MODULE__TESTIMPORTMULTIPLE': 'missing',
 'MODULE__TESTINTERNALCAPI': 'yes',
 'MODULE__TESTINTERNALCAPI_LDFLAGS': '',
 'MODULE__TESTMULTIPHASE': 'missing',
 'MODULE__THREAD_LDFLAGS': '',
 'MODULE__TRACEMALLOC_LDFLAGS': '',
 'MODULE__TYPING': 'yes',
 'MODULE__TYPING_LDFLAGS': '',
 'MODULE__UUID': 'missing',
 'MODULE__WEAKREF_LDFLAGS': '',
 'MODULE__XXSUBINTERPRETERS': 'yes',
 'MODULE__XXSUBINTERPRETERS_LDFLAGS': '',
 'MODULE__XXTESTFUZZ': 'yes',
 'MODULE__XXTESTFUZZ_LDFLAGS': '',
 'MODULE__ZONEINFO': 'yes',
 'MODULE__ZONEINFO_LDFLAGS': '',
 'MULTIARCH': 'wasm32-wasi',
 'MULTIARCH_CPPFLAGS': '-DMULTIARCH=\\"wasm32-wasi\\"',
 'MVWDELCH_IS_EXPRESSION': 0,
 'NO_AS_NEEDED': '',
 'OBJECT_OBJS': '\\',
 'OPENSSL_INCLUDES': '',
 'OPENSSL_LDFLAGS': '',
 'OPENSSL_LIBS': '',
 'OPENSSL_RPATH': '',
 'OPT': '-DNDEBUG -g -fwrapv -O3 -Wall',
 'OTHER_LIBTOOL_OPT': '',
 'PACKAGE_BUGREPORT': 0,
 'PACKAGE_NAME': 0,
 'PACKAGE_STRING': 0,
 'PACKAGE_TARNAME': 0,
 'PACKAGE_URL': 0,
 'PACKAGE_VERSION': 0,
 'PARSER_HEADERS': '\\',
 'PARSER_OBJS': '\\ \\ Parser/myreadline.o Parser/tokenizer.o',
 'PEGEN_HEADERS': '\\',
 'PEGEN_OBJS': '\\',
 'PGO_PROF_GEN_FLAG': '-fprofile-instr-generate',
 'PGO_PROF_USE_FLAG': '-fprofile-instr-use=code.profclangd',
 'PLATLIBDIR': 'lib',
 'POBJS': '\\',
 'POSIX_SEMAPHORES_NOT_ENABLED': 0,
 'PROFILE_TASK': '-m test --pgo --timeout=1200',
 'PTHREAD_KEY_T_IS_COMPATIBLE_WITH_INT': 1,
 'PTHREAD_SYSTEM_SCHED_SUPPORTED': 0,
 'PURIFY': '',
 'PY3LIBRARY': '',
 'PYLONG_BITS_IN_DIGIT': 30,
 'PYTHON': 'python.wasm',
 'PYTHONFRAMEWORK': '',
 'PYTHONFRAMEWORKDIR': 'no-framework',
 'PYTHONFRAMEWORKINSTALLDIR': '',
 'PYTHONFRAMEWORKPREFIX': '',
 'PYTHONPATH': '',
 'PYTHON_FOR_BUILD': '_PYTHON_PROJECT_BASE=/Users/areese/p/src/github.com/singlestore-labs/python-wasi/cpython '
                     '_PYTHON_HOST_PLATFORM=$(_PYTHON_HOST_PLATFORM) '
                     'PYTHONPATH=$(shell test -f pybuilddir.txt && echo '
                     '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/cpython/`cat '
                     'pybuilddir.txt`:)./Lib '
                     '_PYTHON_SYSCONFIGDATA_NAME=_sysconfigdata__wasi_wasm32-wasi '
                     '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/cpython/inst/3.11/bin/python3.11',
 'PYTHON_FOR_FREEZE': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/cpython/inst/3.11/bin/python3.11',
 'PYTHON_FOR_REGEN': '',
 'PYTHON_HEADERS': '\\',
 'PYTHON_OBJS': '\\',
 'PY_BUILTIN_HASHLIB_HASHES': '"md5,sha1,sha256,sha512,sha3,blake2"',
 'PY_BUILTIN_MODULE_CFLAGS': '-Wsign-compare -Wunreachable-code -DNDEBUG -g '
                             '-fwrapv -O3 -Wall -g -D_WASI_EMULATED_GETPID '
                             '-D_WASI_EMULATED_SIGNAL '
                             '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                             '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                             '-isystem '
                             '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                             '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                             '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                             '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                             '-g -D_WASI_EMULATED_GETPID '
                             '-D_WASI_EMULATED_SIGNAL '
                             '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                             '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                             '-isystem '
                             '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                             '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                             '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                             '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                             '-std=c99 -Wextra -Wno-unused-parameter '
                             '-Wno-missing-field-initializers '
                             '-Wstrict-prototypes '
                             '-Werror=implicit-function-declaration '
                             '-fvisibility=hidden  -I./Include/internal -I. '
                             '-I./Include -g -D_WASI_EMULATED_GETPID '
                             '-D_WASI_EMULATED_SIGNAL '
                             '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                             '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                             '-isystem '
                             '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                             '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                             '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                             '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                             '-g -D_WASI_EMULATED_GETPID '
                             '-D_WASI_EMULATED_SIGNAL '
                             '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                             '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                             '-isystem '
                             '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                             '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                             '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                             '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                             '-DPy_BUILD_CORE_BUILTIN',
 'PY_CFLAGS': '-Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall '
              '-g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
              '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
              '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
              '-isystem '
              '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
              '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
              '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
              '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot -g '
              '-D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
              '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
              '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
              '-isystem '
              '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
              '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
              '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
              '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot',
 'PY_CFLAGS_NODIST': '-std=c99 -Wextra -Wno-unused-parameter '
                     '-Wno-missing-field-initializers -Wstrict-prototypes '
                     '-Werror=implicit-function-declaration '
                     '-fvisibility=hidden  -I./Include/internal',
 'PY_COERCE_C_LOCALE': 1,
 'PY_CORE_CFLAGS': '-Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 '
                   '-Wall -g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                   '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                   '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                   '-isystem '
                   '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                   '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                   '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                   '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                   '-g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                   '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                   '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                   '-isystem '
                   '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                   '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                   '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                   '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                   '-std=c99 -Wextra -Wno-unused-parameter '
                   '-Wno-missing-field-initializers -Wstrict-prototypes '
                   '-Werror=implicit-function-declaration -fvisibility=hidden  '
                   '-I./Include/internal -I. -I./Include -g '
                   '-D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                   '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                   '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                   '-isystem '
                   '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                   '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                   '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                   '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                   '-g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                   '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                   '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                   '-isystem '
                   '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                   '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                   '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                   '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                   '-DPy_BUILD_CORE',
 'PY_CORE_LDFLAGS': '',
 'PY_CPPFLAGS': '-I. -I./Include -g -D_WASI_EMULATED_GETPID '
                '-D_WASI_EMULATED_SIGNAL -D_WASI_EMULATED_PROCESS_CLOCKS '
                '-I/opt/include '
                '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                '-isystem '
                '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot -g '
                '-D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                '-isystem '
                '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot',
 'PY_ENABLE_SHARED': 0,
 'PY_FORMAT_SIZE_T': '"z"',
 'PY_LDFLAGS': '',
 'PY_LDFLAGS_NODIST': '',
 'PY_LDFLAGS_NOLTO': '',
 'PY_SQLITE_ENABLE_LOAD_EXTENSION': 0,
 'PY_SSL_DEFAULT_CIPHERS': 1,
 'PY_SSL_DEFAULT_CIPHER_STRING': 0,
 'PY_STDMODULE_CFLAGS': '-Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv '
                        '-O3 -Wall -g -D_WASI_EMULATED_GETPID '
                        '-D_WASI_EMULATED_SIGNAL '
                        '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                        '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                        '-isystem '
                        '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                        '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                        '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                        '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                        '-g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                        '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                        '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                        '-isystem '
                        '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                        '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                        '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                        '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                        '-std=c99 -Wextra -Wno-unused-parameter '
                        '-Wno-missing-field-initializers -Wstrict-prototypes '
                        '-Werror=implicit-function-declaration '
                        '-fvisibility=hidden  -I./Include/internal -I. '
                        '-I./Include -g -D_WASI_EMULATED_GETPID '
                        '-D_WASI_EMULATED_SIGNAL '
                        '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                        '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                        '-isystem '
                        '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                        '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                        '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                        '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
                        '-g -D_WASI_EMULATED_GETPID -D_WASI_EMULATED_SIGNAL '
                        '-D_WASI_EMULATED_PROCESS_CLOCKS -I/opt/include '
                        '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                        '-isystem '
                        '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix/include '
                        '-I/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/include '
                        '-I/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/include '
                        '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot',
 'Py_DEBUG': 0,
 'Py_ENABLE_SHARED': 0,
 'Py_HASH_ALGORITHM': 0,
 'Py_STATS': 0,
 'Py_TRACE_REFS': 0,
 'QUICKTESTOPTS': '-x test_subprocess test_io test_lib2to3 \\',
 'READELF': 'wasm32-wasi-readelf',
 'RESSRCDIR': 'Mac/Resources/framework',
 'RETSIGTYPE': 'void',
 'RUNSHARED': '',
 'SCRIPTDIR': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/lib',
 'SETPGRP_HAVE_ARG': 0,
 'SHAREDMODS': 'Modules/_ctypes_test.cpython-311.so',
 'SHELL': '/bin/sh',
 'SHLIBS': '-Wl,--stack-first -Wl,-z,stack-size=83886080 -L/opt/lib '
           '-L/Users/areese/p/src/github.com/singlestore-labs/python-wasi/wasix '
           '-lwasix '
           '-L/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot/lib/wasm32-wasi '
           '-lwasi-emulated-signal '
           '-L/Users/areese/p/src/github.com/singlestore-labs/python-wasi/docker/lib '
           '--sysroot=/Users/areese/p/wasi-sdk-14.0/share/wasi-sysroot '
           '-lwasi-emulated-signal -lpthread',
 'SHLIB_SUFFIX': '.so',
 'SIGNED_RIGHT_SHIFT_ZERO_FILLS': 0,
 'SITEPATH': '',
 'SIZEOF_DOUBLE': 8,
 'SIZEOF_FLOAT': 4,
 'SIZEOF_FPOS_T': 16,
 'SIZEOF_INT': 4,
 'SIZEOF_LONG': 4,
 'SIZEOF_LONG_DOUBLE': 16,
 'SIZEOF_LONG_LONG': 8,
 'SIZEOF_OFF_T': 8,
 'SIZEOF_PID_T': 4,
 'SIZEOF_PTHREAD_KEY_T': 4,
 'SIZEOF_PTHREAD_T': 4,
 'SIZEOF_SHORT': 2,
 'SIZEOF_SIZE_T': 4,
 'SIZEOF_TIME_T': 8,
 'SIZEOF_UINTPTR_T': 4,
 'SIZEOF_VOID_P': 4,
 'SIZEOF_WCHAR_T': 4,
 'SIZEOF__BOOL': 1,
 'SOABI': 'cpython-311',
 'SRCDIRS': 'Modules   Modules/_blake2   Modules/_ctypes   Modules/_decimal   '
            'Modules/_decimal/libmpdec   Modules/_io   '
            'Modules/_multiprocessing   Modules/_sha3   Modules/_sqlite   '
            'Modules/_xxtestfuzz   Modules/cjkcodecs   Modules/expat   '
            'Objects   Parser   Programs   Python   Python/frozen_modules   '
            'Python/deepfreeze',
 'SRC_GDB_HOOKS': './Tools/gdb/libpython.py',
 'STATIC_LIBPYTHON': 1,
 'STDC_HEADERS': 1,
 'STRICT_SYSV_CURSES': "/* Don't use ncurses extensions */",
 'STRIPFLAG': '-s',
 'SUBDIRS': '',
 'SUBDIRSTOO': 'Include Lib Misc',
 'SYSLIBS': '-lm',
 'SYS_SELECT_WITH_SYS_TIME': 1,
 'TCLTK_INCLUDES': '',
 'TCLTK_LIBS': '',
 'TESTOPTS': '',
 'TESTPATH': '',
 'TESTPYTHON': './python.wasm',
 'TESTPYTHONOPTS': '',
 'TESTRUNNER': './python.wasm ./Tools/scripts/run_tests.py',
 'TESTSUBDIRS': 'ctypes/test \\',
 'TESTTIMEOUT': 1200,
 'TEST_MODULES': 'yes',
 'THREAD_STACK_SIZE': 0,
 'TIMEMODULE_LIB': 0,
 'TIME_WITH_SYS_TIME': 1,
 'TM_IN_SYS_TIME': 0,
 'TZPATH': '/usr/share/zoneinfo:/usr/lib/zoneinfo:/usr/share/lib/zoneinfo:/etc/zoneinfo',
 'UNICODE_DEPS': '\\',
 'UNIVERSALSDK': '',
 'UPDATE_FILE': './Tools/scripts/update_file.py',
 'USE_COMPUTED_GOTOS': 0,
 'VERSION': '3.11',
 'WASM_ASSETS_DIR': '"./Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python"',
 'WASM_STDLIB': '""./Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python"/local/lib/python3.11/os.py"',
 'WHEEL_PKG_DIR': '',
 'WINDOW_HAS_FLAGS': 0,
 'WITH_DECIMAL_CONTEXTVAR': 1,
 'WITH_DOC_STRINGS': 1,
 'WITH_DTRACE': 0,
 'WITH_DYLD': 0,
 'WITH_EDITLINE': 0,
 'WITH_FREELISTS': 1,
 'WITH_LIBINTL': 0,
 'WITH_NEXT_FRAMEWORK': 0,
 'WITH_PYMALLOC': 1,
 'WITH_VALGRIND': 0,
 'X87_DOUBLE_ROUNDING': 0,
 'XMLLIBSUBDIRS': 'xml xml/dom xml/etree xml/parsers xml/sax',
 'abs_builddir': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/cpython',
 'abs_srcdir': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/cpython',
 'datarootdir': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python/share',
 'exec_prefix': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python',
 'prefix': '/Users/areese/p/src/github.com/singlestore-labs/python-wasi/opt/wasi-python',
 'srcdir': '.'}
