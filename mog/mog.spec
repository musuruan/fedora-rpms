%global rev 1548

Name:           mog
Version:        0.63
Release:        1%{?dist}
Summary:        A side-view, flick-screen platform game

License:        GPLv2
URL:            https://mog.jorito.net/
Source0:        http://braingames.jorito.net/mog/downloads/%{name}.src_%{version}-%{rev}.tgz
Source1:        %{name}.sh
Source2:        %{name}.appdata.xml
# Patch Makefile
Patch0:        %{name}-0.63-Makefile.patch
# Disable fullscreen on startup
# Patch from haikuports
# https://github.com/haikuports/haikuports/tree/master/games-arcade/mog/patches
Patch1:         %{name}-0.63-fullscreen.patch
# Fix NAME_MAX redefinition
# Patch from Void Linux
# https://github.com/void-linux/void-packages/blob/master/srcpkgs/mog/patches/
Patch2:         %{name}-0.63-name_max.patch
# Fix format strings
# Patch from Rosa Linux
# https://abf.io/import/mazeofgalious
Patch3:         %{name}-0.63-sfmt.patch

BuildRequires:  gcc-c++
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_sound-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme


%description
The Maze of Galious (MoG in short) was originally a Konami game for the MSX
computer system. Its real name is Knightmare II: The Maze of Galious and is
the sequel of another Konami game called Knightmare.

MoG is a very addictive game where you have to kill thousands of enemies,
collect items in order to obtain new powers and defeat some really great demons
at the end of each level. The gameplay of MoG is not the boring linear one.

In MoG you are free to go everywhere you want from the beginning of the game.
You have to be very careful of the order in which you visit all the rooms in
the HUGE map if you want to keep your character alive. The map is structured
in a main map (called the castle) and 10 submaps (called the worlds).
Initially you are in the castle and you have to find the keys that open the
doors to go to each of the worlds. To complete the game you have to defeat
the boss at the end of each one of the 10 worlds. You are free to revisit
each world as often as you want in order to see if you have missed something.

To defeat all 10 demons you control two characters: Popolon and Aphrodite.
Each one has special abilities, i.e. Popolon has a greater ability to jump
and Aphrodite is able to dive.


%prep
%setup -q -n %{name}-%{version}.%{rev}
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1

# Fix end-of-line encoding
sed -i 's/\r//' *.txt

# Fix char encondigs
for i in *.txt; do
  iconv --from=ISO-8859-1 --to=UTF-8 $i > $i.utf8
  mv $i.utf8 $i
done


%build
%set_build_flags
%make_build


%install
# Install wrapper script
install -d %{buildroot}%{_bindir}
install -m 755 -p %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# Install game and data
install -d %{buildroot}%{_libexecdir}/%{name}
install -m 755 -p %{name} %{buildroot}%{_libexecdir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -pr graphics rooms sound %{buildroot}%{_datadir}/%{name}

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
convert -resize 48x48 \
  -extent 48x48 \
  -gravity center \
  -background none \
  build/linux/%{name}.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --set-icon=%{name} \
  --remove-category=Application \
  build/linux/%{name}.desktop

# Install AppData file
install -d %{buildroot}%{_metainfodir}
install -p -m 644 %{SOURCE2} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml
%license LICENSE
%doc readme.txt MoG-FAQ.txt


%changelog
* Sat Dec 14 2019 Andrea Musuruane <musuruan@gmail.com> - 0.63-1
- First release
