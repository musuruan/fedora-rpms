Name:           Nuked-MD
Version:        1.2
Release:        1%{?dist}
Summary:        Cycle accurate Mega Drive emulator

License:        GPL-2.0-or-later
URL:            https://github.com/nukeykt/Nuked-MD
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Fix missing string.h include in cartridge.c
# https://github.com/nukeykt/Nuked-MD/commit/b875cd79104217af581131b22f4111409273617a.patch
Patch0:         %{name}-1.2-fix_missing_include.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  SDL2-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Cycle accurate Mega Drive core. The goal of this project is to emulate Sega
Mega Drive chipset accurately as possible using decapped chips photos.


%prep
%autosetup -p1


%build
%cmake
%cmake_build


%install
# Install binary
install -d %{buildroot}%{_bindir}
install -p -m 755 %{__cmake_builddir}/%{name} %{buildroot}%{_bindir}


%files
%license LICENSE
%doc *.md *.png
%{_bindir}/%{name}


%changelog
* Thu Aug 15 2024 Andrea Musuruane <musuruan@gmail.com> - 1.2-1
- First release
