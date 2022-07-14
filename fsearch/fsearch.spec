%global appid io.github.cboxdoerfer.FSearch

Name:           fsearch
Version:        0.1.4
Release:        1%{?dist}
Summary:        A fast file search utility for Unix-like systems based on GTK+3

License:        GPLv2+
URL:            https://github.com/cboxdoerfer/fsearch
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme

%description
FSearch is a fast file search utility, inspired by Everything Search Engine.
It's written in C and based on GTK 3.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{appid}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop

%files -f %{name}.lang
%license License
%doc README.md NEWS
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{appid}.appdata.xml

%changelog
* Thu Jul 14 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Sun Mar 27 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 0.1.2-1
- Initial package
