%define pkgname libglademm
%define version 2.6.7
%define release %mkrel 7

%define libglade_version 2.6.1
%define gtkmm_version 2.6.0

%define major 1
%define api_version 2.4
%define libname		%mklibname glademm %{api_version} %{major}
%define libname_orig	%mklibname glademm %{api_version}
%define develname %mklibname -d glademm %{api_version}

Name:	 	%{pkgname}%{api_version}
Summary: 	C++ interface of glade2 library
Version: 	%{version}
Release: 	%{release}
License: 	LGPLv2+
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

%package	-n %develname
Summary:	Development related files of %{pkgname}
Group:		Development/GNOME and GTK+
Provides:	%{pkgname}-devel = %{version}-%{release}
Provides:	%name-devel = %version-%release
Requires:	%{libname} = %{version}
Requires:	libglade2.0-devel >= %{libglade_version}
Requires:	gtkmm2.4-devel >= %{gtkmm_version}
Obsoletes: %mklibname -d glademm 2.4 1

%description	-n %develname
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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL
%{_libdir}/libglademm-%{api_version}.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL
%{_includedir}/*
%{_libdir}/%{pkgname}-%{api_version}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a
#%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.so

%files doc
%defattr(-, root, root)
%{_docdir}/gnomemm-2.6/*
%{_datadir}/devhelp/books/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.6.7-5mdv2011.0
+ Revision: 661464
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 2.6.7-4mdv2011.0
+ Revision: 602552
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.6.7-3mdv2010.1
+ Revision: 520833
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.6.7-2mdv2010.0
+ Revision: 425550
- rebuild

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.7-1mdv2009.0
+ Revision: 286534
- new version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.6.6-2mdv2009.0
+ Revision: 222596
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Feb 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.6-1mdv2008.1
+ Revision: 164910
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 05 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.5-1mdv2008.1
+ Revision: 95564
- new version
- new devel name

* Mon Jul 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.4-2mdv2008.0
+ Revision: 50525
- rebuild for new glib2.0

* Tue Jun 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.4-1mdv2008.0
+ Revision: 41506
- new version
- bump deps


* Tue Jan 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.3-2mdv2007.0
+ Revision: 103070
- Import libglademm2.4

* Tue Jan 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.3-2mdv2007.1
- Rebuild

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 2.6.3-1mdv2007.0
- New release 2.6.3

* Thu Feb 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.2-1mdk
- New release 2.6.2
- use mkrel

* Sun Oct 09 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.1-1mdk
- New release 2.6.1

* Tue May 10 2005 Götz Waschk <waschk@mandriva.org> 2.6.0-2mdk
- fix devel provides

* Mon Mar 07 2005 Götz Waschk <waschk@linux-mandrake.com> 2.6.0-1mdk
- requires new gtkmm
- New release 2.6.0

* Wed Feb 23 2005 Götz Waschk <waschk@linux-mandrake.com> 2.4.2-1mdk
- source URL
- New release 2.4.2

* Mon Jun 21 2004 Abel Cheung <deaddog@deaddog.org> 2.4.1-2mdk 
- Rebuild against new gtkmm
- fix source URL

* Tue Jun 08 2004 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.4.1-1mdk
- fix source URL
- reenable libtoolize
- New release 2.4.1

* Thu Apr 29 2004 Abel Cheung <deaddog@deaddog.org> 2.4.0-1mdk
- New major release

* Thu Apr 29 2004 Abel Cheung <deaddog@deaddog.org> 2.2.0-1mdk
- New version
- Remove all patches (upstream or not needed)
- Only provides libglademm2.0(-devel), so other packages won't
  require libglademm without indicating API version
- Please use UTF-8 for spec in the future

