Name:           perl-JSON-XS
Version:        4.03
Release:        1%{?dist}
Summary:        JSON serialising/deserialising, done correctly and fast
License:        CHECK(Distributable)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/JSON-XS/
Source0:        JSON-XS-%{version}.tar.gz
Patch0:         Makefile.PL.patch
Patch1:         META.json.patch
Patch2:         META.yml.patch 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gcc
BuildRequires:  perl(common::sense)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Types::Serialiser)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
Requires:       perl(common::sense)
Requires:       perl(Types::Serialiser)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be correct and its secondary goal is to be fast. To
reach the latter goal it was written in C.

%prep
%setup -q -n JSON-XS-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes COPYING META.json README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/JSON*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/json_xs

%changelog
* Tue May 09 2023 Andy Lake 4.03-1
- Specfile autogenerated by cpanspec 1.78.
