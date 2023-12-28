Name:           pekka-kana-2
Version:        1.2.7
Release:        1%{?dist}
Summary:        2D Oldschool platform game where you control a rooster

License:        BSD
URL:            https://pistegamez.net/game_pk2.html
Source0:        https://gitlab.com/coringao/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Your mission in Pekka Kana 2 is to save Pekka's chicken friends from an evil
crow.

The simple goal in each level is to find the exit sign, which is usually not
that simple as it sounds because of enemies, traps, and quirky puzzles.


%prep
%autosetup

# Fix datadir
sed -i 's!/usr/share/games/pekka-kana-2/data!/usr/share/pekka-kana-2/data!' \
  src/pk2.cpp 


%build
%set_build_flags
%make_build


%install
# Install binary
install -d %{buildroot}%{_bindir}
install -p -m 0755 bin/%{name} %{buildroot}%{_bindir}

# Install data
install -d %{buildroot}%{_datadir}/%{name}
cp -aR data %{buildroot}%{_datadir}/%{name}

# Install man page
install -d %{buildroot}%{_mandir}/man6
install -p -m 644 data/%{name}.6 %{buildroot}%{_mandir}/man6/

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  data/%{name}.desktop

# Resize and install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
convert -resize 256x256 \
  -extent 256x256 \
  -gravity center \
  -background none \
  data/%{name}.png \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*
%license LICENSE 
%doc Readme.md


%changelog
* Wed May 26 2021 Andrea Musuruane <musuruan@gmail.com> - 1.2.7-1
- First import
