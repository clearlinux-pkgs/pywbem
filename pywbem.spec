#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pywbem
Version  : 1.2.0
Release  : 63
URL      : https://files.pythonhosted.org/packages/5d/2b/67680f775ea65b197c4db6a51e0d9bffcf24031f75866ece4f4d8a1e9e97/pywbem-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5d/2b/67680f775ea65b197c4db6a51e0d9bffcf24031f75866ece4f4d8a1e9e97/pywbem-1.2.0.tar.gz
Summary  : pywbem - A WBEM client
Group    : Development/Tools
License  : LGPL-2.1
Requires: pywbem-bin = %{version}-%{release}
Requires: pywbem-license = %{version}-%{release}
Requires: pywbem-python = %{version}-%{release}
Requires: pywbem-python3 = %{version}-%{release}
Requires: PyYAML
Requires: nocasedict
Requires: nocaselist
Requires: ply
Requires: python-mock
Requires: requests
Requires: six
Requires: urllib3
Requires: yamlloader
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : nocasedict
BuildRequires : nocaselist
BuildRequires : ply
BuildRequires : python-mock
BuildRequires : requests
BuildRequires : six
BuildRequires : urllib3
BuildRequires : yamlloader

%description
.. # Note: On Pypi, variable substitution with raw content is not enabled, so
.. # we have to specify the package version directly in the links.

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
Provides: pypi(pywbem)
Requires: pypi(nocasedict)
Requires: pypi(nocaselist)
Requires: pypi(ply)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(six)
Requires: pypi(urllib3)
Requires: pypi(yamlloader)

%description python3
python3 components for the pywbem package.


%prep
%setup -q -n pywbem-1.2.0
cd %{_builddir}/pywbem-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619731642
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pywbem
cp %{_builddir}/pywbem-1.2.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pywbem/caeb68c46fa36651acf592771d09de7937926bb3
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pywbem/caeb68c46fa36651acf592771d09de7937926bb3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
