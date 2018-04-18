%define debug_package %{nil}
Name:           apache-parquet-cpp
Version:    	%{VERSION}
Release:        1%{?dist}
Summary:        A C++ library to read and write the Apache Parquet columnar data format.
Group:      	System Environment/Libraries
License:    	Apache 2.0
URL:            https://parquet.apache.org/
Source:     	%{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  boost-static
BuildRequires:  boost-regex
BuildRequires:  bison 
BuildRequires:  flex 
BuildRequires:  gcc-c++ 
BuildRequires:  cmake >= 3.2.0
BuildRequires:  zlib-devel
BuildRequires:	apache-arrow-cpp-devel >= 0.8.0
Requires:       zlib
Requires:       boost-regex
Requires:	apache-arrow-cpp >= 0.8.0

%description
A C++ library to read and write the Apache Parquet columnar data format.

%package devel
Summary:	%{name} development package
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for %{name}.

%prep
%setup -n parquet-cpp-%{name}-%{version}

%build
export PARQUET_TEST_DATA=`pwd`/data
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%check
make unittest

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc CHANGELOG LICENSE.txt NOTICE.txt README.md
%{_libdir}/libparquet.so*
%{_datarootdir}/parquet-cpp

%files devel
%defattr(-,root,root,-)
%{_includedir}
%{_libdir}/libparquet.a
%{_libdir}/pkgconfig

%changelog
