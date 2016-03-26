%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_lto 1

%define pkgname	libglademm
%define api	2.4
%define major	1
%define libname	%mklibname glademm %{api} %{major}
%define devname %mklibname -d glademm %{api}

Summary:	C++ interface of glade2 library
Name:		%{pkgname}%{api}
Version:	2.6.7
Release:	23
License:	LGPLv2+
Group:		System/Libraries
Url:		http://gtkmm.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libglademm/%{url_ver}/%{pkgname}-%{version}.tar.bz2

Buildrequires:	doxygen
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(libglade-2.0)

%description
This package provides a C++ interface for glade2.  It is a subpackage
of the gnomemm project.  The interface provides a convenient interface for C++
programmers to create glade2 objects.

%package	-n %{libname}
Summary:	C++ interface of glade2 library
Group:		System/Libraries
Provides:	%{pkgname} = %{version}-%{release}

%description	-n %{libname}
This package provides a C++ interface for glade2.  It is a subpackage
of the gnomemm project.  The interface provides a convenient interface for C++
programmers to create glade2 objects.

%package	-n %{devname}
Summary:	Development related files of %{pkgname}
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%mklibname -d glademm 2.4 1

%description	-n %{devname}
This package provides headers and various development files needed for
compiling or developing applications that use Glade 2 C++ interface.

%package	doc
Summary:	Documentation for %{pkgname} library
Group:		Books/Other

%description	doc
This package provides API documentation of %{pkgname} library, which
is part of gnomemm project that provides C++ interface for GNOME libraries.
The documents can be browsed via devhelp, an API documentation viewer.

%prep
%setup -qn %{pkgname}-%{version}

%build
export CXXFLAGS="%{optflags} -std=gnu++11"
%configure2_5x \
	--disable-static
%make 

### Build doc
pushd docs/reference
  sed -i -e 's/^(HAVE_DOT.*=) YES/$1 NO/' Doxyfile
  make all
popd

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libglademm-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog INSTALL
%{_includedir}/*
%{_libdir}/%{pkgname}-%{api}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%files doc
%{_docdir}/gnomemm-2.6/*
%{_datadir}/devhelp/books/*

