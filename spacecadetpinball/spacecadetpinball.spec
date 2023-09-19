# DO NOT DISTRIBUTE PACKAGED RPMS FROM THIS SPEC FILE!

Name:           spacecadetpinball
Version:        2.0.1
Release:        1%{?dist}
Summary:        3D Pinball

License:        MIT
URL:            https://github.com/k4zmu2a/SpaceCadetPinball
Source0:        %url/archive/Release_%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-g++
BuildRequires:  cmake
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel

%description
Reverse engineering of '3D Pinball for Windows - Space Cadet', a game bundled
with Windows.

This game is distributed without the data files. To play, copy the original
DAT and SOUND files from a Windows or 'Full Tilt! installation and place them
in $XDG_DATA_HOME/SpaceCadetPinball (usually:
~/.local/share/SpaceCadetPinball/)


%prep
%autosetup -n SpaceCadetPinball-Release_%{version}

# Fix directories
sed -i 's!/Platform/Linux/!Platform/Linux/!' CMakeLists.txt


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_bindir}/SpaceCadetPinball
%{_datadir}/applications/SpaceCadetPinball.desktop
%{_datadir}/icons/hicolor/*/apps/SpaceCadetPinball.png
%{_datadir}/metainfo/SpaceCadetPinball.metainfo.xml


%changelog
* Tue Jun 07 2022 Andrea Musuruane <musuruan@gmail.com> - 2.0.1-1
- First release
