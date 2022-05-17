Name:           bfs
Version:        2.5
Release:        1%{?dist}
Summary:        A breadth-first version of the UNIX find command

License:        0BSD
URL:            https://github.com/tavianator/bfs
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(oniguruma)
# needed to run %check
BuildRequires:  /usr/bin/setfacl

%description
bfs is a breadth-first version of the UNIX find(1) command.

bfs supports almost every feature from every major find(1)
implementation, so your existing command lines should work as-is.
It also adds some features of its own, such as a more forgiving
command line parser and some additional options.

%prep
%autosetup

%build
%make_build

%install
%make_install

%check
%make_build check

%files
%license LICENSE
%doc README.md RELEASES.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%changelog
* Mon May 16 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 2.5-1
- Initial package
