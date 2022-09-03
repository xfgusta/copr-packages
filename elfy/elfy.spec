Name:           elfy
Version:        0.2.0
Release:        2%{?dist}
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
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Sep 03 2022 Gustavo Costa <xfgusta@gmail.org> - 0.2.0-2
- Set build flags

* Fri Sep 02 2022 Gustavo Costa <xfgusta@gmail.org> - 0.2.0-1
- Update to 0.2.0

* Sat Jun 04 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 0.1.0-1
- Initial package
