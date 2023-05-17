Name:           perl-Params-ValidationCompiler
Version:        0.31
Release:        1%{?dist}
Summary:        Build an optimized subroutine parameter validator once, use it forever
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Params-ValidationCompiler/
Source0:        Params-ValidationCompiler-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor) >= 1.17
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util) >= 1.29
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Specio) >= 0.14
BuildRequires:  perl(Sub::Util) >= 1.40
BuildRequires:  perl(Test2::Plugin::NoWarnings)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::More) >= 1.302015
BuildRequires:  perl(Test::Without::Module)
Requires:       perl(Carp)
Requires:       perl(Class::XSAccessor) >= 1.17
Requires:       perl(Eval::Closure)
Requires:       perl(Exception::Class)
Requires:       perl(Exporter)
Requires:       perl(List::Util) >= 1.29
Requires:       perl(Scalar::Util)
Requires:       perl(Sub::Util) >= 1.40
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module creates a customized, highly efficient parameter checking
subroutine. It can handle named or positional parameters, and can return
the parameters as key/value pairs or a list of values.

%prep
%setup -q -n Params-ValidationCompiler-%{version}

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
%doc azure-pipelines.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md cpanfile dist.ini LICENSE META.json perlcriticrc perltidyrc precious.toml README.md test-matrix.als
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed May 17 2023 Andy Lake 0.31-1
- Specfile autogenerated by cpanspec 1.78.
