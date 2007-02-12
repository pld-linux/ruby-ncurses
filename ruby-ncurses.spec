%define tarname ncurses-ruby
Summary:	Ruby interface to Ncurses
Summary(pl.UTF-8):	Interfejs Ncurses dla Ruby
Name:		ruby-Ncurses
Version:	0.9.1
Release:	4
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://download.berlios.de/%{tarname}/%{tarname}-%{version}.tar.bz2
# Source0-md5:	cb99721b492995bb3548b700b6e86fe2
URL:		http://ncurses-ruby.berlios.de/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.8.4-5
%{?ruby_mod_ver_requires_eq}
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
%setup -q -n %{tarname}-%{version}

%build
ruby extconf.rb

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_archdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}
install ncurses.so $RPM_BUILD_ROOT%{ruby_archdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README rdoc
%{ruby_rubylibdir}/*.rb
%attr(755,root,root) %{ruby_archdir}/*.so
%{ruby_ridir}/Ncurses
