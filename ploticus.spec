# TODO: optflags
Summary:	Charting tool
Summary(pl.UTF-8):	Narzędzie do wykresów
Name:		ploticus
Version:	2.31
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://ploticus.sourceforge.net/download/pl231src.tar.gz
# Source0-md5:	70712f7f41484db3bfd9210ae7742762
URL:		http://ploticus.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free, GPL, non-interactive software package for producing plots,
charts, and graphics from data. It was developed in a Unix/C
environment and runs on various Unix, Linux, and Win32 systems.
ploticus is good for automated or just-in-time graph generation,
handles date and time data nicely, and has basic statistical
capabilities. It allows significant user control over colors, styles,
options and details.

%description -l pl.UTF-8
Darmowy, wydany na GPL pakiet oprogramowania nieinteraktywnego do
tworzenia rysunków, wykresów i grafiki z danych. Został stworzony w
środowisku Unix/C i działa na różnych systemach uniksowych, pod
Linuksem oraz Win32. ploticus jest dobry do generowania wykresów
zautomatyzowanego lub w czasie rzeczywistym, obsługuje dobrze dane
dotyczące daty i czasu, ma podstawowe możliwości statystyczne. Daje
użytkownikowi znaczącą kontrolę nad kolorami, stylami, opcjami i
szczegółami.

%package libs
Summary:	Libraries for ploticus charting
Summary(pl.UTF-8):	Biblioteki do oprogramowania ploticus
Group:		Libraries

%description libs
Libraries for ploticus charting.

%description libs -l pl.UTF-8
Biblioteki do oprogramowania ploticus.

%prep
%setup -n pl231src

%build
cd src
%{__make} \
	PREFABS_DIR="/usr/share/ploticus"
%{__make} clean
%{__make} -f Makefile_api \
	ARCOM='%{__cc} -shared -W,soname=libploticus.so.0.0.0 -o' \
	LIBEXT=so \
	PREFABS_DIR="/usr/share/ploticus"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir}/%{name}}

install src/pl $RPM_BUILD_ROOT%{_bindir}
install src/libploticus.so $RPM_BUILD_ROOT%{_libdir}/libploticus.so.0
cp -a prefabs/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*
