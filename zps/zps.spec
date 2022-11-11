Name:           zps
Version:        1.2.8
Release:        1%{?dist}
Summary:        A small utility for listing and cleaning up zombie processes

License:        GPL-3.0
URL:            https://github.com/orhun/zps
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils

%description
zps lists the running processes with theirs stats and indicates/reaps the 
zombie processes.

%prep
%autosetup

%build
%make_build CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"

%install
%make_install TARGET="%{buildroot}"
install -Dpm 0644 man/%{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Nov 11 2022 Gustavo Costa <xfgusta@gmail.com> 1.2.8-1
- Update to 1.2.8
- Change License to SPDX

* Tue Jun 29 2021 Gustavo Costa <xfgusta@fedoraproject.org> 1.2.7-1
- Initial package
