%undefine _hardened_build

Name:           xdump
Version:        0.1.1
Release:        1%{?dist}
Summary:        Display file contents in hexadecimal and ASCII

License:        MIT
URL:            https://github.com/xfgusta/xdump
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc

%description
The xdump utility is a filter which displays the specified file, or standard
input if no file is specified, in hexadecimal and ASCII format.

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
* Sat Oct 09 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 0.1.1-1
- Initial package
