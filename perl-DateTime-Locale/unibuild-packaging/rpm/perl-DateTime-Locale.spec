Name:           perl-DateTime-Locale
Version:        1.38
Release:        1%{?dist}
Summary:        Localization support for DateTime.pm
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DateTime-Locale/
Source0:        DateTime-Locale-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.008004
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Dist::CheckConflicts) >= 0.02
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(namespace::autoclean) >= 0.19
BuildRequires:  perl(Params::ValidationCompiler) >= 0.13
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test2::Plugin::NoWarnings)
BuildRequires:  perl(Test2::Plugin::UTF8)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::File::ShareDir::Dist)
BuildRequires:  perl(Test::More) >= 1.302015
Requires:       perl(Carp)
Requires:       perl(Dist::CheckConflicts) >= 0.02
Requires:       perl(Exporter)
Requires:       perl(File::ShareDir)
Requires:       perl(File::ShareDir::Install)
Requires:       perl(File::Spec)
Requires:       perl(List::Util) >= 1.45
Requires:       perl(namespace::autoclean) >= 0.19
Requires:       perl(Params::ValidationCompiler) >= 0.13
Requires:       perl(Specio::Declare)
Requires:       perl(Specio::Library::String)
Requires:       perl(Storable)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
DateTime::Locale is primarily a factory for the various locale subclasses.
It also provides some functions for getting information on all the
available locales.

%prep
%setup -q -n DateTime-Locale-%{version}

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
%doc azure-pipelines.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md cpanfile dist.ini LICENSE LICENSE.cldr META.json perlcriticrc perltidyrc precious.toml README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed May 17 2023 Andy Lake 1.38-1
- Specfile autogenerated by cpanspec 1.78.
