%define	upstream_name	 File-NCopy
%define	upstream_version 0.36

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Copies files to directories, or a single file to another file
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHORNY/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Copies files to directories, or a single file to another file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/File


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.360.0-4mdv2012.0
+ Revision: 765247
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.360.0-3
+ Revision: 763761
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.360.0-2
+ Revision: 667143
- mass rebuild

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.360.0-1mdv2010.1
+ Revision: 407692
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.36-3mdv2009.1
+ Revision: 351751
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.36-2mdv2009.0
+ Revision: 223753
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Nov 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2008.1
+ Revision: 113398
- update to new version 0.36

* Sun Apr 29 2007 Olivier Thauvin <nanardon@mandriva.org> 0.35-1mdv2008.0
+ Revision: 19146
- 0.35


* Tue Apr 11 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.34-2mdk
- Rebuild, fix url, summary, description and license, use mkrel

* Wed Apr 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.34-1mdk
- 0.34
- add url tag

* Wed Aug 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.32-8mdk
- rebuild for new perl
- drop Prefix tag
- drop Distribution tag
- don't use PREFIX
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.32-7mdk
- rebuild for new auto{prov,req}

