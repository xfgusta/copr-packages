Name:           strace-with-colors
Version:        5.18
Release:        2%{?dist}
Summary:        A diagnostic, debugging and instructional userspace tracer (with colors!)

License:        LGPLv2+ and GPLv2+
URL:            https://strace.io
Source0:        %{url}/files/%{version}/strace-%{version}.tar.xz
Patch0:         %{name}.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  xz
BuildRequires:  pkgconfig(bluez)
BuildRequires:  elfutils-devel
BuildRequires:  binutils-devel
BuildRequires:  libselinux-devel

Conflicts:      strace

%description
The strace program intercepts and records the system calls called and
received by a running process.  Strace can print a record of each
system call, its arguments and its return value.  Strace is useful for
diagnosing problems and debugging, as well as for instructional
purposes.

%prep
%autosetup -n strace-%{version} -p1

%build
%configure --enable-mpers=no
%make_build

%install
%make_install

%files
%license COPYING
%doc CREDITS ChangeLog-CVS NEWS README
%{_bindir}/strace
%{_bindir}/strace-log-merge
%{_mandir}/man1/strace.1*
%{_mandir}/man1/strace-log-merge.1*

%changelog
* Fri Jul 15 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 5.18-2
- Update to 5.18-1: Add --color option

* Sun Jun 19 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 5.18-1
- Update to 5.18

* Tue Apr 19 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 5.17-3
- Update to 5.17-3: Disable colored output when using -o option

* Thu Apr 07 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 5.17-2
- Update to 5.17-2: Add --no-color option

* Sun Mar 27 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 5.17-1
- Update to 5.17

* Fri Dec 17 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 5.15-1
- Initial package
