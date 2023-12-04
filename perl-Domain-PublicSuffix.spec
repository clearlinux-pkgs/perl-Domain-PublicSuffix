#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Domain-PublicSuffix
Version  : 0.20
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/N/NM/NMELNICK/Domain-PublicSuffix-0.20.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NM/NMELNICK/Domain-PublicSuffix-0.20.tar.gz
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Domain-PublicSuffix,
version 0.20:
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
%setup -q -n Domain-PublicSuffix-0.20
cd %{_builddir}/Domain-PublicSuffix-0.20
pushd ..
cp -a Domain-PublicSuffix-0.20 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
cp %{_builddir}/Domain-PublicSuffix-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Domain-PublicSuffix/fc82b37af3a4f3536401e0dec56c34519025d893 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/share/package-licenses/perl-Domain-PublicSuffix/fc82b37af3a4f3536401e0dec56c34519025d893

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/get_root_domain.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
