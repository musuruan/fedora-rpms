Name:           hypnotix
Version:        4.4
Release:        1%{?dist}
Summary:        An M3U IPTV Player

# Icons on the landing page: CC BY-ND 2.0
License:        GPL-3.0-or-later and CC-BY-ND-2.0
URL:            https://github.com/linuxmint/hypnotix
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme
Requires:       xapps
Requires:       mpv-libs
Requires:       python3-cairo
Requires:       python3-cinemagoer
Requires:       python3-setproctitle
Requires:       python3-unidecode
Requires:       python3-gobject
Requires:       python3-requests
Requires:       yt-dlp

%description
Hypnotix is an IPTV streaming application with support for live TV, movies
and series.


%prep
%autosetup

# Remove shebang from non executable scripts
sed -i -e '/^#!/, 1d' usr/lib/hypnotix/xtream.py

# Set version
sed -i "s/__DEB_VERSION__/%{version}/g" usr/lib/hypnotix/hypnotix.py


%build
%make_build

%install
# Install
install -d %{buildroot}
cp -a .%{_prefix} %{buildroot}

# Validate desktop file
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%files -f %{name}.lang
%license debian/copyright
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.x.%{name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_prefix}/lib/%{name}


%changelog
* Tue Jun 18 2024 Andrea Musuruane <musuruan@gmail.com> - 4.4-1
- Updated to new upstream release

* Tue Feb 06 2024 Andrea Musuruane <musuruan@gmail.com> - 4.3-1
- Updated to new upstream release

* Tue Jun 21 2022 Andrea Musuruane <musuruan@gmail.com> - 2.7-1
- Updated to new upstream release

* Sun Mar 28 2021 Andrea Musuruane <musuruan@gmail.com> - 1.5-1
- Updated to new upstream release

* Fri Jan 15 21:35:45 CET 2021 Andrea Musuruane <musuruan@gmail.com> - 1.4-1
- First release
