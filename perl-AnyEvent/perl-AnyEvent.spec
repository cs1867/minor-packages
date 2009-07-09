%{!?perl_prefix: %define perl_prefix %(eval "`%{__perl} -V:installprefix`"; echo $installprefix)}
%{!?perl_style: %define perl_style %(eval "`%{__perl} -V:installstyle`"; echo $installstyle)}

Autoreq: 0 

%define disttag pSPS

Name:           perl-AnyEvent
Version:        4.81
Release:        1.%{disttag}
Summary:        Provide framework for multiple event loops
License:        CHECK(Distributable)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/AnyEvent/
Source0:        http://www.cpan.org/modules/by-module/AnyEvent/AnyEvent-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
#Requires:       perl(EV) >= 3.05
#Requires:       perl(Guard) >= 1.02
Requires:       perl(JSON)
Requires:       perl(JSON::XS) >= 2.2
Requires:       perl(Net::SSLeay) >= 1.33
Requires:       perl

%description
AnyEvent provides an identical interface to multiple event loops. This
allows module authors to utilise an event loop without forcing module users
to use the same event loop (as only a single event loop can coexist
peacefully at any one time).

%prep
%setup -q -n AnyEvent-%{version}

%build
%{__perl} Makefile.PL INSTALL_BASE=%{perl_prefix}
make %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{__mv} scripts $RPM_BUILD_ROOT/tmp

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
make test

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes COPYING README
/usr/*
/tmp/*

%post
/tmp/./perl-AnyEvent_post.sh
%{__rm} /tmp/perl-AnyEvent_post.sh

%changelog
* Thu Jul 09 2009 Jason Zurawski 4.81-1
- Specfile autogenerated by cpanspec 1.78.
