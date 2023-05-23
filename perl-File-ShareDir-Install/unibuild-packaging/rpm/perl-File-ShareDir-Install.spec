Name:           perl-File-ShareDir-Install
Version:        0.14
Release:        1%{?dist}
Summary:        Install shared files
License:        Distributable, see LICENSE
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-ShareDir-Install/
Source0:        File-ShareDir-Install-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
File::ShareDir::Install allows you to install read-only data files from a
distribution. It is a companion module to File::ShareDir, which allows you
to locate these files after installation.

%prep
%setup -q -n File-ShareDir-Install-%{version}

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
%doc Changes CONTRIBUTING dist.ini LICENSE META.json README testrules.yml
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed May 17 2023 Andy Lake 0.14-1
- Specfile autogenerated by cpanspec 1.78.