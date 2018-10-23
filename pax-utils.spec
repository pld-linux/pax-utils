Summary:	PaX utilities
Summary(pl.UTF-8):	Narzędzia PaX
Name:		pax-utils
Version:	1.2.3
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dev.gentoo.org/~slyfox/distfiles/%{name}-%{version}.tar.xz
# Source0-md5:	f7cb7348dd4577389ccdd082bb18c162
URL:		https://wiki.gentoo.org/wiki/Hardened/PaX_Utilities
Requires:	python-elftools
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
%doc BUGS README.md TODO
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
