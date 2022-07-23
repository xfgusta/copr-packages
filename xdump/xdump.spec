Name:           xdump
Version:        1.0.0
Release:        1%{?dist}
Summary:        Display file contents in hexadecimal and ASCII

License:        MIT
URL:            https://github.com/xfgusta/xdump
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc

%description
The xdump utility is a filter which displays the specified file, or standard
input if no file is specified, in hexadecimal and ASCII format. It uses a
colored output to distinguish different categories of bytes.

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
* Sat Jul 23 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- Change description
- Set CFLAGS and LDFLAGS

* Sat Oct 09 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 0.1.1-1
- Initial package
