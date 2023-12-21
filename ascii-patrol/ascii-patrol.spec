Name:           ascii-patrol
Version:        1.7
Release:        1%{?dist}
Summary:        An ASCII game project which was mainly inspired by Moon Patrol

License:        GPLv3
URL:            http://ascii-patrol.com/
Source0:        https://github.com/msokalski/ascii-patrol/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  pulseaudio-libs-devel
# It is required for highscores table support
Requires:       curl

%description
Ascii Patrol is an ASCII game project. It was mainly inspired by "Moon Patrol". 

%prep
%autosetup -n %{name}-%{version}

# Fix Makefile
sed -i 's/CXXFLAGS = -Wno-multichar -O3 -D NIX/CXXFLAGS += -D NIX/' \
  Makefile
sed -i 's/LDFLAGS  = -pthread/LDFLAGS  += -pthread/' Makefile


%build
%set_build_flags
%make_build


%install
# Install binary
install -d %{buildroot}%{_bindir}
install -m 755 asciipat %{buildroot}%{_bindir}


%files
%{_bindir}/asciipat
%license LICENSE
%doc README.md


%changelog
* Sat Sep 11 2021 Andrea Musuruane <musuruan@gmail.com> - 1.7-1
- Update to new upstream realese

* Wed May  8 2019 Andrea Musuruane <musuruan@gmail.com> - 1.4-1
- First release
