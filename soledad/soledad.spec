Name:           soledad
Version:        1.3
Release:        1%{?dist}
Summary:        Help Sol stop robots destroying the park

License:        GPLv3+
URL:            https://azurasun.com/
Source0:        https://azurasun.com/download/sol_130_final_pc_win_linux.zip
Source2:        %{name}-Makefile
Source3:        %{name}.png
Source4:        %{name}.desktop

BuildRequires:  gcc
BuildRequires:  unzip
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  SDL2-devel
BuildRequires:  physfs-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  speech-dispatcher-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
The park is being destroyed by the powerful corporation Black Moon and Sol
can't let that happen! Help her stop them before it's too late! Use power-ups
to obtain new abilities like flying, climbing walls, smashing through floors
or even gliding over large gaps. 


%prep
%setup -q -n "Sol 1.30 Final PC Win Linux"

# Unzip source code
unzip source/sol130_source.zip

# Copy makefile
cp -a %{SOURCE2} source/Makefile

# Remove stuff
rm source/sol130_source.zip
rm -rf lib
rm -f *.dll
rm soledad
rm soledad.exe

# Fix libspeechd.h path
sed -i 's|#include <libspeechd.h>|#include <speech-dispatcher/libspeechd.h>|' source/reader.c

# IUP is not in Fedora
sed -i 's|#define HAS_LAUNCHER 1|#define HAS_LAUNCHER 0|' source/main.h


%build
pushd source
%set_build_flags
%make_build
popd


%install
# Install binary
mkdir -p  %{buildroot}%{_bindir}
install -m 0755 source/%{name} %{buildroot}%{_bindir}

# Install data
mkdir -p  %{buildroot}%{_datadir}/%{name}
install -m 0644 soledad.dat %{buildroot}/%{_datadir}/%{name}

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE4}


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%license LICENSE
%doc doc/changelog.txt


%changelog
* Sat Oct 07 2023 Andrea Musuruane <musuruan@gmail.com> - 1.3-1
- Updated to new upstream release

* Mon Dec 07 2015 Andrea <musuruan@gmail.com> - 1.2-1
- First release
