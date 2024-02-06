Name:           leocad
Version:        23.03
Release:        1%{?dist}
Summary:        CAD program for creating virtual LEGO models

License:        GPLv2
URL:            http://www.leocad.org
Source0:        https://github.com/leozide/leocad/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtgamepad-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib


%description
CAD program for creating virtual LEGO models.

It has an intuitive interface, designed to allow new users to start creating
new models without having to spend too much time learning the application.


%prep
%autosetup

# Fix UTF-8 encoding
pushd docs
iconv --from=ISO-8859-1 --to=UTF-8 CREDITS.txt > CREDITS.txt.utf8
mv CREDITS.txt.utf8 CREDITS.txt
popd


%build
%qmake_qt5 DISABLE_UPDATE_CHECK=1 \
  QMAKE_CXXFLAGS="$CXXFLAGS" \
  QMAKE_LFLAGS="$LDFLAGS"
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}

# Handle doc in files section
rm -rf %{buildroot}%{_docdir}

# Validate desktop file
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

# Validate AppData file
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files
%license docs/COPYING.txt
%doc docs/{README.txt,CREDITS.txt}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/*/mimetypes/application-vnd.%{name}.*


%changelog
* Tue Feb 06 2024 Andrea Musuruane <musuruan@gmail.com> - 23.03-1
- Updated to new upstream release

* Mon Feb 20 2023 Andrea Musuruane <musuruan@gmail.com> - 21.06-1
- First release
