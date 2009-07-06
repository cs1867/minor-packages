%{!?perl_prefix: %define perl_prefix %(eval "`%{__perl} -V:installprefix`"; echo $installprefix)}
%{!?perl_style: %define perl_style %(eval "`%{__perl} -V:installstyle`"; echo $installstyle)}

%define disttag pSPS

Name:           perl-Data-Validate-IP
Version:        0.08
Release:        3.%{disttag}
Summary:        Ip validation methods
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Validate-IP/
Source0:        http://www.cpan.org/modules/by-module/Data/Data-Validate-IP-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(Net::Netmask)
Requires:       perl(Test::Simple)
Requires:       perl

%description
This module collects ip validation routines to make input validation, and
untainting easier and more readable.

%prep
%setup -q -n Data-Validate-IP-%{version}

%build
%{__perl} Makefile.PL INSTALL_BASE=%{perl_prefix}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{__mv} scripts $RPM_BUILD_ROOT/tmp

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
/usr/*
/tmp/*

%post
/tmp/./perl-Data-Validate-IP_post.sh
%{__rm} /tmp/perl-Data-Validate-IP_post.sh

%changelog
* Mon Jul 6 2009 Jason Zurawski 0.08-3
- Compat changes for 64 bit linux.

* Tue Mar 31 2009 Jason Zurawski 0.08-2
- Compat changes for RHEL/Fedora/CentOS/Scientific linux.

* Wed Mar 04 2009 Jason Zurawski 0.08-1
- Specfile autogenerated by cpanspec 1.77.
