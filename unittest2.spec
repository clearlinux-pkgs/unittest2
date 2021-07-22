#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x89EFD588E975D6DF (rbtcollins@hp.com)
#
Name     : unittest2
Version  : 1.1.0
Release  : 78
URL      : http://pypi.debian.net/unittest2/unittest2-1.1.0.tar.gz
Source0  : http://pypi.debian.net/unittest2/unittest2-1.1.0.tar.gz
Source1  : http://pypi.debian.net/unittest2/unittest2-1.1.0.tar.gz.asc
Summary  : The new features in unittest backported to Python 2.4+.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: unittest2-bin = %{version}-%{release}
Requires: unittest2-python = %{version}-%{release}
Requires: unittest2-python3 = %{version}-%{release}
Requires: six
Requires: traceback2
BuildRequires : buildreq-distutils3
BuildRequires : linecache2-python
BuildRequires : python3-dev
BuildRequires : six
BuildRequires : traceback2
BuildRequires : traceback2-python
Patch1: remove-argparse-from-requires.patch

%description
framework in Python 2.7 and onwards. It is tested to run on Python 2.6, 2.7,
        3.2, 3.3, 3.4 and pypy.
        
        To use unittest2 instead of unittest simply replace ``import unittest`` with
        ``import unittest2``.
        
        unittest2 is maintained in a mercurial repository. The issue tracker is on

%package bin
Summary: bin components for the unittest2 package.
Group: Binaries

%description bin
bin components for the unittest2 package.


%package python
Summary: python components for the unittest2 package.
Group: Default
Requires: unittest2-python3 = %{version}-%{release}

%description python
python components for the unittest2 package.


%package python3
Summary: python3 components for the unittest2 package.
Group: Default
Requires: python3-core
Provides: pypi(unittest2)
Requires: pypi(six)
Requires: pypi(traceback2)

%description python3
python3 components for the unittest2 package.


%prep
%setup -q -n unittest2-1.1.0
cd %{_builddir}/unittest2-1.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603410789
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unit2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
