Name:           biniax2
Version:        1.30
Release:        3%{?dist}
Summary:        Colorful logic game with arcade and tactics modes

License:        zlib
URL:            http://biniax.com/index2.html
Source0:        http://www.tuzsuzov.com/biniax/%{name}-%{version}-fullsrc.tar.gz
Source1:        %{name}.desktop
# Patch from Gentoo
Patch0:         %{name}-1.30-dotfiles.patch
# Patch from Gentoo
Patch1:         %{name}-1.30-fno-common.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_image-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils 
Requires:       hicolor-icon-theme


%description
Biniax-2 is an original and entertaining game. Takes a minute to learn and
gives you hours and hours of gameplay. There are three game modes (two
singleplayer and one multiplayer), hall of fame, dynamic music and a nice
cartoon look. 


%prep
%autosetup -c -p1

# Remove litter
rm data/Thumbs.db
rm -rf SDLinclude

# Use DATADIR
sed -i 's|data/|%{_datadir}/%{name}/|' desktop/gfx.c desktop/snd.c

# Honor build flags
sed -i 's|$(CC) $(AUTO)|$(CC) $(CFLAGS) $(LDFLAGS) $(AUTO)|' makefile

# Fix end-of-line encoding
sed -i 's/\r//' LICENSE.txt data/text/help.txt
find -type f \( -name '*.h' -o -name '*.c' \) -exec sed -i 's/\r//' '{}' \;

# Fix spurious executable permissions
chmod -x LICENSE.txt data/text/help.txt
find -type f \( -name '*.h' -o -name '*.c' \) -exec chmod -x '{}' \;


%build
%set_build_flags
%make_build biniax


%install
# Install game
install -d %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}

# Install data
install -d %{buildroot}%{_datadir}/%{name}
cp -pr data/* %{buildroot}%{_datadir}/%{name}/

# Install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
convert icon.ico \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%license LICENSE.txt


%changelog
* Sat Jul 09 2022 Andrea Musuruane <musuruan@gmail.com> - 1.30-3
- Fix FTBFS

* Sat Sep 11 2021 Andrea Musuruane <musuruan@gmail.com> - 1.30-2
- Update URL and Source0

* Thu Mar 21 2019 Andrea Musuruane <musuruan@gmail.com> 1.30-1
- First import. 
