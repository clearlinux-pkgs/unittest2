#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x89EFD588E975D6DF (rbtcollins@hp.com)
#
Name     : unittest2
Version  : 1.1.0
Release  : 34
URL      : http://pypi.debian.net/unittest2/unittest2-1.1.0.tar.gz
Source0  : http://pypi.debian.net/unittest2/unittest2-1.1.0.tar.gz
Source99 : https://pypi.python.org/packages/source/u/unittest2/unittest2-1.1.0.tar.gz.asc
Summary  : The new features in unittest backported to Python 2.4+.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: unittest2-bin
Requires: unittest2-legacypython
Requires: unittest2-python
Requires: argparse
Requires: six
Requires: traceback2
BuildRequires : argparse
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
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


%package legacypython
Summary: legacypython components for the unittest2 package.
Group: Default

%description legacypython
legacypython components for the unittest2 package.


%package python
Summary: python components for the unittest2 package.
Group: Default
Requires: unittest2-legacypython

%description python
python components for the unittest2 package.


%prep
%setup -q -n unittest2-1.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1504999299
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1504999299
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unit2

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
