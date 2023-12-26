Name:           little-spy
Version:        1.0.6
Release:        1%{?dist}
Summary:        Recover stolen intelligence and technology

License:        MIT
URL:            https://github.com/wimpysworld/little-spy
Source0:        https://github.com/wimpysworld/little-spy/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        export_presets.cfg
Source2:        %{name}.metainfo.xml

BuildRequires:  godot3-headless
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       godot3-runner
Requires:       hicolor-icon-theme

BuildArch:      noarch

ExcludeArch:    ppc64le
ExcludeArch:    s390x

%description
Airdrop into an enemy stronghold, recover stolen intelligence and technology.

Collect as much stolen intelligence and technology as you can and get to the
extraction point before the helicopter leaves without you. Earn a higher agent
ranking by collecting more items and complete the mission as fast as possible
to earn a higher bonus.


%prep
%autosetup
cp -a %{SOURCE1} .


%build
godot3-headless --export-pack "Linux64" %{name}.pck


%install
install -d %{buildroot}%{_datadir}/%{name}
install -p -m 644 %{name}.pck %{buildroot}%{_datadir}/%{name}

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --remove-key=Version \
  --set-key=Exec \
  --set-value="godot3-runner --main-pack %{_datadir}/%{name}/%{name}.pck" \
  --set-icon=%{name} \
  --dir %{buildroot}%{_datadir}/applications \
  snap/gui/%{name}.desktop

# Install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -p -m 644 snap/gui/%{name}.png \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

# Install appData file
install -d %{buildroot}%{_metainfodir}
install -p -m 644 %{SOURCE2} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml
%license LICENSE.md
%doc README.md


%changelog
* Tue Dec 26 2023 Andrea Musuruane <musuruan@gmail.com> - 1.0.6-1
- First version
