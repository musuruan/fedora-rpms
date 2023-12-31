Name:           crates
Version:        0.7.3
Release:        1%{?dist}
Summary:        3D puzzle game

License:        GPLv3+
URL:            http://www.octaspire.com/crates/
Source0:        https://github.com/octaspire/crates/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.sh
Patch0:         %{name}-0.7.3-cflags.patch
Patch1:         %{name}-0.7.3-comments.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  libGLU-devel
BuildRequires:  compat-lua-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme


%description
OCTASPIRE CRATES! is challenging and fun three dimensional puzzle game. 
It comes with a default mission containing 30 levels and 35 different game 
entities. Playing the whole default mission in one go will take a little bit 
more than twenty minutes from experienced player doing no mistakes, but in 
the beginning it will take probably much, much longer. 


%prep
%autosetup -p1


%build
%cmake #-DCMAKE_BUILD_TYPE:STRING=Debug 
%cmake_build 


%install
# Install wrapper script
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}

# Install main executable
mkdir -p %{buildroot}%{_libexecdir}/%{name}
install -m 755 %{name} %{buildroot}%{_libexecdir}/%{name}

# Install data
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -aR resources %{buildroot}%{_datadir}/%{name}

# Install man page
mkdir -p %{buildroot}%{_mandir}/man6
install -m 644 man/man6/%{name}.6 %{buildroot}%{_mandir}/man6

# Install icons
for i in 16 24 48; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
  convert resources/images/crateslogo${i}x${i}x32.ico \
    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}


%files
%{_bindir}/%{name}
%{_libexecdir}/%{name}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*
%doc COPYING HISTORY README


%changelog
* Sun Dec 31 2023 Andrea Musuruane <musuruan@gmail.com> - 0.7.3-1
- First release
