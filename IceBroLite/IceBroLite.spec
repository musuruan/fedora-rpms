Name:           IceBroLite
Version:        1.18
Release:        2%{?dist}
Summary:        External Debugger for VICE 3.5 and higher

# TODO: clarify license
License:        unknown
URL:            https://github.com/Sakrac/IceBroLite
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# Fix format security issues
# https://github.com/Sakrac/IceBroLite/pull/47
Patch0:         %{name}-1.18-fmt_string.patch
# VICE executable selector is Windows only
# https://github.com/Sakrac/IceBroLite/issues/48
Patch1:         %{name}-1.18-vice_file_selector.patch

BuildRequires:  make
BuildRequires:  gcc-g++
BuildRequires:  glfw-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
#BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme

# imgui is not yet packaged
# https://github.com/ocornut/imgui/
Provides:       bundled(imgui) = 1.89.2

%description
IceBro Lite is a source-level debugger with a graphical user interface (GUI).
The primary purpose of the IceBro Lite debugger is to inspect and validate
assembler code.

IceBro Lite is designed for use with the VICE C64 emulator, version 3.5. More
specifically, it’s built to take advantage of the new binary monitor protocol
introduced in VICE C64 3.5


%prep
%autosetup -p1

# Fix Makefile
sed -i 's/CXXFLAGS =/CXXFLAGS +=/' src/Makefile
sed -i '/CXXFLAGS += -g -O2 -Wall -Wformat/d' src/Makefile
sed -i 's/$(CXX) -o $@ $^ $(CXXFLAGS) $(LIBS)/$(CXX) -o $@ $^ $(LDFLAGS) $(LIBS)/' src/Makefile


%build
%set_build_flags
%make_build -C src


%install
# Install binary
install -d %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}

# Install desktop file
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# Resize and install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
convert -resize 48x48 \
  -extent 48x48 \
  -gravity center \
  -background none \
  assets/icebrolite.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


# TODO: appData file


%files
#license add-license-file-here
%doc manual.MD
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Fri Dec 29 2023 Andrea Musuruane <musuruan@gmail.com> - 1.18-2
- Fix VICE executable selector

* Sun Dec 24 2023 Andrea Musuruane <musuruan@gmail.com> - 1.18-1
- Updated to new upstream release

* Fri Dec 30 2022 Andrea Musuruane <musuruan@gmail.com> - 1.1-1
- First version
