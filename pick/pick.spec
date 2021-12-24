Name:           pick
Version:        4.0.0
Release:        1%{?dist}
Summary:        A fuzzy search tool for the command-line

# The entire source code is MIT except for
# compat-reallocarray.c and compat-strtonum.c files which are ISC
License:        MIT and ISC
URL:            https://github.com/mptre/pick
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  ncurses-devel

Conflicts:      nmh

%description
The pick utility allows users to choose one option from a set of choices using
an interface with fuzzy search functionality. pick reads a list of choices on
stdin and outputs the selected choice on stdout. Therefore it is easily used
both in pipelines and subshells.

%prep
%autosetup

%build
export PREFIX=%{_prefix}
export MANDIR=%{_mandir}
export INSTALL_MAN="%{__install} -p -m 0644"
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Nov 28 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 4.0.0-1
- Initial package
