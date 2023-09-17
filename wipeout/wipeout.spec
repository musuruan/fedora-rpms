# DO NOT DISTRIBUTE PACKAGED RPMS FROM THIS SPEC FILE!

%global forgeurl https://github.com/phoboslab/wipeout-rewrite
%global commit f9f7b152639aaa3402a7b7d3fed8979d5dcdda93
%global date 20230917
%forgemeta

Name:           wipeout
Version:        0
Release:        0.1%{?dist}
Summary:        Futuristic racing video game

License:        Commercial
URL:            https://phoboslab.org/log/2023/08/rewriting-wipeout
Source0:        %{forgesource}
Source1:        %{name}.desktop

BuildRequires:  gcc-c++
BuildRequires:  cmake 
BuildRequires:  glew-devel
BuildRequires:  SDL2-devel
BuildRequires:  unzip
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils 
Requires:       hicolor-icon-theme
Requires:       %{name}-data


%description
Wipeout is a racing game that is set in 2052, where players compete in the
F3600 anti-gravity racing league.


%prep
%forgesetup

# Fix spurious executable permissions
find -type f \( -name '*.h' -o -name '*.c' \) -exec chmod -x '{}' \;


%build
%cmake -DPATH_ASSETS=%{_datadir}/
%cmake_build


%install
%cmake_install

# Install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
convert packaging/windows/%{name}.ico \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}


%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%doc README.md


%changelog
* Sun Sep 17 2023 Andrea Musuruane <musuruan@gmail.com> - 0-0.1.20230917gitf9f7b15
- First release
