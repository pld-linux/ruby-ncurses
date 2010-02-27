%define pkgname ncurses
Summary:	Ruby interface to Ncurses
Summary(pl.UTF-8):	Interfejs Ncurses dla Ruby
Name:		ruby-%{pkgname}
Version:	1.2.4
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://download.berlios.de/ncurses-ruby/%{pkgname}-ruby-%{version}.tar.bz2
# Source0-md5:	8a3e0ed33ac245241b6afd911520c205
Patch0:		%{name}-utf8.patch
URL:		http://ncurses-ruby.berlios.de/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.8.4-5
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-Ncurses
Provides:	ruby-Ncurses
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

%prep
%setup -q -n %{pkgname}-ruby-%{version}
%patch0 -p1

%build
ruby extconf.rb

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncursesw -fPIC"

rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_ridir}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README rdoc
%{ruby_sitelibdir}/*.rb
%attr(755,root,root) %{ruby_sitearchdir}/*.so
%{ruby_ridir}/Ncurses
