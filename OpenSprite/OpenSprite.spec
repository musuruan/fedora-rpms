%global commit b0967158a99adb94e4a04299bf6853ae16ffe21e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           OpenSprite
Version:        1.42
Release:        1%{?dist}
Summary:        An open source sprite editor to generate sprites for the C64

License:        GPLv3
URL:            https://github.com/jowin202/OpenSprite
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop

BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
An open source sprite editor to generate sprites for the Commodore C64!


%prep
%autosetup -n %{name}-%{commit}

# Fix install path
sed -i 's!target.path = /opt/$${TARGET}/bin!target.path = /usr/bin!' \
   OpenSprite.pro


%build
%qmake_qt6 OpenSprite.pro
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# Install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/96x96/apps
install -p -m 0644 icons/opensprite96x96.png \
  %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/%{name}.png


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Thu Jun 13 2024 Andrea Musuruane <musuruan@gmail.com> - 1.42-1
- Updated to new upstream release

* Sun May 05 2024 Andrea Musuruane <musuruan@gmail.com> - 1.41-1
- Updated to new upstream release

* Sun Apr 07 2024 Andrea Musuruane <musuruan@gmail.com> - 1.4-1
- First release
