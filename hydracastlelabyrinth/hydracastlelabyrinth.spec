%global commit 229369c222f8604530f5e06f795b4505ef21d439
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           hydracastlelabyrinth
Version:        0
Release:        0.3.20240228git229369c%{?dist}
Summary:        Regain the crown stolen by the snake god Hydra!

# Hydra Castle Labyrinth files are freeware
License:        GPL-2.0-only and freeware
URL:            https://github.com/ptitSeb/hydracastlelabyrinth
Source0:        %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        %{name}.sh

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Hydra Castle consists of "fields" and "dungeon". You will need the key hidden
in the "field" to enter the "dungeon". There are 8 "dungeon" in total, and
the "boss" awaits you in the back.


%prep
%autosetup -n %{name}-%{commit}

# Fix destkop file
sed -i '1d' io.github.ptitSeb.%{name}.desktop

# Fix CMakeFile
sed -i 's!set(CMAKE_INSTALL_BINDIR ".")!set(CMAKE_INSTALL_BINDIR "libexec")!' CMakeLists.txt
sed -i 's!set(CMAKE_INSTALL_DATADIR ".")!set(CMAKE_INSTALL_DATADIR "share/%{name}")!' CMakeLists.txt


%build
%cmake -DUSE_SDL2=ON
%cmake_build


%install
%cmake_install

# Fix directory permissions
find %{buildroot}%{_datadir}/%{name} -type d -exec chmod 755 {} \;

# Install wrapper script
install -d %{buildroot}%{_bindir}
install -m 755 -p %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# Call wrapper script in desktop file
desktop-file-install \
  --delete-original \
  --set-key=Exec \
  --set-value=%{name} \
  --set-comment="Regain the crown stolen by the snake god Hydra!" \
  --add-category=ActionGame \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/io.github.ptitSeb.%{name}.desktop

# Validate AppData file
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/appdata/*.metainfo.xml


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libexecdir}/hcl
%{_datadir}/appdata/io.github.ptitSeb.%{name}.metainfo.xml
%{_datadir}/applications/io.github.ptitSeb.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/io.github.ptitSeb.%{name}.png
%license LICENSE
%doc README.md

%changelog
* Tue Jun 18 2024 Andrea Musuruane <musuruan@gmail.com> - 0-0.3.20240228git229369c
- Updated to latest git commit

* Sun Jul 10 2022 Andrea Musuruane <musuruan@gmail.com> - 0-0.2.20220624gita400068
- Updated to latest git commit

* Sat Sep 04 2021 Andrea Musuruane <musuruan@gmail.com> - 0-0.1.20210416gitab43945
- First release
