#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pywbem
Version  : 0.11.0
Release  : 13
URL      : https://github.com/pywbem/pywbem/archive/v0.11.0.tar.gz
Source0  : https://github.com/pywbem/pywbem/archive/v0.11.0.tar.gz
Summary  : Python WBEM Client
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1
Requires: pywbem-bin
Requires: pywbem-python3
Requires: pywbem-license
Requires: pywbem-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
PyWBEM is a Python library for making CIM operations over HTTP using the 
WBEM CIM-XML protocol.  WBEM is a manageability protocol, like SNMP,
standardised by the Distributed Management Task Force (DMTF) available
at http://www.dmtf.org/standards/wbem.

%package bin
Summary: bin components for the pywbem package.
Group: Binaries
Requires: pywbem-license

%description bin
bin components for the pywbem package.


%package doc
Summary: doc components for the pywbem package.
Group: Documentation

%description doc
doc components for the pywbem package.


%package license
Summary: license components for the pywbem package.
Group: Default

%description license
license components for the pywbem package.


%package python
Summary: python components for the pywbem package.
Group: Default
Requires: pywbem-python3

%description python
python components for the pywbem package.


%package python3
Summary: python3 components for the pywbem package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pywbem package.


%prep
%setup -q -n pywbem-0.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530383077
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pywbem
cp pywbem/LICENSE.txt %{buildroot}/usr/share/doc/pywbem/pywbem_LICENSE.txt
cp packaging/debian/copyright %{buildroot}/usr/share/doc/pywbem/packaging_debian_copyright
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mof_compiler
/usr/bin/mof_compiler.bat
/usr/bin/wbemcli
/usr/bin/wbemcli.bat
/usr/bin/wbemcli.py

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/pywbem/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/pywbem/pywbem_LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
