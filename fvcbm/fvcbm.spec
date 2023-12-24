Name:           fvcbm
Version:        3.1 
Release:        1%{?dist}
Summary:        List directories of Commodore 64/128 compatible archive files

License:        GPLv2
URL:            https://github.com/dfandrich/fvcbm
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  groff-base

%description
Fvcbm displays Commodore 64/128 archive, self-dissolving archive and disk image
directories. This can be especially useful in combination with a Commodore 64
emulator.

Supported archive formats are ARC230 (ARC), self-extracting ARC230 (SDA),
Lynx, CS-DOS (LZH), self-extracting CS-DOS (SFX), PC64 emulator files
(R/S/U/P00), LBR, 64Net files (N64), emulator tape images (T64 and TAP) and
disk images (D64 and X64).


%prep
%autosetup

# Fix Makefile
sed -i 's/$(CC) $(CFLAGS) -o/$(CC) $(CFLAGS) $(LDFLAGS) -o/' Makefile
sed -i 's/$(BINDIR)/$(DESTDIR)$(BINDIR)/' Makefile
sed -i 's/$(MANDIR)/$(DESTDIR)$(MANDIR)/' Makefile
sed -i 's/-o root -g bin//' Makefile
sed -i 's/-o root -g root//' Makefile



%build
%set_build_flags
%make_build linux


%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
%make_install PREFIX=%{_prefix}


%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Sat Dec 23 2023 Andrea Musuruane <musuruan@gmail.com> - 3.1-1
- First release
