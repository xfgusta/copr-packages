Name:           elfy
Version:        0.1.0
Release:        1%{?dist}
Summary:        Display information about ELF files

License:        MIT
URL:            https://github.com/xfgusta/elfy
Source0:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libelf)

%description
A tool for displaying information about ELF files.

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
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Jun 04 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 0.1.0-1
- Initial package
