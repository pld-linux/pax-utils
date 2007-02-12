Summary:	PaX utilities
Summary(pl.UTF-8):	NarzÄdzia PaX
Name:		pax-utils
Version:	0.1.13
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dev.gentoo.org/~solar/pax/%{name}-%{version}.tar.bz2
# Source0-md5:	5f09df47a16e83462384b44b75310539
URL:		http://www.gentoo.org/proj/en/hardened/pax-utils.xml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various useful ELF related utils for ELF32, ELF64 binaries that can
check files for security relevant properties.

%description -l pl.UTF-8
RĂłĹźne przydatne narzÄdzia dla binariĂłw ELF32 i ELF64 sprawdzajÄce
pliki pod kÄtem wĹaĹciwoĹci zwiÄzanych z bezpieczeĹstwem.

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

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}/{BUGS,README,TODO}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS README TODO
%attr(755,root,root) %{_bindir}/dumpelf
%attr(755,root,root) %{_bindir}/pspax
%attr(755,root,root) %{_bindir}/scanelf
%{_mandir}/man1/dumpelf.1*
%{_mandir}/man1/pspax.1*
%{_mandir}/man1/scanelf.1*
