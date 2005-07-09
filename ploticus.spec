#
Summary:	Charting tool
Name:		ploticus
Version:	2.31
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://ploticus.sourceforge.net/download/pl231src.tar.gz
URL:		http://ploticus.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free, GPL, non-interactive software package for producing plots,
charts, and graphics from data. It was developed in a Unix/C
environment and runs on various Unix, Linux, and win32 systems.
ploticus is good for automated or just-in-time graph generation,
handles date and time data nicely, and has basic statistical
capabilities. It allows significant user control over colors, styles,
options and details.

%package libs
Summary:	Libraries for ploticus charting
Group:		Development/Libraries

%description libs
Libraries for ploticus charting.

%prep
%setup -n pl231src

%build
cd src
%{__make} PREFABS_DIR="/usr/share/ploticus"
%{__make} clean
%{__make} -f Makefile_api ARCOM='gcc -shared -W,soname=libploticus.so.0.0.0 -o' LIBEXT=so PREFABS_DIR="/usr/share/ploticus"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_libdir},%{_datadir}/%{name}}

install src/pl $RPM_BUILD_ROOT/%{_bindir}
install src/libploticus.so $RPM_BUILD_ROOT/%{_libdir}/libploticus.so.0
cp -a prefabs/* $RPM_BUILD_ROOT/%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig

%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*
