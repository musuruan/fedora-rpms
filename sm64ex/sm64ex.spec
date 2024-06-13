# DO NOT DISTRIBUTE PACKAGED RPMS FROM THIS SPEC FILE!

%global ver us
%global forgeurl https://github.com/sm64pc/sm64ex/
%global commit 6f7d974a73037d8ae61fb5dff8e1aec40432e1f8
%global date 20240605
%forgemeta

Name:           sm64ex
Version:        0
Release:        0.1%{?dist}
Summary:        Fork of Super Mario 64 with additional features

License:        Commercial
URL:            https://github.com/sm64pc/sm64ex
Source0:        %{forgesource}
Source1:        baserom.%{ver}.z64
# Icon taken from
# https://www.steamgriddb.com/icon/33056
Source2:        %{name}.png
Source3:        %{name}.desktop

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  glew-devel
BuildRequires:  SDL2-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Princess Peach has been captured! Help Mario rescue her from the evil Bowser.

The game is centered around Princess Peach's Castle, a hub world where Mario
can enter different realms by jumping into enchanted paintings. Each realm
offers multiple missions, requiring players to collect Power Stars to advance.


%prep
%forgesetup

# Fix Makefile
sed -i 's/LDFLAGS := $(BITS) -march=$(TARGET_ARCH) -lm $(BACKEND_LDFLAGS) -lpthread -ldl/LIBS := -lm $(BACKEND_LDFLAGS) -lpthread -ldl/' Makefile
sed -i 's/$(GODDARD_O_FILES) $(LDFLAGS)/$(GODDARD_O_FILES) $(LDFLAGS) $(LIBS)/' Makefile

# Copy ROM
cp -a %{SOURCE1} .


%build
%set_build_flags
PLATFORM_CFLAGS="$CFLAGS" ; export PLATFORM_CFLAGS ;
%make_build VERSION=%{ver} BETTERCAMERA=1 NO_PIE=0


%install
# Install binary
mkdir -p  %{buildroot}%{_bindir}
install -m 0755 build/%{ver}_pc/sm64.%{ver}.f3dex2e \
  %{buildroot}%{_bindir}/%{name}

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 0644 %{SOURCE2} \
   %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE3}


%files
%doc README*.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Sat Jun 08 2024 Andrea Musuruane <musuruan@gmail.com> - 0-0.1.20240605git6f7d974
- First release
