Name:           dablin
Version:        1.15.0
Release:        1%{?dist}
Summary:        DAB/DAB+ receiver (including ETI-NI and EDI AF playback)

License:        GPLv3+
URL:            https://github.com/Opendigitalradio/dablin
Source0:        https://github.com/Opendigitalradio/dablin/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libmpg123-devel
BuildRequires:  faad2-devel
# HE-AAC is not correct with this decoder
#BuildRequires:  fdk-aac-devel
BuildRequires:  SDL2-devel
BuildRequires:  gtkmm30-devel

%description
DABlin plays a DAB/DAB+ audio service – from a live transmission or from a
stored ensemble recording (ETI-NI, or EDI AF with ETI). Both DAB (MP2) and
DAB+ (AAC-LC, HE-AAC, HE-AAC v2) services are supported.

%package gtk
Summary:  DAB/DAB+ receiver for Linux/GTK (including ETI-NI playback)
Requires: %{name} = %{version}-%{release}

%description gtk
DABlin plays a DAB/DAB+ audio service – from a live transmission or from a
stored ensemble recording (ETI-NI, or EDI AF with ETI). Both DAB (MP2) and
DAB+ (AAC-LC, HE-AAC, HE-AAC v2) services are supported.

The GTK GUI version in addition supports the data applications Dynamic Label
and MOT Slideshow (if used by the selected service).


%prep
%autosetup 

# Do not strip symbols
sed -i '/SET(CMAKE_EXE_LINKER_FLAGS  "${CMAKE_EXE_LINKER_FLAGS} -s")/d' \
  CMakeLists.txt


%build
#cmake -DUSE_FDK-AAC=1
%cmake
%cmake_build


%install
%cmake_install


%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files gtk
%license COPYING
%{_bindir}/%{name}_gtk
%{_mandir}/man1/%{name}_gtk.1*


%changelog
* Sat Aug 12 2023 Andrea Musuruane <musuruan@gmail.com> - 1.15.0-1
- Update to new upstream version

* Sun Sep 12 2021 Andrea Musuruane <musuruan@gmail.com> - 1.13.0-1
- Update to new upstream version

* Mon Sep 23 2019 Andrea Musuruane <musuruan@gmail.com> - 1.11.0-1
- First release 
