Name:           perl-IPC-Run
Version:        20220807.0
Release:        1%{?dist}
Summary:        System() and background procs w/ piping, redirs, ptys (Unix, Win32)
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IPC-Run/
Source0:        IPC-Run-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Patch0:         run.t.patch
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Pty) >= 1.08
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Readonly::Array)
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(IO::Pty) >= 1.08
Requires:       perl(Readonly)
Requires:       perl(Test::More) >= 0.47
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
IPC::Run allows you to run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are both
supported and may be mixed.

%prep
%setup -q -n IPC-Run-%{version}
%patch0 -p0

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
%doc Changelog LICENSE META.json README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri May 19 2023 Andy Lake 20220807.0-1
- Specfile autogenerated by cpanspec 1.78.
