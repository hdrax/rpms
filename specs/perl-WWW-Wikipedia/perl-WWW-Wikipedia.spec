# $Id$
# Authority: dries
# Upstream: Ed Summers <ehs$pobox,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Wikipedia

Summary: Lookup an entry in the wikipedia
Name: perl-WWW-Wikipedia
Version: 1.92
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Wikipedia/

Source: http://search.cpan.org//CPAN/authors/id/B/BR/BRICAS/WWW-Wikipedia-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Lookup an entry in the wikipedia.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/WWW::Wikipedia*
%doc %{_mandir}/man1/wikipedia*
%{_bindir}/wikipedia
%{perl_vendorlib}/WWW/Wikipedia.pm
%{perl_vendorlib}/WWW/Wikipedia/

%changelog
* Thu Jan 04 2007 Dries Verachtert <dries@ulyssis.org> - 1.92-1
- Updated to release 1.92.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.91-1
- Initial package.

