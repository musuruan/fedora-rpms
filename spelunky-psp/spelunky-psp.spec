Name:           spelunky-psp
Version:        0.5
Release:        1%{?dist}
Summary:        A platform game with randomized levels

# Code under GPLv3 and custom license for assets
License:        GPL-3.0-only and Spelunky-User-License-1.1b
URL:            https://github.com/dbeef/spelunky-psp
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Spelunky is a unique platformer with randomized levels that offer a challenging
new experience each time you play. Journey deep underground and explore
fantastic places filled with all manner of monsters, traps, and treasure.
You'll have complete freedom while you navigate the fully-destructible
environments and master their many secrets. To stay or flee, to kill or
rescue, to shop or steal... in Spelunky, the choice is yours and so are the
consequences!


%prep
%autosetup


%build
%cmake
%cmake_build


%install
# Install binary
install -d %{buildroot}%{_bindir}
install -p -m 755 %{__cmake_builddir}/Spelunky_PSP %{buildroot}%{_bindir}

# Install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 \
  platforms/android/android-app/src/main/res/mipmap-mdpi/ic_launcher.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}


%files
%license LICENSE
%doc README.md
%{_bindir}/Spelunky_PSP
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Mon Sep 09 2024 Andrea Musuruane <musuruan@gmail.com> - 0.5-1
- First release
