# $Id$
# Authority: dag
# Tag: rfx
# ExcludeDist: el3 el4

%{?el4:%define _without_modxorg 1}

%define major_version 3.9

Summary: Cross-platform make system
Name: cmake
Version: %{major_version}.1
Release: 1%{?dist}
License: BSD
Group: Development/Tools
URL: http://www.cmake.org/

Source0: http://www.cmake.org/files/v%{major_version}/cmake-%{version}.tar.gz
Source1: macros.cmake
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: curl-devel
BuildRequires: expat-devel
BuildRequires: gcc-c++
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
CMake is used to control the software compilation process using simple 
platform and compiler independent configuration files. CMake generates 
native makefiles and workspaces that can be used in the compiler 
environment of your choice. CMake is quite sophisticated: it is possible 
to support complex environments requiring system configuration, pre-processor 
generation, code generation, and template instantiation.

%prep
%setup

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
./bootstrap \
    --prefix="%{_prefix}" \
    --init="cmake.init" \
    --datadir="/share/cmake" \
    --docdir="/doc-rpm/" \
    --mandir="/share/man"
#    --system-libs
%{__make} %{?_smp_mflags} VERBOSE="1"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.cmake
%{__perl} -pi -e 's|@@CMAKE_VERSION@@|%{version}|' %{buildroot}%{_sysconfdir}/rpm/macros.cmake
%{__install} -Dp -m0644 Auxiliary/cmake-mode.el %{buildroot}%{_datadir}/emacs/site-lisp/cmake-mode.el

### Clean up buildroot
%{__mv} -f %{buildroot}%{_prefix}/doc-rpm/ .
find %{buildroot}%{_datadir}/cmake/Modules/ -type f | xargs chmod -x

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc-rpm/*
%config(noreplace) %{_sysconfdir}/rpm/macros.cmake
%{_bindir}/*
%{_datadir}/cmake/
%{_datadir}/aclocal/*
%dir %{_datadir}/emacs/
%dir %{_datadir}/emacs/site-lisp/
%{_datadir}/emacs/site-lisp/cmake-mode.el

%changelog
* Fri Aug 03 2012 Steve Huff <shuff@vecna.org> - 2.8.8-1
- Update to version 2.8.8 (moved to RFX).

* Sat May 05 2007 Dag Wieers <dag@wieers.com> - 2.6.4-1
- Initial package. (using DAR)
