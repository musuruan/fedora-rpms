Name:           gearlynx
Version:        0.0.7
Release:        1%{?dist}
Summary:        Atari Lynx emulator and debugger

License:        GPL-3.0-or-later
URL:            https://github.com/drhelius/Gearlynx
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  SDL2-devel
BuildRequires:  gtk3-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Gearlynx is a cross-platform Atari Lynx emulator written in C++.

This is an open source project with its ongoing development made possible
thanks to the support by these awesome backers. If you find it useful, please
consider sponsoring.


%prep
%autosetup -n Gearlynx-%{version}


%build
%set_build_flags
%make_build -C platforms/linux/


%install
# Install binary
install -d %{buildroot}%{_bindir}
install -p -m 755 platforms/linux/%{name} %{buildroot}%{_bindir}

# Install icons
for i in 16 32 64 128 256 512; do
  install -d %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
  convert -resize x${i} platforms/macos/image.png \
    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}


%files
%license LICENSE
%doc README.md backers.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Thu Oct 09 2025 Andrea Musuruane <musuruan@gmail.com> - 0.0.7-1
- Updated to new upstream release

* Sat Oct 04 2025 Andrea Musuruane <musuruan@gmail.com> - 0.0.5-1
- First release
 
