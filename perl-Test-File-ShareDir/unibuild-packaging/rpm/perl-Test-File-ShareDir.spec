Name:           perl-Test-File-ShareDir
Version:        1.001002
Release:        1%{?dist}
Summary:        Create a Fake ShareDir for your modules for testing
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-File-ShareDir/
Source0:        Test-File-ShareDir-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Tiny) >= 0.018
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Carp)
Requires:       perl(Class::Tiny)
Requires:       perl(Exporter) >= 5.57
Requires:       perl(File::Copy::Recursive)
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(parent)
Requires:       perl(Path::Tiny) >= 0.018
Requires:       perl(Scope::Guard)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Test::File::ShareDir is some low level plumbing to enable a distribution to
perform tests while consuming its own share directories in a manner similar
to how they will be once installed.

%prep
%setup -q -n Test-File-ShareDir-%{version}

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
%doc Changes dist.ini dist.ini.meta LICENSE META.json perlcritic.rc README weaver.ini
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed May 17 2023 Andy Lake 1.001002-1
- Specfile autogenerated by cpanspec 1.78.
