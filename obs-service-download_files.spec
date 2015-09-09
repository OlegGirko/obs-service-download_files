Name: obs-service-download_files
Summary: An OBS source service: download files
Version: 0.5.1
Release: 1
Group: Development/Tools
License: GPLv2+
BuildArch: noarch
Source: https://github.com/openSUSE/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1: 0001-Fix-grammar.patch
Patch2: 0002-Add-GPL2-license.patch
Patch3: 0003-Add-Makefile-with-install-target.patch
Patch4: 0004-Debianization.patch
Patch5: 0005-Stricter-change-filename-check.patch
Requires: wget
Requires: perl
Requires: perl(Build)
Requires: gzip
Requires: bzip2
Requires: xz
Requires: tar

%description
This is a source service for openSUSE Build Service.

This service is parsing all spec files and downloads all Source files which
are specified via a http, https or ftp url.

%prep
%setup -q -n src
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%make_build \
  prefix=%{_prefix} \
  localstatedir=%{_localstatedir} \
  sysconfdir=%{_sysconfdir}

%install
%make_install \
  prefix=%{_prefix} \
  localstatedir=%{_localstatedir} \
  sysconfdir=%{_sysconfdir}

%files
%defattr(-,root,root,-)
%{_prefix}/lib/obs/service
%{_sysconfdir}/obs/services
%{_localstatedir}/cache/obs
