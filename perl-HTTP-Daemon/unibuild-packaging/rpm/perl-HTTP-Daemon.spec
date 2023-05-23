Name:           perl-HTTP-Daemon
Version:        6.16
Release:        1%{?dist}
Summary:        Simple http server class
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTTP-Daemon/
Source0:        HTTP-Daemon-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Date) >= 6
BuildRequires:  perl(HTTP::Request) >= 6
BuildRequires:  perl(HTTP::Response) >= 6
BuildRequires:  perl(HTTP::Status) >= 6
BuildRequires:  perl(IO::Socket::IP) >= 0.32
BuildRequires:  perl(LWP::MediaTypes) >= 6
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Needs)
Requires:       perl(Carp)
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(HTTP::Request) >= 6
Requires:       perl(HTTP::Response) >= 6
Requires:       perl(HTTP::Status) >= 6
Requires:       perl(IO::Socket::IP) >= 0.32
Requires:       perl(LWP::MediaTypes) >= 6
Requires:       perl(Socket)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Instances of the HTTP::Daemon class are HTTP/1.1 servers that listen on a
socket for incoming requests. The HTTP::Daemon is a subclass of
IO::Socket::IP, so you can perform socket operations directly on it too.

%prep
%setup -q -n HTTP-Daemon-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes CONTRIBUTING cpanfile dist.ini LICENCE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue May 23 2023 Andy Lake 6.16-1
- Specfile autogenerated by cpanspec 1.78.
