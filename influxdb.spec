#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : influxdb
Version  : 5.3.1
Release  : 49
URL      : https://files.pythonhosted.org/packages/86/4f/a9c524576677c1694b149e09d4fd6342e4a1d9a5f409e437168a14d6d150/influxdb-5.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/86/4f/a9c524576677c1694b149e09d4fd6342e4a1d9a5f409e437168a14d6d150/influxdb-5.3.1.tar.gz
Summary  : InfluxDB client
Group    : Development/Tools
License  : MIT
Requires: influxdb-license = %{version}-%{release}
Requires: influxdb-python = %{version}-%{release}
Requires: influxdb-python3 = %{version}-%{release}
Requires: msgpack
Requires: python-dateutil
Requires: pytz
Requires: requests
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : cov-core-python
BuildRequires : coverage-python
BuildRequires : funcsigs-python
BuildRequires : msgpack
BuildRequires : nose-python
BuildRequires : python-dateutil
BuildRequires : python-dateutil-python
BuildRequires : python-mock-python
BuildRequires : pytz
BuildRequires : pytz-python
BuildRequires : requests
BuildRequires : requests-mock-python
BuildRequires : requests-python
BuildRequires : six

%description
===============

%package license
Summary: license components for the influxdb package.
Group: Default

%description license
license components for the influxdb package.


%package python
Summary: python components for the influxdb package.
Group: Default
Requires: influxdb-python3 = %{version}-%{release}

%description python
python components for the influxdb package.


%package python3
Summary: python3 components for the influxdb package.
Group: Default
Requires: python3-core
Provides: pypi(influxdb)
Requires: pypi(msgpack)
Requires: pypi(python_dateutil)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(six)

%description python3
python3 components for the influxdb package.


%prep
%setup -q -n influxdb-5.3.1
cd %{_builddir}/influxdb-5.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605462754
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/influxdb
cp %{_builddir}/influxdb-5.3.1/LICENSE %{buildroot}/usr/share/package-licenses/influxdb/00911d51b2df5ac0cc09dc2f5549a55945db02f0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/influxdb/00911d51b2df5ac0cc09dc2f5549a55945db02f0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
