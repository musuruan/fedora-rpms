Name:           view64
Version:        1.60
Release:        2%{?dist}
Summary:        Viewer for Commodore C64 images

License:        GPLv2+
URL:            http://view64.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{version}/%{name}-%{version}-src.zip

BuildRequires:  gcc-c++
BuildRequires:  fltk-devel
BuildRequires:  desktop-file-utils


%description
View64 is a C64 image file viewer with built in PAL/NTSC rendering.

%prep
%autosetup -n %{name}-%{version}-src

# Fix Makefile
sed -i 's/= -O2 -Wall/+=/' Makefile
sed -i '/LDFLAGS = -g/d' Makefile
sed -i '/+= $(LDFLAGS)/d' Makefile
sed -i '/view64-fltk/{n;s/$(CXXFLAGS)/$(CXXFLAGS) $(LDFLAGS)/}' Makefile
sed -i '/view64pnm/{n;s/$(CFLAGS)/$(CFLAGS) $(LDFLAGS)/}' Makefile
sed -i 's!PREFIX = $(DESTDIR)/usr/local!PREFIX = $(DESTDIR)/usr!' Makefile

%build
%set_build_flags
%make_build all view64pnm


%install
%make_install

# Install config file
install -d %{buildroot}%{_sysconfdir}
install -p -m 644 view64.conf %{buildroot}%{_sysconfdir}

# Install mime file
install -d %{buildroot}%{_datadir}/mime/packages
install -p -m 644 %{name}.xml %{buildroot}%{_datadir}/mime/packages

# Install man pages
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 *.1 %{buildroot}%{_mandir}/man1/

# Install desktop file
# Icon is missing
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{name}.desktop


%files
%{_bindir}/%{name}
%{_bindir}/%{name}pnm
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}pnm.1*
%license LICENSE
%doc README README.html


%changelog
* Sat Dec 15 2018 Andrea Musuruane <musuruan@gmail.com> - 1.60-2
- Used %%set_build_flags macro

* Mon May 14 2018 Andrea Musuruane <musuruan@gmail.com> - 1.60-1
- First release
