%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	Ruby interface to Ncurses
Summary(pl):	Interfejs Ncurses dla Ruby
Name:		ruby-Ncurses
%define tarname ncurses-ruby
Version:	0.9.1
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://download.berlios.de/%{tarname}/%{tarname}-%{version}.tar.bz2
# Source0-md5:	cb99721b492995bb3548b700b6e86fe2
URL:		http://ncurses-ruby.berlios.de/
BuildRequires:	ruby
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This ruby extension makes most functions, constants, and external variables of
the C library ncurses accessible from the Ruby programming language.

All C functions are wrapped by module functions of a the module "Ncurses", with
exactly the same name. Additionally, C functions expecting a WINDOW* as their
first argument can also be called as methods of the "Ncurses::WINDOW" class. 

%description -l pl
Rozszerzenie do ruby, które umo¿liwia dostêp do wiêkszo¶æ fukcji, sta³ych i
zewnêtrznych zmiennych z biblioteki ncurses z poziomu jêzyka Ruby.

Wszystkie fukcje C s± dostêpne poprzez funkcje modu³u "Ncurses" pod dok³adnie
t± sam± nazw±. Dodatkowo funkcje, które spodziewaj± sie mieæ WINDOW* jako ich
pierwszy argument mog± byæ tak¿e wywo³ywane jako metody klasy "Ncurses::WINDOW"

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
%{ruby_archdir}/*.so
%{ruby_ridir}/Ncurses
