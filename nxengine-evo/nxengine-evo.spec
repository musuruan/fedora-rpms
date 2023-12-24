%global gittag v2.6.5-1 
%global tr_version 1.14

Name:           nxengine-evo
Version:        2.6.5.1
Release:        2%{?dist}
Summary:        Jump-and-run platformer

# Cave Story files are freeware
License:        GPLv3+ and freeware
URL:            https://github.com/nxengine/nxengine-evo
Source0:        https://github.com/nxengine/nxengine-evo/archive/%{gittag}/%{name}-%{version}.tar.gz
Source1:        https://github.com/nxengine/translations/releases/download/v%{tr_version}/all.zip#/%{name}-lang-%{tr_version}.zip
Source2:        https://www.cavestory.org/downloads/cavestoryen.zip
# Fix compiling with GCC 13
# https://github.com/nxengine/nxengine-evo/issues/280
Patch0:         %{name}-2.6.5.1-gcc13.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
NXEngine Evo is a complete open-source clone/rewrite of the masterpiece
jump-and-run platformer Doukutsu Monogatari (also known as Cave Story).

NXEngine Evo is an upgraded/refactored version of NXEngine by Caitlin Shaw.


%prep
%autosetup -n %{name}-2.6.5-1 -p1
%setup -q -T -D -a 1 -n %{name}-2.6.5-1
%setup -q -T -D -a 2 -n %{name}-2.6.5-1

# Fix end-of-line encoding
sed -i 's/\r//' CaveStory/Readme.txt


%build
%cmake
%cmake_build

# Extract content
cp -ar CaveStory/data/* data

cp CaveStory/Doukutsu.exe .
./%{_vpath_builddir}/nxextract


%install
%cmake_install

# Remove nxextract
rm  %{buildroot}%{_bindir}/nxextract

# Validate desktop file
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/org.nxengine.nxengine_evo.desktop

# Validate AppData file
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.nxengine.nxengine_evo.appdata.xml


%files
%{_bindir}/%{name}
%{_datadir}/nxengine
%{_datadir}/applications/org.nxengine.nxengine_evo.desktop
%{_datadir}/icons/hicolor/*/apps/org.nxengine.nxengine_evo.png
%{_metainfodir}/org.nxengine.nxengine_evo.appdata.xml
%license LICENSE
%doc README.md CaveStory/Readme.txt CaveStory/Manual CaveStory/Manual.html


%changelog
* Sun Apr 02 2023 Andrea Musuruane <musuruan@gmail.com> - 2.6.5.1-2
- Fix compiling with GCC 13

* Mon Aug 09 2021 Andrea Musuruane <musuruan@gmail.com> - 2.6.5.1-1
- First release
