Name:           trurl
Version:        0.8
Release:        1%{?dist}
Summary:        Command line tool for URL parsing and manipulation

License:        curl
URL:            https://curl.se/trurl
Source0:        https://github.com/curl/trurl/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  python3-devel

%description
A small command line tool that parses and manipulates URLs, designed to help
shell script authors everywhere.

%prep
%autosetup -n %{name}-%{name}-%{version}

%build
%make_build

%check
make test

%install
%make_install PREFIX=%{_prefix}

%files
%license COPYING
%doc README.md RELEASE-NOTES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jun 18 2023 Gustavo Costa <xfgusta@gmail.com> - 0.8-1
- Update to 0.8

* Wed May 31 2023 Gustavo Costa <xfgusta@gmail.com> - 0.7-1
- Update to 0.7

* Wed Apr 26 2023 Gustavo Costa <xfgusta@gmail.com> - 0.6-1
- Update to 0.6
- Drop patch

* Tue Apr 18 2023 Gustavo Costa <xfgusta@gmail.com> - 0.5-1
- Update to 0.5
- Use python to run tests
- Set CFLAGS
- Add patch to update the version

* Tue Apr 11 2023 Gustavo Costa <xfgusta@gmail.com> - 0.4-1
- Update to 0.4

* Sat Apr 08 2023 Gustavo Costa <xfgusta@gmail.com> - 0.3-1
- Update to 0.3
- Add BR perl(Test::More)
- Drop patch
- Change URL
- Add RELEASE-NOTES to doc

* Tue Apr 04 2023 Gustavo Costa <xfgusta@gmail.com> - 0.2-1
- Initial package
