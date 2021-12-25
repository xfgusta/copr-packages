%undefine _hardened_build

Name:           lr
Version:        1.5.1
Release:        1%{?dist}
Summary:        List files, recursively

License:        MIT
URL:            https://github.com/leahneukirchen/lr
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc

%description
lr is a versatile tool to generate file listings with configurable formatting,
ordering and filtering.

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md NEWS.md
%{_bindir}/%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Sep 13 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 1.5.1-1
- Initial package
