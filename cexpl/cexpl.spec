Name:           cexpl
Version:        0.1.0
Release:        1%{?dist}
Summary:        Command-line tool to interact with Compiler Explorer

License:        MIT
URL:            https://github.com/xfgusta/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

Requires:       python3dist(colorama)
Requires:       python3dist(requests)
Requires:       python3dist(setuptools)

%description
Command-line tool to interact with Compiler Explorer. cexpl is able to query
all available languages, compilers, build and execute your source code. You
can also give some extra arguments, like compiler flags, command-line
arguments and STDIN.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Oct 04 2022 Gustavo Costa <xfgusta@gmail.com> - 0.1.0-1
- Initial package
