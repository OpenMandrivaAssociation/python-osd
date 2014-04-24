%define truename	pyosd
%define name		python-osd
%define version 0.2.14
%define release 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Python wrapper for libosd
Group:		Development/Python
License:	GPL
URL:		http://repose.cx/pyosd
Source:		%{truename}-%{version}.tar.bz2
BuildRequires:	pkgconfig(python)
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
python setup.py install --root=$RPM_BUILD_ROOT   

%files 
%dir %py_platsitedir/pyosd
%py_platsitedir/pyosd/*
%py_platsitedir/_pyosd.so
%py_platsitedir/pyosd-%{version}-*.egg-info
%defattr(-,root,root)
%doc AUTHORS README*  ChangeLog COPYING



