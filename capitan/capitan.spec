Name:           capitan
Version:        1.0.3 
Release:        2%{?dist}
Summary:        Save Seville from the evil Torrebruno

License:        GPLv3+
URL:            http://computeremuzone.com/ficha.php?id=754&l=en
Source0:        http://computeremuzone.com/pc/Capitan.tar.bz2
Source1:        %{name}.appdata.xml
# Fix Makefile
Patch0:         %{name}-1.0.3-Makefile.patch
# Patches from OpenBSD
# Fix building with libpng-1.5
Patch1:         %{name}-1.0.3-loadpng.patch
# Fix a random crash that happened during the second screen in the game
Patch2:         %{name}-1.0.3-background.patch
# Fix datadir
Patch3:         %{name}-1.0.3-messages.patch
Patch4:         %{name}-1.0.3-hardware.patch
Patch5:         %{name}-1.0.3-partida.patch
Patch6:         %{name}-1.0.3-presentacion.patch
Patch7:         %{name}-1.0.3-logger.patch
Patch8:         %{name}-1.0.3-sonido.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  allegro-devel
BuildRequires:  alfont-devel
BuildRequires:  AllegroOGG-devel
BuildRequires:  libpng-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme


%description
A calm day begins in Seville. Mariano López goes to his job as sausage 
delivery man. Meanwhile, at Santiponce's interstratospheric device center, 
everybody is getting ready to the first fully Spanish rocket launch, 
designed by famous Dr. Torrebruno, an eminent nuclear physicist who had to 
leave the project prematurely, due to a strange mental disease. But nobody 
expected the rocket to suffer a sudden variation on its path, and falls 
right on the truck that Mariano López uses to transport a blood sausages 
cargo.

Mariano, unconscious, lies on the floor besides his sausages and the 
truck's wreckage, spread all around. Some hours later, he wakes up really 
hungry, and eats an entire box of the radiated blood sausages. But... what 
the hell is happening!? Mariano is becoming different: Every muscle grows, 
he becomes taller, his ugly face becomes a pretty superhero's, Captain 'S', 
who discovers that everything was part of the evil Torrebruno's plan, with 
the true intention of ruling the World, starting by Seville.


%package data
Summary: Data files for %{name}
Requires: %{name} = %{version}
BuildArch: noarch

%description data
Data files for %{name}


%prep
%autosetup -p0

# Delete executable
rm %{name} 

# Delete bundled libraries
rm -rf dependencies

# Use Fedora libAllegroOGG 
sed -i "s!lalogg!lAllegroOGG!" Makefile
sed -i "s!alogg\.h!AllegroOGG/alogg\.h!" src/include/constantes.h

# Fix desktop file
sed -i "s!Icon=capitan.png!Icon=capitan!" extra/%{name}.desktop


%build
%set_build_flags
export CXXFLAGS+=' -DCAPITAN_DATA_DIR=\"%{_datadir}/%{name}/\"'
%make_build 


%install
# Install game
install -d %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}

# Install data
install -d %{buildroot}%{_datadir}/%{name}
cp -pr data lang %{buildroot}%{_datadir}/%{name}

# Install icon
install -d %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
install -p -m 644 extra/%{name}.png \
  %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/

# Install desktop file
desktop-file-install \
  --remove-category Application \
  --remove-key Encoding \
  --dir %{buildroot}%{_datadir}/applications \
  extra/%{name}.desktop

# Install AppData file
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml
%doc extra/instructions.pdf
%license docs/license.txt

%files data
%{_datadir}/%{name}


%changelog
* Sat Sep 11 2021 Andrea Musuruane <musuruan@gmail.com> - 1.0.3-2
- Add make to BR

* Thu Aug 16 2018 Andrea Musuruane <musuruan@gmail.com> 1.0.3-1
- First release
