#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	ParamParser
Summary:	Class::ParamParser - complex parameter list parsing
Summary(pl):	Class::ParamParser - analizowanie z�o�onych list parametr�w
Name:		perl-Class-ParamParser
Version:	1.041
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	06ea167ae52c80629249244f93fbccbd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl 5 object class implements two methods which inherited
classes can use to tidy up parameter lists for their own methods and
functions. The two methods differ in that one returns a HASH ref
containing named parameters and the other returns an ARRAY ref
containing positional parameters.

%description -l pl
Ta klasa obiektu Perla 5 implementuje dwie metody, z kt�rych
odziedziczone klasy mog� korzysta� do oczyszczenia list parametr�w dla
ich w�asnych metod i funkcji. Metody r�ni� si� tym, �e jedna zwraca
referencj� do hasza zawieraj�cego parametry nazwane, a druga zwraca
referencj� do tablicy zawieraj�cej parametry pozycyjne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog ReadMe
%{perl_vendorlib}/Class/ParamParser.pm
%{_mandir}/man3/*
