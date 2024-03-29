#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pywbem
Version  : 1.4.0
Release  : 71
URL      : https://files.pythonhosted.org/packages/34/1c/1c595fe36d09d97ab0a99b3557fff1439139b5ddafb1c5e796bc220ea2cd/pywbem-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/34/1c/1c595fe36d09d97ab0a99b3557fff1439139b5ddafb1c5e796bc220ea2cd/pywbem-1.4.0.tar.gz
Summary  : pywbem - A WBEM client
Group    : Development/Tools
License  : LGPL-2.1
Requires: pywbem-bin = %{version}-%{release}
Requires: pywbem-license = %{version}-%{release}
Requires: pywbem-python = %{version}-%{release}
Requires: pywbem-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : ply
BuildRequires : pypi(mock)
BuildRequires : pypi(nocasedict)
BuildRequires : pypi(nocaselist)
BuildRequires : pypi(ply)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
BuildRequires : pypi(six)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(yamlloader)
BuildRequires : python-mock

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
Requires: pypi(mock)
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
%setup -q -n pywbem-1.4.0
cd %{_builddir}/pywbem-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641237160
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pywbem
cp %{_builddir}/pywbem-1.4.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pywbem/caeb68c46fa36651acf592771d09de7937926bb3
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
