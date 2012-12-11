%define truename	pyosd
%define name		python-osd
%define version 0.2.14
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Python wrapper for libosd
Group:		Development/Python
License:	GPL
URL:		http://repose.cx/pyosd
Source:		%{truename}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel
BuildRequires:	libxosd-devel
Provides:	%{truename}
Obsoletes:	%{truename}

%description 
PyOSD is a python module for displaying text on your X display, much like the 
"On Screen Displays" used on TVs and some monitors.

%prep
%setup -q -n %{truename}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT  
python setup.py install --root=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT  

%files 
%dir %py_platsitedir/pyosd
%py_platsitedir/pyosd/*
%py_platsitedir/_pyosd.so
%py_platsitedir/pyosd-%{version}-*.egg-info
%defattr(-,root,root)
%doc AUTHORS README*  ChangeLog COPYING



%changelog
* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 0.2.14-5mdv2011.0
+ Revision: 591934
- Rebuild

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.2.14-4mdv2010.0
+ Revision: 442324
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.2.14-3mdv2009.0
+ Revision: 242455
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Apr 17 2007 Guillaume Bedot <littletux@mandriva.org> 0.2.14-1mdv2008.0
+ Revision: 13741
- Release 0.2.14 / python 2.5 build


* Thu Dec 22 2005 Michael Scherer <misc@mandriva.org> 0.2.12-1mdk
- New release 0.2.12

* Fri Dec 16 2005 Michael Scherer <misc@mandriva.org> 0.2.9-4mdk
- Rebuild
- use mkrel
- use a macro

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.2.9-3mdk
- Rebuild for new python

* Thu Jun 24 2004 Michael Scherer <misc@mandrake.org> 0.2.9-2mdk
- New release 0.2.9, 2mdk because 0.2.9-1mdk doesn't exist

* Sat Aug 09 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 0.2.6-1mdk
- 2.6
- changed name to python-osd
- drop patch (merged upstream)

* Mon Apr 28 2003 Götz Waschk <waschk@linux-mandrake.com> 0.2.5-5mdk
- fix distriblint warning

* Tue Feb 18 2003 Götz Waschk <waschk@linux-mandrake.com> 0.2.5-4mdk
- new xosd

* Tue Feb 04 2003 Götz Waschk <waschk@linux-mandrake.com> 0.2.5-3mdk
- rebuild for new xosd

* Sat Jan 04 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.2.5-2mdk
- rebuild

* Tue Dec 03 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.2.5-1mdk
- contributed by Pascal Terjan <CMoi@tuxfamily.org>

