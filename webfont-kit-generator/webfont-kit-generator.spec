%global appname webfontkitgenerator
%global appid com.rafaelmardojai.WebfontKitGenerator

Name:           webfont-kit-generator
Version:        0.5.0
Release:        1%{?dist}
Summary:        Create @font-face kits easily

License:        GPLv3
URL:            https://github.com/rafaelmardojai/webfont-kit-generator
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  glib2-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
Requires:       python3-gobject
Requires:       libhandy1
Requires:       gtk3
Requires:       gtksourceview4
Requires:       python3dist(fonttools)

%description
Webfont Kit Generator is a simple utility that allows you to generate woff, 
woff2 and the necessary CSS boilerplate from non-web font formats (otf & ttf).

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appname}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{appid}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop

%files -f %{appname}.lang
%license COPYING
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/%{appname}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Wed Jun 30 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 0.5.0-1
- Initial package
