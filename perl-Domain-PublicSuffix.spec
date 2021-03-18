#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Domain-PublicSuffix
Version  : 0.19
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/N/NM/NMELNICK/Domain-PublicSuffix-0.19.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NM/NMELNICK/Domain-PublicSuffix-0.19.tar.gz
Summary  : 'Parse a domain down to root'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Domain-PublicSuffix-bin = %{version}-%{release}
Requires: perl-Domain-PublicSuffix-license = %{version}-%{release}
Requires: perl-Domain-PublicSuffix-man = %{version}-%{release}
Requires: perl-Domain-PublicSuffix-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Accessor::Fast)
BuildRequires : perl(Net::IDN::Encode)

%description
This archive contains the distribution Domain-PublicSuffix,
version 0.19:
Parse a domain down to root

%package bin
Summary: bin components for the perl-Domain-PublicSuffix package.
Group: Binaries
Requires: perl-Domain-PublicSuffix-license = %{version}-%{release}

%description bin
bin components for the perl-Domain-PublicSuffix package.


%package dev
Summary: dev components for the perl-Domain-PublicSuffix package.
Group: Development
Requires: perl-Domain-PublicSuffix-bin = %{version}-%{release}
Provides: perl-Domain-PublicSuffix-devel = %{version}-%{release}
Requires: perl-Domain-PublicSuffix = %{version}-%{release}

%description dev
dev components for the perl-Domain-PublicSuffix package.


%package license
Summary: license components for the perl-Domain-PublicSuffix package.
Group: Default

%description license
license components for the perl-Domain-PublicSuffix package.


%package man
Summary: man components for the perl-Domain-PublicSuffix package.
Group: Default

%description man
man components for the perl-Domain-PublicSuffix package.


%package perl
Summary: perl components for the perl-Domain-PublicSuffix package.
Group: Default
Requires: perl-Domain-PublicSuffix = %{version}-%{release}

%description perl
perl components for the perl-Domain-PublicSuffix package.


%prep
%setup -q -n Domain-PublicSuffix-0.19
cd %{_builddir}/Domain-PublicSuffix-0.19

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Domain-PublicSuffix
cp %{_builddir}/Domain-PublicSuffix-0.19/LICENSE %{buildroot}/usr/share/package-licenses/perl-Domain-PublicSuffix/49247d81119a808f6cebaea16d362cd8aa7ede31
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/get_root_domain

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Domain::PublicSuffix.3
/usr/share/man/man3/Domain::PublicSuffix::Default.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Domain-PublicSuffix/49247d81119a808f6cebaea16d362cd8aa7ede31

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/get_root_domain.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Domain/PublicSuffix.pm
/usr/lib/perl5/vendor_perl/5.32.1/Domain/PublicSuffix/Default.pm
