%global appid com.github.hugolabe.Wike

Name:           wike
Version:        1.6.3
Release:        1%{?dist}
Summary:        Wikipedia Reader for the GNOME Desktop

License:        GPLv3
URL:            https://github.com/hugolabe/wike
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
Requires:       python3-gobject
Requires:       gtk3
Requires:       libhandy1
Requires:       webkit2gtk3
Requires:       python3dist(dbus-python)
Requires:       python3dist(requests)

%description
Wike is a Wikipedia reader for the GNOME Desktop. Provides access to all the 
content of this online encyclopedia in a native application, with a simpler and 
distraction-free view of articles.

%prep
%autosetup -n Wike-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{appid}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/actions/*
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_metainfodir}/%{appid}.metainfo.xml
%{_datadir}/dbus-1/services/%{appid}.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/%{appid}.SearchProvider.ini

%changelog
* Fri Dec 17 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 1.6.3-1
- Initial package