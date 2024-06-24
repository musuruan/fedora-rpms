Name:           gtkmagnetic
Version:        2.3.1
Release:        1%{?dist}
Summary:        An interpreter for Magnetic Scrolls adventures

License:        GPL-3.0-only
URL:            https://msmemorial.if-legends.org/magnetic.php
Source0:        http://www.ifarchive.org/if-archive/magnetic-scrolls/interpreters/magnetic/Magnetic231Src.zip
Source1:        %{name}.desktop
# Patch from Ubuntu Interactive Fiction Team
Patch0:         %{name}-2.3.1-ms_init.patch
# Fix for 64 bit compatibility and other issues
# Patch from Gargoyle via AUR
# https://github.com/garglk/garglk/
Patch1:         %{name}-2.3.1-gargoyle.patch
# Fix format strings
Patch2:         %{name}-2.3.1-sfmt.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gtk2-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme


%description
Magnetic is an interpreter for the games written between 1985 and 1991 by
Magnetic Scrolls, a text adventure producer based in London, England. Although
they only produced seven games they have acquired legendary status for text
adventures of as good quality as Infocom accompanied by exceptional graphics.


%prep
%setup -q -c -n %{name}-%{version} 
%patch 0 -p0
%patch 1 -p0
%patch 2 -p1

pushd Gtk

# Fix end-of-line-encoding
sed -i 's/\r//' BUGS NEWS README TODO

# Fix UTF-8 encoding
iconv --from=ISO-8859-1 --to=UTF-8 README > README.utf8
mv README.utf8 README

# Use SDL mixer for sound
sed -i 's/SOUND_SYSTEM = SMPEG/# SOUND_SYSTEM = SMPEG/' Makefile
sed -i 's/# SOUND_SYSTEM = SDL_MIXER/SOUND_SYSTEM = SDL_MIXER/' Makefile

# Fix LIBS
sed -i 's/LIBS = $(GTK_LIBS) $(SOUND_LIBS)/LIBS = $(GTK_LIBS) $(SOUND_LIBS) -lm/' Makefile

# Fix CFLAGS and LDFLAGS
sed -i 's/CFLAGS = $(EMU_CFLAGS) -ansi/CFLAGS += $(DEF_CFLAGS) -ansi/' Makefile
sed -i 's/$(CC) -o/$(CC) $(CFLAGS) $(LDFLAGS) -o/' Makefile
sed -i 's/$(CC) -c $(EMU_CFLAGS)/$(CC) -c $(CFLAGS)/' Makefile

popd


%build
pushd Gtk
%set_build_flags
%make_build
popd


%install
# Install binary
install -d %{buildroot}%{_bindir}
install -p -m 0755 Gtk/gtkmagnetic %{buildroot}%{_bindir}/%{name}

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# Install icons
for i in  16 32 48 256; do
  install -d %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
  install -p -m 644 Win/icon/bitmaps/${i}x${i}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done


%files
%license COPYING
%doc Gtk/BUGS Gtk/NEWS Gtk/README Gtk/TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Sun Jun 23 2024 Andrea Musuruane <musuruan@gmail.com> - 2.3.1-1
- First release
