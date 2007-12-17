%define	module	File-NCopy
%define	name	perl-%{module}
%define	version	0.36
%define	release	%mkrel 1

Summary: 	Copies files to directories, or a single file to another file
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
BuildArch:	noarch
Source0: 	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%module/
BuildRequires:	perl-devel

%description
Copies files to directories, or a single file to another file.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%check
%__make test

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/File

