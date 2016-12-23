#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : unittest2
Version  : 1.1.0
Release  : 30
URL      : https://pypi.python.org/packages/source/u/unittest2/unittest2-1.1.0.tar.gz
Source0  : https://pypi.python.org/packages/source/u/unittest2/unittest2-1.1.0.tar.gz
Summary  : The new features in unittest backported to Python 2.4+.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: unittest2-bin
Requires: unittest2-python
BuildRequires : argparse-python
BuildRequires : linecache2-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : traceback2-python
Patch1: remove-argparse-from-requires.patch

%description
unittest2 is a backport of the new features added to the unittest testing
framework in Python 2.7 and onwards. It is tested to run on Python 2.6, 2.7,
3.2, 3.3, 3.4 and pypy.

%package bin
Summary: bin components for the unittest2 package.
Group: Binaries

%description bin
bin components for the unittest2 package.


%package python
Summary: python components for the unittest2 package.
Group: Default
Requires: argparse-python
Requires: traceback2-python

%description python
python components for the unittest2 package.


%prep
%setup -q -n unittest2-1.1.0
%patch1 -p1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unit2

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
