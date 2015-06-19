Summary:	PaX utilities
Summary(pl.UTF-8):	Narzędzia PaX
Name:		pax-utils
Version:	1.0.3
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dev.gentoo.org/~vapier/dist/%{name}-%{version}.tar.xz
# Source0-md5:	e1c9f808a661204fbdca5e3b17da791e
URL:		http://www.gentoo.org/proj/en/hardened/pax-utils.xml
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various useful ELF related utils for ELF32, ELF64 binaries that can
check files for security relevant properties.

%description -l pl.UTF-8
Różne przydatne narzędzia dla binariów ELF32 i ELF64 sprawdzające
pliki pod kątem właściwości związanych z bezpieczeństwem.

%prep
%setup -q

%build
%{__make} %{?debug:debug} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS README TODO
%attr(755,root,root) %{_bindir}/dumpelf
%attr(755,root,root) %{_bindir}/lddtree
%attr(755,root,root) %{_bindir}/pspax
%attr(755,root,root) %{_bindir}/scanelf
%attr(755,root,root) %{_bindir}/scanmacho
%attr(755,root,root) %{_bindir}/symtree
%{_mandir}/man1/dumpelf.1*
%{_mandir}/man1/pspax.1*
%{_mandir}/man1/scanelf.1*
%{_mandir}/man1/scanmacho.1*
