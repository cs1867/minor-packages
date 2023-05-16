%{!?perl_vendorlib: %define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}

Name:           perl-JSON-Validator
Version:        1.05
Release:        1%{?dist}
Summary:        Validate data against a JSON schema
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/JSON-Validator/
Source0:        JSON-Validator-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl-macros
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Mojolicious) >= 7.15
BuildRequires:  perl(Test::More) 
BuildRequires:  perl(Data::Validate::IP)
BuildRequires:  perl-Data-Validate-Domain
BuildRequires:  perl(YAML::Syck)
Requires:       perl(Mojolicious) >= 7.15
Requires:       perl(Data::Validate::IP)
Requires:       perl-Data-Validate-Domain
Provides:       perl(JSON::Validator)

%description
JSON::Validator is a class for validating data against JSON schemas. You
might want to use this instead of JSON::Schema if you need to validate data
against draft 4 of the specification.

%prep
%setup -q -n JSON-Validator-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

#%check || :
#make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes cpanfile META.json README run-all-tests.sh
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Oct 30 2017 Andy Lake 1.05-1
- Specfile autogenerated by cpanspec 1.78.
