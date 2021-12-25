Name:           extrace
Version:        0.8
Release:        1%{?dist}
Summary:        Trace exec() calls system-wide

License:        GPLv2+ and BSD
URL:            https://github.com/leahneukirchen/extrace
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc

%description
extrace traces all program executions occurring on a system.

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README NEWS.md
%caps(cap_net_admin=ep) %{_bindir}/%{name}
%caps(cap_net_admin=ep) %{_bindir}/pwait
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/pwait.1*

%changelog
* Thu Aug 26 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 0.8-1
- Initial package
