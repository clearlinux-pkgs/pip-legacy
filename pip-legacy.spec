Name     : pip-legacy
Version  : 10.0.1
Release  : 59
URL      : http://pypi.debian.net/pip/pip-10.0.1.tar.gz
Source0  : http://pypi.debian.net/pip/pip-10.0.1.tar.gz
Summary  : The PyPA recommended tool for installing Python packages.
Group    : Development/Tools
License  : MIT
Requires: pip-legacy-bin
Requires: pip-legacy-license
Requires: pip-legacy-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : setuptools-python

%description
===
        
        The `PyPA recommended`_ tool for installing Python packages.

%package bin
Summary: bin components for the pip-legacy package.
Group: Binaries
Requires: pip-legacy-license

%description bin
bin components for the pip-legacy package.


%package extras
Summary: extras components for the pip-legacy package.
Group: Default

%description extras
extras components for the pip-legacy package.


%package -n pip-legacypython
Summary: legacypython components for the pip-legacy package.
Group: Default
Requires: python-core

%description -n pip-legacypython
legacypython components for the pip-legacy package.


%package license
Summary: license components for the pip-legacy package.
Group: Default

%description license
license components for the pip-legacy package.


%package python
Summary: python components for the pip-legacy package.
Group: Default

%description python
python components for the pip-legacy package.


%prep
%setup -q -n pip-10.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529164644
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pip-legacy
cp LICENSE.txt %{buildroot}/usr/share/doc/pip-legacy/LICENSE.txt
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pip2
/usr/bin/pip2.7
%exclude /usr/bin/pip

%files -n pip-legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/pip-legacy/LICENSE.txt

%files python
%defattr(-,root,root,-)
