Name:           goattracker
Version:        2.76
Release:        1%{?dist}
Summary:        A crossplatform music editor for creating Commodore 64 music

License:        GPLv2+
URL:            http://covertbitops.c64.org/
Source0:        http://downloads.sourceforge.net/%{name}2/GoatTracker_%{version}.zip
# Desktop file from Debian
Source1:        %{name}.desktop

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  SDL-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme


%description
This is a crossplatform C64 music editor. Supports emulated output via Dag
Lem's reSID engine, the HardSID soundcard or CatWeasel MK3.

It supports emulated output via the software reSID engine, the HardSID
soundcard, or the Catweasel (MK3/MK4) controller card, and produces songs in
its own format (*.SNG). The program can also export tunes in SID format, BIN
format, or Commodore PRG format for inclusion on a floppy you can stick into
a 1541/1571/1581 drive.

Like most tracker programs, the program is able to import instrument files,
create and modify track patterns, set the order of playback of patterns and
change details of the song such as the title and author. If you are familiar
with tracker-like programs, then GoatTracker will feel like a simple version
of those, though with differences attributable to the hardware. People new to
composing in general should look up other information on composing on the
C64.


%prep
%autosetup -c %{name}-%{version}

# Clean sources
rm -rf win32
rm -rf src/bme/*.exe

# Fix end-of-line encoding
sed -i 's/\r//' {authors,readme.txt}

# Fix UTF-8 encoding
iconv --from=ISO-8859-1 --to=UTF-8 readme.txt > readme.txt.utf8
mv readme.txt.utf8 readme.txt


# Fix Makefile
sed -i 's/-Ibme -Iasm -O3/-Ibme -Iasm/' src/makefile.common
sed -i 's/$(CC)/$(CC) $(LDFLAGS)/' src/makefile.common
sed -i 's/$(CXX)/$(CXX) $(LDFLAGS)/' src/makefile.common
sed -i '/strip/d' src/makefile.common


%build
pushd src
%set_build_flags
%make_build
popd


%install
# Install binary
install -d %{buildroot}%{_bindir}
install -p -m 755 linux/goattrk2 \
  %{buildroot}%{_bindir}/%{name}
install -p -m 755 linux/{gt2reloc,ins2snd2,mod2sng,sngspli2} \
  %{buildroot}%{_bindir}

# Install examples
install -d %{buildroot}%{_datadir}/%{name}
cp -aR examples %{buildroot}%{_datadir}/%{name}

# Install man page
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 linux/%{name}.1 \
  %{buildroot}%{_mandir}/man1/%{name}.1

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --set-icon=%{name} \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# Install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
convert src/goattrk2.ico \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


%files
%license copying
%doc authors goat_tracker_commands.pdf readme.txt
%{_bindir}/%{name}
%{_bindir}/{gt2reloc,ins2snd2,mod2sng,sngspli2}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*


%changelog
* Sun Jul 03 2022 Andrea Musuruane <musuruan@gmail.com> - 2.76-1
- First release
 
