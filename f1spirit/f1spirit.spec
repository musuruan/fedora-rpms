Name:           f1spirit
Version:        1.0
Release:        0.rc9%{?dist}
Summary:        Konami's F-1 Spirit remake

License:        Distributable
URL:            http://f1spirit.jorito.net/
Source0:        http://braingames.jorito.net/f1spirit/f1spirit.src_0.rc9-1615.tgz
Patch0:         %{name}-1.0-Makefile.patch
Patch1:         %{name}-1.0-gcc6.patch
Patch2:         %{name}-1.0-format_string.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_net-devel
BuildRequires:  libcurl-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils 


%description
This is a remake of racing game developed by Konami for the MSX home 
computer systems in 1987. 

You will race with many different types of cars, starting by Stock or Rally 
cars, and finishing by driving F1 cars (once you have classified for it by 
passing for F3, F3000 and Endurance cars).


%prep
%autosetup -p1 -n %{name}-0.rc9.1615

# Fix to compile with current libcurl
sed -i '/#include <curl\/types.h>/d' sources/*.cpp

# Fix Icon in desktop file
sed -i 's/Icon=f1spirit.png/Icon=f1spirit/' build/linux/f1spirit.desktop

# Fix char encoding
iconv --from=ISO-8859-1 --to=UTF-8 readme.txt > readme.txt.utf8
touch -r readme.txt readme.txt.utf8
mv readme.txt.utf8 readme.txt


%build
%set_build_flags
%make_build

%install
%make_install

# Install desktop file
desktop-file-install \
  --delete-original \
  --remove-category Application \
  --remove-key Encoding \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%doc readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Wed Jan 03 2024 Andrea Musuruane <musuruan@gmail.com> 1.0-0.rc9
- First release
