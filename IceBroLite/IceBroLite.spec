Name:           IceBroLite
Version:        1.1
Release:        1%{?dist}
Summary:        External Debugger for VICE 3.5 and higher

# TODO: clarify license
License:        unknown
URL:            https://github.com/Sakrac/IceBroLite
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Patch0:         %{name}-1.1-fmt_string.patch

BuildRequires:  make
BuildRequires:  gcc-g++
BuildRequires:  glfw-devel
BuildRequires:  desktop-file-utils
#BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme
# TODO: remove boundled imgui
# https://github.com/ocornut/imgui/

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

# Install icon
# TODO: l'icona non viene visualizzata
install -d %{buildroot}%{_datadir}/icons/hicolor/42x42/apps
install -m 644 -p assets/icebrolite.png \
  %{buildroot}%{_datadir}/icons/hicolor/42x42/apps/%{name}.png

# TODO: appData file


%files
#license add-license-file-here
%doc manual.MD
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Fri Dec 30 2022 Andrea Musuruane <musuruan@gmail.com> - 1.1-1
- First version
