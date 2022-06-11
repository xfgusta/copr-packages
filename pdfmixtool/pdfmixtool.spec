%global appid eu.scarpetta.PDFMixTool

Name:           pdfmixtool
Version:        1.1
Release:        1%{?dist}
Summary:        An application to split, merge, rotate and mix PDF files

License:        GPLv3+
URL:            https://scarpetta.eu/pdfmixtool
Source0:        https://gitlab.com/scarpetta/pdfmixtool/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  cmake(qt5)
BuildRequires:  cmake(qt5svg)
BuildRequires:  qt5-qttools-devel
BuildRequires:  pkgconfig(ImageMagick++)
BuildRequires:  qpdf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

%description
PDF Mix Tool is a simple and lightweight application that allows you to
perform common editing operations on PDF files.

%prep
%autosetup -n %{name}-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop

%files
%license LICENSE
%doc README.md CHANGELOG.md AUTHORS.md TRANSLATORS.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appid}.*
%{_metainfodir}/%{appid}.appdata.xml

%changelog
* Sat Jun 11 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 1.1-1
- Update to 1.1

* Fri Dec 10 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 1.0.2-1
- Initial package
