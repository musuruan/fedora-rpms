%global commit 8aeac7bd9fa7

Name:           blastem
Version:        0.6.2
Release:        1%{?dist}
Summary:        The fast and accurate Genesis emulator

License:        GPL-3.0-or-later
URL:            https://www.retrodev.com/blastem/
Source0:        https://www.retrodev.com/repos/blastem/archive/%{commit}.tar.gz#/%{name}-%{version}.tar.gz
# Desktop file from NetBSD package 
Source1:        %{name}.desktop
# Appdata file from flathub
Source2:        com.retrodev.%{name}.appdata.xml
# Man page from Debian
Source3:        %{name}.6
# Fix broken enum definitions that cause multiple definition errors
# when building with -fno-common which is now the default in GCC 10
# https://www.retrodev.com/repos/blastem/raw-rev/e45a317802bd
Patch0:         %{name}-0.6.2-gcc10.patch
# Fix a couple of small memory leaks
# https://www.retrodev.com/repos/blastem/raw-rev/dda7479f3bbb
Patch1:         %{name}-0.6.2-memleaks.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  SDL2-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  glew-devel
BuildRequires:  zlib-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pillow
BuildRequires:  icoutils
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme

%description
BlastEm is a highly precise multi-system emulator that emulates the Sega
Genesis/Mega Drive, Master System and Game Gear.

Despite this high accuracy, even the most demanding software runs at full
speed on modest hardware like a 1.6GHz AMD E-350 laptop. 

%prep
%autosetup -n %{name}-%{commit} -p1

# Remove bundled zlib and Android files
rm -rf zlib android

# Fix zlib header
sed -i 's|"zlib/zlib.h"|<zlib.h>|' blastem.c png.c zip.c

# Fix CFLAGS & LDFLAGS
sed \
  -e '/^CFLAGS:=$(OPT) $(CFLAGS)/d' \
  -e '/^LDFLAGS:=$(OPT) $(LDFLAGS)/d' \
  -e 's|^CFLAGS:=|CFLAGS+=|g' \
  -e 's|^LDFLAGS:=|LDFLAGS+=|g' \
  -e 's|$(OPT)|$(LDFLAGS)|g' \
  -e '/^CFLAGS+=/s| $(CFLAGS)||g' \
  -i Makefile


%build
%set_build_flags
%make_build \
  HOST_ZLIB=1 \
  DATA_PATH=%{_datadir}/%{name} \
  CONFIG_PATH=%{_sysconfdir}/%{name}


%install
# Install binary file
install -d %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}

# Install config file
install -d %{buildroot}%{_sysconfdir}/%{name}
install -p -m 644 default.cfg %{buildroot}%{_sysconfdir}/%{name}

# Install data files
install -d %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}/images
install -d %{buildroot}%{_datadir}/%{name}/shaders
install -p -m 644 gamecontrollerdb.txt rom.db %{buildroot}%{_datadir}/%{name}
install -p -m 644 images/*  %{buildroot}%{_datadir}/%{name}/images
install -p -m 644 shaders/*  %{buildroot}%{_datadir}/%{name}/shaders

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# Install icons
icotool -x icons/windows.ico
for px in 16 32 48 256 ;do
  install -d %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps
  install -p -m 0644 windows_*_${px}x${px}x*.png \
     %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps/%{name}.png
done

# Install AppData file
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

# Install man page
install -d %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE3} \
  %{buildroot}%{_mandir}/man6/%{name}.6


%files
%license COPYING
%doc CHANGELOG README
%{_bindir}/%{name}
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/metainfo/com.retrodev.%{name}.appdata.xml
%{_mandir}/man6/%{name}.6*


%changelog
* Fri Mar 15 2024 Andrea Musuruane <musuruan@gmail.com> - 0.6.2-1
- First release
