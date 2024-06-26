Name:           perl-B-Hooks-EndOfScope
Version:        0.26
Release:        1%{?dist}
Summary:        Execute code after a scope finished compilation
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/B-Hooks-EndOfScope/
Source0:        B-Hooks-EndOfScope-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006001
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Implementation) >= 0.05
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter::Progressive) >= 0.001006
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Module::Implementation) >= 0.05
Requires:       perl(Scalar::Util)
Requires:       perl(Sub::Exporter::Progressive) >= 0.001006
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module allows you to execute code when perl finished compiling the
surrounding scope.

%prep
%setup -q -n B-Hooks-EndOfScope-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes CONTRIBUTING dist.ini LICENCE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri May 19 2023 Andy Lake 0.26-1
- Specfile autogenerated by cpanspec 1.78.
