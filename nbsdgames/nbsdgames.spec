Name:           nbsdgames
Version:        6.0.2
Release:        1%{?dist}
Summary:        21 new, improved, text-based games

License:        CC0-1.0
URL:            https://github.com/abakh/nbsdgames
Source0:        https://github.com/abakh/nbsdgames/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
A package of 21 new, improved, text-based games. Some are entirely original
ideas. Best and lightest! Years of free, fun and endless brain exercise for
everyone.

%prep
%autosetup


%build
%make_build nb


%install
make nbinstall DESTDIR=/builddir/build/BUILD/nbsdgames-6.0.2-build/BUILDROOT 'INSTALL=/usr/bin/install -p'
make nbmanpages DESTDIR=/builddir/build/BUILD/nbsdgames-6.0.2-build/BUILDROOT 'INSTALL=/usr/bin/install -p'

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  src/%{name}.desktop

# Install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 src/%{name}.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps


%files
%license LICENSE
%doc README.md
%{_bindir}/nb*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man6/nb*.6*


%changelog
* Sat Oct 03 2026 Andrea Musuruane <musuruan@gmail.com> - 6.0.2-1
- First release

