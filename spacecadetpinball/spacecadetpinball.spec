# DO NOT DISTRIBUTE PACKAGED RPMS FROM THIS SPEC FILE!

Name:           spacecadetpinball
Version:        2.1.0
Release:        2%{?dist}
Summary:        3D Pinball

License:        MIT
URL:            https://github.com/k4zmu2a/SpaceCadetPinball
Source0:        %url/archive/Release_%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-g++
BuildRequires:  cmake
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Reverse engineering of '3D Pinball for Windows - Space Cadet', a game bundled
with Windows.

The Space Cadet table features the player as a member of a space fleet where
they complete missions to increase their rank. Players accept a mission by
hitting "mission targets" which select which mission they will take, and by
going up the "launch ramp". Players must complete a certain number of tasks
in each mission, such as hitting the "attack bumpers" (a set of four bumpers
at the top of the table) eight times. Missions will finish when the goal is
achieved or when all of the lights beneath the launch ramp are turned off.


%prep
%autosetup -n SpaceCadetPinball-Release_%{version}


%build
%cmake
%cmake_build


%install
%cmake_install

# Install README.Fedora
cat > README.Fedora << EOF
This game is distributed without the data files. To play, copy the original
DAT and SOUND files from a Windows or 'Full Tilt!' installation and place them
in $XDG_DATA_HOME/SpaceCadetPinball (usually:
~/.local/share/SpaceCadetPinball/)
EOF

# Validate desktop file
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/SpaceCadetPinball.desktop

# Validate AppData file
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/SpaceCadetPinball.metainfo.xml


%files
%license LICENSE
%doc README.md README.Fedora
%{_bindir}/SpaceCadetPinball
%{_datadir}/applications/SpaceCadetPinball.desktop
%{_datadir}/icons/hicolor/*/apps/SpaceCadetPinball.png
%{_metainfodir}/SpaceCadetPinball.metainfo.xml


%changelog
* Tue Jun 18 2024 Andrea Musuruane <musuruan@gmail.com> - 2.1.0-2
- Added desktop file and AppData file validation

* Mon Jun 17 2024 Andrea Musuruane <musuruan@gmail.com> - 2.1.0-1
- Updated to new upstream release

* Tue Jun 07 2022 Andrea Musuruane <musuruan@gmail.com> - 2.0.1-1
- First release
