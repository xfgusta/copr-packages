Name:           nq
Version:        0.5
Release:        1%{?dist}
Summary:        Unix command line queue utility

License:        CC0
URL:            https://github.com/leahneukirchen/nq
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl(Test::Harness)

Recommends:     (tmux or screen)

%description
The nq utility provides a very lightweight queuing system without requiring 
setup, maintenance, supervision or any long-running processes.

%prep
%autosetup

%build
%make_build CFLAGS='%{build_cflags}'

%check
%make_build check

%install
%make_install PREFIX=%{_prefix}

%files
%license COPYING
%doc README.md NEWS.md
%{_bindir}/%{name}
%{_bindir}/fq
%{_bindir}/tq
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/fq.1*
%{_mandir}/man1/tq.1*

%changelog
* Sat Mar 26 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 0.5-1
- Remove patch
- Update to 0.5

* Tue Oct 12 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 0.4-1
- Initial package
