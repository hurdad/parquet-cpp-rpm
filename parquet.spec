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
BuildRequires:  cmake 
BuildRequires:  zlib-devel
Requires:		apache-arrow >= 0.2.0
AutoReqProv: 	no

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
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64
rm -rf $RPM_BUILD_ROOT/home

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

%files devel
%defattr(-,root,root,-)
%{_includedir}
%{_libdir}/libparquet.a

%changelog