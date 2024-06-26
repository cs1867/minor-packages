%{!?perl_prefix: %define perl_prefix %(eval "`%{__perl} -V:installprefix`"; echo $installprefix)}
%{!?perl_style: %define perl_style %(eval "`%{__perl} -V:installstyle`"; echo $installstyle)}

%define disttag pSPS

Name:           perl-Data-Validate-Domain
Version:        0.09
Release:        3.%{disttag}%{?dist}
Summary:        Domain validation methods
License:        CHECK(GPL+ or Artistic)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Validate-Domain/
Source0:        Data-Validate-Domain-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl-macros
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Net::Domain::TLD) >= 1.62
BuildRequires:  perl
BuildRequires:  coreutils
Provides:       perl(Data::Validate::Domain)

%description
This module collects domain validation routines to make input validation,
and untainting easier and more readable.

%prep
%setup -q -n Data-Validate-Domain-%{version}

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
* Wed Aug 18 2010 Tom Throckmorton <throck@mcnc.org> - 0.09-3
- minor spec changes to enable rebuild via mock

* Mon Jun 7 2010 Aaron Brown 0.09-2
- Remove the custom %post scripts

* Thu Jul 09 2009 Jason Zurawski 0.09-1
- Specfile autogenerated by cpanspec 1.78.
