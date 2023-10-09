%global commit a4000681a20cd6639183cf72a722f4c2daf30cc7
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           hydracastlelabyrinth
Version:        0
Release:        0.2.20220624gita400068%{?dist}
Summary:        Regain the crown stolen by the snake god Hydra!

# Hydra Castle Labyrinth files are freeware
License:        GPLv2 and freeware
URL:            https://github.com/ptitSeb/hydracastlelabyrinth
Source0:        %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        %{name}.sh
Source2:        %{name}.desktop

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Hydra Castle consists of "fields" and "dungeon". You will need the key hidden
in the "field" to enter the "dungeon". There are 8 "dungeon" in total, and
the "boss" awaits you in the back.


%prep
%autosetup -n %{name}-%{commit}


%build
%cmake -DUSE_SDL2=ON
%cmake_build


%install
# Install wrapper script
install -d %{buildroot}%{_bindir}
install -m 755 -p %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# Install game binary
install -d %{buildroot}%{_libexecdir}/%{name}
install -p -m 0755 %{_vpath_builddir}/hcl %{buildroot}%{_libexecdir}

# Install data
install -d %{buildroot}%{_datadir}/%{name}
cp -aR data/ %{buildroot}%{_datadir}/%{name}

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -m 0644 icon.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE2}


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libexecdir}/hcl
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%license LICENSE
%doc README.md

%changelog
* Sun Jul 10 2022 Andrea Musuruane <musuruan@gmail.com> - 0-0.2.20220624gita400068
- Updated to latest git commit

* Sat Sep 04 2021 Andrea Musuruane <musuruan@gmail.com> - 0-0.1.20210416gitab43945
- First release
