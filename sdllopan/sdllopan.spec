%define pkgversion %(echo %version|sed s/\\\\\.//) 

Name:           sdllopan
Version:        1.0
Release:        3%{?dist}
Summary:        Mahjong solitaire

License:        GPL+
URL:            http://linuxmotors.com/linux/sdllopan/
Source0:        http://www.linuxmotors.com/linux/sdllopan/downloads/%{name}-%{pkgversion}.tgz
Source1:        %{name}.desktop
# Icon taken from
# https://github.com/pcbsd/appcafe/blob/master/icons/games_sdl_lopan.png
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
# Upstream clarification about the license
Source4:        %{name}-license.txt
# Fix Makefile
Patch0:         %{name}-1.0-Makefile.patch
# Add Window title
# https://github.com/haikuports/haikuports/tree/master/games-puzzle/sdllopan/patches
Patch1:         %{name}-1.0-Window_title.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  SDL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme

%description
Classical Chinese solitaire game.

The goal is to click on pairs of matching tiles to make them go away to
eventually clear the board. 

Tiles can only be clicked on if they're not blocked sideways or above by
another tile. Most tiles only match identical ones, but:
* any two flowers match
* any two seasons match


%prep
%autosetup -n %{name}-%{pkgversion}

# Use datadir
sed -i 's|data/bg%d.pcx|%{_datadir}/%{name}/data/bg%d.pcx|' lopan.c
sed -i 's|data/tiles%d.pcx|%{_datadir}/%{name}/data/tiles%d.pcx|' lopan.c
sed -i 's|char temp\[64\];|char temp\[256\];|' lopan.c

# Copy license
cp -a %{SOURCE4} license.txt


%build
%set_build_flags
%make_build


%install
# Install binary
install -d %{buildroot}%{_bindir}
install -p -m 0755 lopan %{buildroot}%{_bindir}

# Install data
install -d %{buildroot}%{_datadir}/%{name}
cp -aR data %{buildroot}/%{_datadir}/%{name}

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# Install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE2} \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# Install AppData file
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%{_bindir}/lopan
%{_datadir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%doc Changelog README
%license license.txt


%changelog
* Tue Dec 26 2023 Andrea Musuruane <musuruan@gmail.com> - 1.0-3
- Updated URL and Source0

* Sat Sep 11 2021 Andrea Musuruane <musuruan@gmail.com> - 1.0-2
- Fix FTBFS

* Fri Jul 13 2018 Andrea Musuruane <musuruan@gmail.com> - 1.0-1
-  First version
