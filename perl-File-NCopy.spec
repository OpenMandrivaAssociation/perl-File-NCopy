%define	modname	File-NCopy
%define	modver	0.36

Summary:	Copies files to directories, or a single file to another file
Name:		perl-%{modname}
Version:	%{modver}
Release:	18
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/File-NCopy
Source0:	https://cpan.metacpan.org/authors/id/C/CH/CHORNY/File-NCopy-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl-devel

%description
Copies files to directories, or a single file to another file.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/File
%{_mandir}/man3/*

