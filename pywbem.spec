#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pywbem
Version  : 0.12.6
Release  : 31
URL      : https://files.pythonhosted.org/packages/e1/10/eec363ccce3674118256709072427802460175ed15f1e90c21f9295c4c14/pywbem-0.12.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/e1/10/eec363ccce3674118256709072427802460175ed15f1e90c21f9295c4c14/pywbem-0.12.6.tar.gz
Summary  : pywbem - A WBEM client
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1 any option) or(at version version-2.1 your
Requires: pywbem-bin = %{version}-%{release}
Requires: pywbem-license = %{version}-%{release}
Requires: pywbem-python = %{version}-%{release}
Requires: pywbem-python3 = %{version}-%{release}
Requires: M2Crypto
Requires: PyYAML
Requires: ordereddict
Requires: pbr
Requires: ply
Requires: python-mock
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : ply
BuildRequires : python-mock

%description
PyWBEM is a Python library for making CIM operations over HTTP using the 
WBEM CIM-XML protocol.  WBEM is a manageability protocol, like SNMP,
standardised by the Distributed Management Task Force (DMTF) available
at http://www.dmtf.org/standards/wbem.

%package bin
Summary: bin components for the pywbem package.
Group: Binaries
Requires: pywbem-license = %{version}-%{release}

%description bin
bin components for the pywbem package.


%package license
Summary: license components for the pywbem package.
Group: Default

%description license
license components for the pywbem package.


%package python
Summary: python components for the pywbem package.
Group: Default
Requires: pywbem-python3 = %{version}-%{release}

%description python
python components for the pywbem package.


%package python3
Summary: python3 components for the pywbem package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pywbem package.


%prep
%setup -q -n pywbem-0.12.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551039513
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pywbem
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/pywbem/LICENSE.txt
cp packaging/debian/copyright %{buildroot}/usr/share/package-licenses/pywbem/packaging_debian_copyright
python3 -tt setup.py build  install --root=%{buildroot}
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pywbem/LICENSE.txt
/usr/share/package-licenses/pywbem/packaging_debian_copyright

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
