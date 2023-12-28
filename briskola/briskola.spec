Name:           briskola
Version:        1.0.0
Release:        2%{?dist}
Summary:        An Italian trick-taking card game 
Summary(it):    Gioco di carte della Briscola

License:        GPLv2+
URL:            http://www.briskola.net/
Source0:        http://www.briskola.net/files/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
# Fix desktop file
Patch0:         %{name}-1.0.0-desktop.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 2.6
BuildRequires:  qt4-devel >= 4.5.3
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib


%description
Briscola is one of the most popular Italian card games because of its simple
rules and the modest ability required to be played.


%description -l it
La Briscola è uno dei giochi di carte più popolari in Italia grazie alle
sue semplici regole e alla modesta abilità richiesta ai giocatori.


%prep
%setup -q
%patch0 -p1


%build
%cmake
%cmake_build


%install
%cmake_install

# Validate desktop file
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install AppData file
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-icon.png
%{_datadir}/metainfo/%{name}.appdata.xml


%changelog
* Sat Sep 11 2021 Andrea Musuruane <musuruan@gmail.com> - 1.0.0-2
- rebuilt

* Fri Jul 13 2018 Andrea Musuruane <musuruan@gmail.com> - 1.0.0-1
- First release
