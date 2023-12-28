Name:           CodenameLT
Version:        1.0.5
Release:        1%{?dist}
Summary:        Run without getting caught by evil agents

# Code is under MIT License. Music and graphics are under CC-BY 4.0 License
License:        MIT and CC-BY
URL:            https://bakudas.itch.io/clt
Source0:        https://github.com/VacaRoxa/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# LUA 11.0 compatibility fixed from upstream
Patch0:         %{name}-1.0.5-love11.0_compatibility.patch

BuildArch:      noarch

BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
Requires:       love


%description
A pixel art game where you have to run without getting caught by evil agents.


%prep
%autosetup -p1

# Fix execution script
sed -i 's!love project/!love %{_datadir}/%{name}/%{name}.love!' run.sh

# Fix desktop file
sed -i 's!Icon=.*$!Icon=%{name}!' \
  dist/snap-template/snap/gui/codenamelt.desktop
mv dist/snap-template/snap/gui/codenamelt.desktop \
  dist/snap-template/snap/gui/%{name}.desktop


%build
pushd project
#love "binary" files are just zipped sources, but should exclude docs
zip -r %{name}.love . -x Readme.md
popd


%install
#Install execution script
install -d %{buildroot}%{_bindir}
install -p -m 755 run.sh \
  %{buildroot}%{_bindir}/%{name}

#Install love file
install -d %{buildroot}%{_datadir}/%{name}
install -p -m 644 project/%{name}.love \
  %{buildroot}%{_datadir}/%{name}/%{name}.love

#Install desktop file
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  dist/snap-template/snap/gui/%{name}.desktop

# Install icons
install -d %{buildroot}%{_datadir}/icons/hicolor/512x512/apps
install -p -m 644 icon/icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

for px in 48 64 256; do
  install -d %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps
  convert -resize ${px}x${px} \
    icon/icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps/%{name}.png
done


%files
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.love
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%license LICENSE COPYRIGHT
%doc README.md


%changelog
* Thu Mar 21 2019 Andrea Musuruane <musuruan@gmail.com> - 1.0.5-1
- First release
