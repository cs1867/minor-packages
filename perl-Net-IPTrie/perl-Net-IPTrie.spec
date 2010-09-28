%{!?perl_prefix: %define perl_prefix %(eval "`%{__perl} -V:installprefix`"; echo $installprefix)}
%{!?perl_style: %define perl_style %(eval "`%{__perl} -V:installstyle`"; echo $installstyle)}

%define disttag pSPS

Name:           perl-Net-IPTrie
Version:        0.4
Release:        5.%{disttag}
Summary:        Perl module for building IPv4 and IPv6 address space hierarchies fast
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-IPTrie/
Source0:        http://www.cpan.org/modules/by-module/Net/Net-IPTrie-v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(Class::Struct) >= 0.63
Requires:       perl(NetAddr::IP) >= 4.007
Requires:       perl(Test::Simple)
Requires:       perl
Requires:       coreutils

BuildRequires:	perl-version
BuildRequires:	perl-NetAddr-IP

%description
This module uses a radix tree (or trie) to quickly build the hierarchy of a
given address space (both IPv4 and IPv6).  This allows the user to perform
fast subnet or routing lookups. It is implemented exclusively in Perl.

%prep
%setup -q -n Net-IPTrie-v%{version}

%build
%{__perl} Makefile.PL INSTALL_BASE=%{perl_prefix} OPTIMIZE="$RPM_OPT_FLAGS"
%{__perl} -pi -e 's/^\tLD_RUN_PATH=[^\s]+\s*/\t/' Makefile
make %{?_smp_mflags}


%install
%{__rm} -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
make test

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
/usr/*

%changelog
* Mon Jun 8 2010 Aaron Brown 0.4-5
- Use the Makefile.PL instead of Build.PL

* Mon Jun 7 2010 Aaron Brown 0.4-4
- Remove the custom %post scripts

* Mon Jul 6 2009 Jason Zurawski 0.4-3
- Compat changes for 64 bit linux.

* Tue Mar 31 2009 Jason Zurawski 0.4-2
- Compat changes for RHEL/Fedora/CentOS/Scientific linux.

* Wed Mar 04 2009 Jason Zurawski 0.4-1
- Specfile autogenerated by cpanspec 1.77.
