%define pkgname ncurses
Summary:	Ruby interface to Ncurses
Summary(pl.UTF-8):	Interfejs Ncurses dla Ruby
Name:		ruby-%{pkgname}
Version:	1.3.1
Release:	3
License:	Ruby-alike
Group:		Development/Languages
Source0:	https://sourceforge.net/projects/ncurses-ruby.berlios/files/%{pkgname}-ruby-%{version}.tar.bz2
# Source0-md5:	63fd3d09a51cdd745e1ed37f85621ea2
Patch0:		%{name}-utf8.patch
Patch1:		format-security.patch
Patch2:		ruby-ncurses-fix-missing-tz-prototypes.patch
URL:		https://sourceforge.net/projects/ncurses-ruby.berlios/
BuildRequires:	ncurses-devel
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-devel
Provides:	ruby-Ncurses
Obsoletes:	ruby-Ncurses
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This ruby extension makes most functions, constants, and external
variables of the C library ncurses accessible from the Ruby
programming language.

All C functions are wrapped by module functions of a the module
"Ncurses", with exactly the same name. Additionally, C functions
expecting a WINDOW* as their first argument can also be called as
methods of the "Ncurses::WINDOW" class.

%description -l pl.UTF-8
Rozszerzenie do ruby, które umożliwia dostęp do większość funkcji,
stałych i zewnętrznych zmiennych biblioteki ncurses z poziomu języka
Ruby.

Wszystkie funkcje C są dostępne poprzez funkcje modułu "Ncurses" pod
dokładnie tymi samymi nazwami. Dodatkowo funkcje, które spodziewają
się mieć WINDOW* jako ich pierwszy argument mogą być także wywoływane
jako metody klasy "Ncurses::WINDOW".

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-ruby-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
ruby extconf.rb \
	--vendor

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncursesw -fPIC"

rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_ridir},%{ruby_rdocdir}}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruby_vendorlibdir}/ncurses.rb
%{ruby_vendorlibdir}/ncurses_sugar.rb
%attr(755,root,root) %{ruby_vendorarchdir}/ncurses_bin.so

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Ncurses
