Name:           opentyrian
Version:        2.1.20221123
Release:        1%{?dist}
Summary:        An arcade-style vertical scrolling shooter

License:        GPLv2+
URL:            https://github.com/opentyrian/opentyrian
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_net-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme


%description
OpenTyrian is an arcade-style vertical scrolling shooter. The story is set
in 20,031 where you play as Trent Hawkins, a skilled fighter-pilot employed
to fight Microsol and save the galaxy.

This package needs game data from the original Tyrian game, which is
available as a freeware.


%prep
%autosetup


%build
%set_build_flags
%make_build \
  TYRIAN_DIR=%{_datadir}/tyrian \
  OPENTYRIAN_VERSION=%{version}


%install
# Install binary
install -d %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}/%{name}

# Install man page
install -d %{buildroot}%{_mandir}/man6
install -p -m 644 linux/man/opentyrian.6 \
  %{buildroot}%{_mandir}/man6/opentyrian.6

# Install icons
for i in 22 24 32 48 128; do
  install -d %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
  install -p -m 644 linux/icons/tyrian-${i}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  linux/opentyrian.desktop

# Install AppData file
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

# Install README.Fedora
cat > README.Fedora << EOF
For running opentyrian you have to download the Tyrian Freeware game assets.
These can be installed using game-data-packager.
EOF


%files
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6*
%doc README NEWS README.Fedora
%license COPYING


%changelog
* Mon May 27 2024 Andrea Musuruane <musuruan@gmail.com> - 2.1.20221123-1
- First release
