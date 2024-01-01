Name:           dMagnetic
Version:        0.37
Release:        1%{?dist}
Summary:        A Magnetic Scrolls Interpreter

License:        BSD
URL:            http://www.dettus.net/dMagnetic/
Source0:        http://www.dettus.net/dMagnetic/%{name}_%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make

%description
dMagnetic is a Magnetic Scrolls Interpreter. It allows to play classic text
adventures such as "The Pawn", "The Guild of Thieves", "Fish!", "Jinxter",
"Myth", "Corruption" and "Wonderland" in a terminal window. The beautiful
graphics are being rendered in glorious ANSI art.


%prep
%autosetup -n %{name}_%{version}

# Fix Makefile
sed -i 's!MYPREFIX=$(DESTDIR)!MYPREFIX=$(DESTDIR)$(PREFIX)!' Makefile
sed -i 's!/share/games!/share/!' Makefile
#sed -i 's!$(LINK) $(LDFLAGS) -o!$(LINK) $(LDFLAGS) -g -o!' Makefile
sed -i 's!install -m 755 -s dMagnetic!install -m 755 dMagnetic!' Makefile


%build
%set_build_flags
%make_build


%install
%make_install PREFIX=%{_prefix}
rm %{buildroot}%{_datadir}/%{name}/{README.txt,LICENSE.txt}


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man5/%{name}ini.5*
%{_mandir}/man6/%{name}.6*
%license LICENSE.txt
%doc README.txt


%changelog
* Fri Dec 01 2023 Andrea Musuruane <musuruan@gmail.com> - 0.37-1
- First release
