Name:           balatro
Version:        1.0.1o
Release:        1%{?dist}
Summary:        A deck-building roguelite

License:        Commercial
URL:            https://www.playbalatro.com/
Source0:        Balatro.exe
Source1:        %{name}.sh
# Desktop file taken from AUR
Source2:        %{name}.desktop

BuildArch:      noarch

BuildRequires:  zip
BuildRequires:  icoutils
BuildRequires:  desktop-file-utils
Requires:       love

%description
Balatro is a hypnotically satisfying deckbuilder where you play illegal poker
hands, discover game-changing jokers, and trigger adrenaline-pumping,
outrageous combos.


%prep
%setup -c -T -n %{name}-%{version}
unzip %{SOURCE0} || true
wrestool -x -t14 -o . %{SOURCE0}
icotool -x *.ico


%build
zip -r9 %{name}.love *.lua *.jkr */

%install
#Install execution script
install -d %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE1} \
  %{buildroot}%{_bindir}/%{name}

#Install love file
install -d %{buildroot}%{_datadir}/%{name}
install -p -m 644 %{name}.love \
  %{buildroot}%{_datadir}/%{name}/%{name}.love

#Install desktop file
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE2}

# Install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 Balatro.exe_14_MAINICON_0_3_32x32x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


%files
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.love
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Sat Apr 25 2026 Andrea Musuruane <musuruan@gmail.com> - 1.0.1o-1
- First release
