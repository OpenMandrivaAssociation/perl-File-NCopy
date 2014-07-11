%define	modname	File-NCopy
%define	modver	0.36

Summary:	Copies files to directories, or a single file to another file
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	12
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHORNY/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
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

