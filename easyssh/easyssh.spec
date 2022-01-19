%global appid com.github.muriloventuroso.easyssh

Name:           easyssh
Version:        1.7.9
Release:        1%{?dist}
Summary:        SSH Connection Manager

License:        GPLv3+
URL:            https://github.com/muriloventuroso/easyssh
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

%description
A complete, efficient and easy-to-use manager. Create and edit connections,
groups, customize the terminal, with multiple instances of the same connection.

%prep
%autosetup

%build
%meson -Dubuntu-bionic-patched-vte=false -Dpatched-vte=true
%meson_build

%install
%meson_install
%find_lang %{appid}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{appid}.appdata.xml

%files -f %{appid}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/%{appid}.appdata.xml

%changelog
* Wed Jan 19 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 1.7.9-1
- Initial package
