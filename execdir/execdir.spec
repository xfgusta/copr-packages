Name:           execdir
Version:        0.3.0
Release:        1%{?dist}
Summary:        Execute a command in a specific directory

License:        MIT
URL:            https://github.com/xfgusta/execdir
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
A tool that lets you run a command in a specific directory. It supports shell
commands and path aliases. execdir will try to get an alias if the path doesn't
exist.

There is also a symlink called x, so you can type less using it.

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
%{_bindir}/x
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/x.1*

%changelog
* Wed Jul 13 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0
- Change description

* Thu Jun 30 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Thu Jun 23 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 0.1.0-1
- Initial package
