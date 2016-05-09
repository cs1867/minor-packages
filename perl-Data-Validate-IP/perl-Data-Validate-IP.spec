%{!?perl_prefix: %define perl_prefix %(eval "`%{__perl} -V:installprefix`"; echo $installprefix)}
%{!?perl_style: %define perl_style %(eval "`%{__perl} -V:installstyle`"; echo $installstyle)}

%define disttag pSPS

Name:           perl-Data-Validate-IP
Version:        0.11
Release:        2.%{disttag}%{?dist}
Summary:        Ip validation methods
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Validate-IP/
Source0:        http://www.cpan.org/modules/by-module/Data/Data-Validate-IP-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Net::Netmask)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl
BuildRequires:  coreutils

%description
This module collects ip validation routines to make input validation, and
untainting easier and more readable.

%prep
%setup -q -n Data-Validate-IP-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
%{!?_without_checks:%{__make} test}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
/usr/*

%changelog
* Wed Aug 18 2010 Tom Throckmorton <throck@mcnc.org> - 0.11-2
- minor spec changes to enable rebuild via mock

* Mon Jun 7 2010 Aaron Brown 0.11-1
- Update to a newer version
- Remove the custom %post scripts

* Mon Jul 6 2009 Jason Zurawski 0.08-3
- Compat changes for 64 bit linux.

* Tue Mar 31 2009 Jason Zurawski 0.08-2
- Compat changes for RHEL/Fedora/CentOS/Scientific linux.

* Wed Mar 04 2009 Jason Zurawski 0.08-1
- Specfile autogenerated by cpanspec 1.77.
