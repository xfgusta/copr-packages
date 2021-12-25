Name:           fzy
Version:        1.0
Release:        1%{?dist}
Summary:        A simple, fast fuzzy finder for the terminal 

License:        MIT
URL:            https://github.com/jhawthorn/fzy
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc

%description
fzy is a fuzzy text selector/file finder for the terminal using a search
similar to that of TextMate or CmdT.

fzy reads a list of newline-separated items from stdin to be displayed as a
menu in the terminal. Upon pressing ENTER, the currently selected item is
printed to stdout.

Entering text narrows the items using fuzzy matching. Results are sorted using
heuristics for the best match.

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
* Sun Jun 27 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 1.0-1
- Initial package
