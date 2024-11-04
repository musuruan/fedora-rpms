Name:           mii_emu
Version:        1.96
Release:        1%{?dist}
Summary:        MII Apple //e Emulator

License:        MIT
URL:            https://github.com/buserror/mii_emu/
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  which
BuildRequires:  mesa-libGLU-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pixman-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

# Bundled libs
Provides: bundled(libmui) = 1.3
Provides: bundled(libmish) = 0.10

%description
An Apple //e emulator with 128K RAM (expandable to 2MB). It supports all known
graphic modes, Mouse Card, Super Serial Card, joystick, Smartport DMA hard
drive card, RAMWorks III card with 1MB RAM, Titan Accelerator //e simulation,
and Terence's J Boldt 1MB ROM card. It supports floppy drive with WOZ 1/2 in
read/write, NIB and DSK in read only . It also includes a built-in debugger
and a super cool looking UI.


%prep
%autosetup

# Fix Version
sed -i 's/(dev)/v%{version}/' Makefile

# Fix install path
sed -i 's!$(DESTDIR)/bin!$(DESTDIR)%{_bindir}!' Makefile

# Fix icon path in docs
sed -i 's!"contrib/mii-icon-64.png"!"%{_datadir}/icons/hicolor/64x64/apps/%{name}_gl.png"!' \
  README.md CHANGELOG.md


%build
%set_build_flags
%make_build


%install
%make_install

# Install docs
install -d %{buildroot}%{_pkgdocdir}/docs/screen
install -p -m 644 CHANGELOG.md README.md \
  %{buildroot}%{_pkgdocdir}
install -p -m 644 docs/screen/* \
  %{buildroot}%{_pkgdocdir}/docs/screen/

# Install desktop file
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  --set-key=Version \
  --set-value=1.5 \
  --set-key=Exec \
  --set-value=%{name}_gl \
  --set-icon=%{name}_gl \
  --remove-category=Emulator \
  --add-category=Emulator \
  contrib/mii_emu.desktop

# Install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
install -p -m 644 contrib/mii-icon-64.png \
  %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}_gl.png


%files
%license LICENSE
%{_bindir}/%{name}_gl
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}_gl.*
%{_pkgdocdir}


%changelog
* Mon Nov 04 2024 Andrea Musuruane <musuruan@gmail.com> - 1.96-1
- First release
