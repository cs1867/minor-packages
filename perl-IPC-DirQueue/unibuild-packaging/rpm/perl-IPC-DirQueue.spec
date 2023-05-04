Name:           perl-IPC-DirQueue
Version:        1.0
Release:        2%{?dist}
Summary:        Disk-based many-to-many task queue
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IPC-DirQueue/
Source0:        IPC-DirQueue-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
Provides:       perl(IPC::DirQueue)

%if %{?rhel}%{!?rhel:0} == 4
BuildRequires:  perl(Time::HiRes) 
%endif

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module implements a FIFO queueing infrastructure, using a directory as
the communications and storage media. No daemon process is required to
manage the queue; all communication takes place via the filesystem.

%prep
%setup -q -n IPC-DirQueue-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc BUGS CHANGES README.dist TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/*

%changelog
* Wed Sep 23 2009 Steve Traylen <steve.traylen@cern.ch> 1.0-2
- Build requires perl(Time::HiRes) explicitly on RHEL4.

* Wed Sep 23 2009 Steve Traylen <steve.traylen@cern.ch> 1.0-1
- Specfile autogenerated by cpanspec 1.78.
