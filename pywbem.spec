#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pywbem
Version  : 0.12.6
Release  : 16
URL      : https://files.pythonhosted.org/packages/e1/10/eec363ccce3674118256709072427802460175ed15f1e90c21f9295c4c14/pywbem-0.12.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/e1/10/eec363ccce3674118256709072427802460175ed15f1e90c21f9295c4c14/pywbem-0.12.6.tar.gz
Summary  : pywbem - A WBEM client
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1
Requires: pywbem-bin
Requires: pywbem-python3
Requires: pywbem-license
Requires: pywbem-python
Requires: PyYAML
Requires: ordereddict
Requires: pbr
Requires: ply
Requires: python-mock
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : ply
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Pywbem is a WBEM client, written in pure Python. It supports Python 2 and
        Python 3. Pywbem also contains a WBEM indication listener.
        
        A WBEM client allows issuing operations to a WBEM server, using the
        `CIM/WBEM standards`_ defined by the DMTF, for the purpose of performing
        systems management tasks. A WBEM indication listener is used to wait for
        and process notifications emitted by a WBEM server, also for the purpose
        of systems management.
        
        CIM/WBEM infrastructure is used for a wide variety of systems management
        tasks in the industry.
        
        For more information on pywbem, see the `pywbem readme`_, and the
        `pywbem documentation`_.

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
%setup -q -n pywbem-0.12.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536879140
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pywbem
cp LICENSE.txt %{buildroot}/usr/share/doc/pywbem/LICENSE.txt
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
/usr/share/doc/pywbem/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
