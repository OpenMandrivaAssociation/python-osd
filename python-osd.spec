%define truename	pyosd
%define name		python-osd
%define version 0.2.12
%define release %mkrel 1

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
%defattr(-,root,root)
%doc AUTHORS README*  ChangeLog COPYING
%py_libdir/site-packages/_pyosd.so
%dir %py_libdir/site-packages/pyosd/
%py_libdir/site-packages/pyosd/__init__.py
%py_libdir/site-packages/pyosd/__init__.pyc
%py_libdir/site-packages/pyosd/daemon.py
%py_libdir/site-packages/pyosd/daemon.pyc

