Name:           execdir
Version:        0.1.0
Release:        1%{?dist}
Summary:        Execute a command in a specific directory

License:        MIT
URL:            https://github.com/xfgusta/execdir
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
execdir is a tool that lets you run a command in a specific directory.

%prep
%autosetup

%build
%make_build CFLAGS='%{build_cflags}' LDFLAGS='%{build_ldflags}'

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/xdir
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/xdir.1*

%changelog
* Thu Jun 23 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 0.1.0-1
- Initial package
