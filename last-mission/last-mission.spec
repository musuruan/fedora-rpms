Name:           last-mission
Version:        0.8
Release:        1%{?dist}
Summary:        A side-view arcade game

License:        GPLv2
URL:            https://github.com/dmitrysmagin/last-mission
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
The Last Mission is a side-view arcade game without scrolling (viewpoint moves
from screen to screen) with map of big dimensions. The game takes its
inspiration from games such as Underwurlde and Starquake.

You control a tank-like robot which can be divided in two: you rotate
caterpillar and head-cannon, and the head part can fly off on its own. However,
the head can only survive separately for a short amount of time, and your
restart position is dictated by the location of the body, even if the head has
moved forward through further screens.
Therefore, the difficulty of the game was in making it possible to advance with
the assembled robot's two parts.


%prep
%autosetup

# Fix end-of-line encoding
sed "s|\r||" -i *.txt

# Fix datadir
sed "s|sound/|%{_datadir}/%{name}/&|g" -i sound.c

# Fix flags and add -lm to LDFLAGS
sed -e 's|CFLAGS = \(.*\)|CFLAGS +=  -std=c99 -D__UNIX__ -DDEBUG|' \
  -e 's|LFLAGS = -s \(.*\)|LDLIBS = -lm \1|' \
  -e 's|$(CC) $^ $(LFLAGS) -o $@|$(CC) $(LDFLAGS) $^ $(LDLIBS) -o $@|' -i Makefile


%build
%set_build_flags
%make_build


%install
# Install game
install -d %{buildroot}%{_bindir}
install -p -m 755 %{name}-sdl %{buildroot}%{_bindir}

# Install data
install -d %{buildroot}%{_datadir}/%{name}/sound
install -p -m 644 sound/*.ogg %{buildroot}%{_datadir}/%{name}/sound

# Install desktop file
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
install -p -m 644 gendata256/last-mission.png \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/


%files
%{_bindir}/%{name}-sdl
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%license COPYING.txt
%doc AUTHORS.txt CHANGELOG.txt README.txt


%changelog
* Sat Jun 01 2024 Andrea Musuruane <musuruan@gmail.com> - 0.8-1
- First release
