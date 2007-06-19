%define pkgname libglademm
%define version 2.6.4
%define release %mkrel 1

%define libglade_version 2.6.1
%define gtkmm_version 2.6.0

%define major 1
%define api_version 2.4
%define libname		%mklibname glademm %{api_version} %{major}
%define libname_orig	%mklibname glademm %{api_version}

Name:	 	%{pkgname}%{api_version}
Summary: 	C++ interface of glade2 library
Version: 	%{version}
Release: 	%{release}
License: 	LGPL
Group:   	System/Libraries
Source:  	ftp://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
URL:     	http://gtkmm.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildRequires:	libglade2.0-devel >= %{libglade_version}
BuildRequires:	gtkmm2.4-devel >= %{gtkmm_version}
Buildrequires:	doxygen

%description
This package provides a C++ interface for glade2.  It is a subpackage
of the gnomemm project.  The interface provides a convenient interface for C++
programmers to create glade2 objects.

%package	-n %{libname}
Summary:	C++ interface of glade2 library
Group:		System/Libraries
Provides:	%{libname_orig} = %{version}-%{release}
Provides:	%{pkgname} = %{version}-%{release}

%description	-n %{libname}
This package provides a C++ interface for glade2.  It is a subpackage
of the gnomemm project.  The interface provides a convenient interface for C++
programmers to create glade2 objects.

%package	-n %{libname}-devel
Summary:	Development related files of %{pkgname}
Group:		Development/GNOME and GTK+
Provides:	%{pkgname}-devel = %{version}-%{release}
Provides:	%name-devel = %version-%release
Requires:	%{libname} = %{version}
Requires:	libglade2.0-devel >= %{libglade_version}
Requires:	gtkmm2.4-devel >= %{gtkmm_version}

%description	-n %{libname}-devel
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
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x --enable-static
%make 

### Build doc
pushd docs/reference
  perl -pi -e 's/^(HAVE_DOT.*=) YES/$1 NO/' Doxyfile
  make all
popd

%install
rm -rf %{buildroot}
%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL
%{_includedir}/*
%{_libdir}/%{pkgname}-%{api_version}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.so

%files doc
%defattr(-, root, root)
%{_docdir}/gnomemm-2.6/*
%{_datadir}/devhelp/books/*


