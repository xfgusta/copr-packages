%global debug_package %{nil}

Name:           zps
Version:        1.2.7
Release:        1%{?dist}
Summary:        A small utility for listing and cleaning up zombie processes

License:        GPLv3
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
%set_build_flags
%make_build

%install
%make_install TARGET="%{buildroot}"
%{__install} -Dpm 0644 man/%{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Jun 29 2021 Gustavo Costa <xfgusta@fedoraproject.org> 1.2.7-1
- Initial package
