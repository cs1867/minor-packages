%{!?perl_prefix: %define perl_prefix %(eval "`%{__perl} -V:installprefix`"; echo $installprefix)}
%{!?perl_style: %define perl_style %(eval "`%{__perl} -V:installstyle`"; echo $installstyle)}

%define disttag pSPS

Name:           perl-Sys-Syslog
Version:        0.27
Release:        1.%{disttag}
Summary:        Perl interface to the UNIX syslog(3) calls
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Sys-Syslog/
Source0:        http://www.cpan.org/modules/by-module/Sys/Sys-Syslog-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(Carp)
Requires:       perl(Fcntl)
Requires:       perl(File::Basename)
Requires:       perl(File::Spec)
Requires:       perl(POSIX)
Requires:       perl(Socket)
Requires:       perl(Test::More)
Requires:       perl(XSLoader)

%description
Sys::Syslog is an interface to the UNIX syslog(3) program. Call syslog()
with a string priority and a list of printf() args just like syslog(3).

%prep
%setup -q -n Sys-Syslog-%{version}

%build
%{__perl} Makefile.PL INSTALL_BASE=%{perl_prefix} OPTIMIZE="$RPM_OPT_FLAGS"
%{__perl} -pi -e 's/^\tLD_RUN_PATH=[^\s]+\s*/\t/' Makefile
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{__mv} scripts $RPM_BUILD_ROOT/tmp

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README README.win32
/usr/*
/tmp/*

%post
/tmp/./perl-Sys-Syslog_post.sh
%{__rm} /tmp/perl-Sys-Syslog_post.sh

%changelog
* Tue Sep 29 2009 Jason Zurawski 0.27-1
- Specfile autogenerated by cpanspec 1.78.
