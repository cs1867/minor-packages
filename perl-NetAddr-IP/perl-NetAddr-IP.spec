%{!?perl_prefix: %define perl_prefix %(eval "`%{__perl} -V:installprefix`"; echo $installprefix)}
%{!?perl_style: %define perl_style %(eval "`%{__perl} -V:installstyle`"; echo $installstyle)}

%define disttag pSPS

Name:           perl-NetAddr-IP
Version:        4.027
Release:        2.%{disttag}
Summary:        Manages IPv4 and IPv6 addresses and subnets
License:        CHECK(GPL+ or Artistic)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/NetAddr-IP/
Source0:        http://www.cpan.org/modules/by-module/NetAddr/NetAddr-IP-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl
Requires:       perl(Test::More)
Requires:       coreutils

%description
This module provides an object-oriented abstraction on top of IP addresses
or IP subnets, that allows for easy manipulations. Version 4.xx of
NetAdder::IP will will work older versions of Perl and does not use
Math::BigInt as in previous versions.

%prep
%setup -q -n NetAddr-IP-%{version}

%build
%{__perl} Makefile.PL INSTALL_BASE=%{perl_prefix} OPTIMIZE="$RPM_OPT_FLAGS"
%{__perl} -pi -e 's/^\tLD_RUN_PATH=[^\s]+\s*/\t/' Makefile
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README TODO
/usr/*

%changelog
* Mon Jun 7 2010 Aaron Brown 4.027-2
- Remove the custom %post scripts

* Mon Sep 28 2009 Jason Zurawski 4.027-1
- Specfile autogenerated by cpanspec 1.78.
