Name:           tapclean
Version:        0.38
Release:        1%{?dist}
Summary:        Commodore tape preservation and restoration tool

License:        GPLv2
URL:            https://sourceforge.net/projects/tapclean
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tgz

BuildRequires:  gcc


%description
TAPClean is a Commodore tape preservation / restoration tool. It will check,
repair, and remaster Commodore 64 and VIC 20 TAP or DC2N DMP files (tape
images).


%prep
%autosetup -n %{name}
# Fix Makefile
sed -i 's/CFLAGS = $(INCS)/CFLAGS += $(INCS)/' src/Makefile
sed -i 's/$(CC)/$(CC) $(LDFLAGS)/' src/Makefile


%build
%set_build_flags
%make_build -C src


%install
# Install binary
install -d %{buildroot}%{_bindir}
install -p -m 0755 src/%{name} %{buildroot}%{_bindir}


%files
%{_bindir}/%{name}
%license docs/license.md
%doc docs/history_of_changes.md


%changelog
* Thu Feb 17 2022 Andrea Musuruane <musuruan@gmail.com> - 0.38-1
- Update to new upstream realese

* Sat Dec 15 2018 Andrea Musuruane <musuruan@gmail.com> - 0.37-1
- First release
 
