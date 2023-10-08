Name:           zmakebas
Version:        1.8.5
Release:        1%{?dist}
Summary:        Convert text files into Spectrum Basic programs

License:        Public Domain
URL:            https://github.com/chris-y/zmakebas
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc

%description
zmakebas converts a Spectrum Basic program written as a text file into an
actual speccy Basic file (as a .TAP file, or optionally a raw headerless file).


%prep
%autosetup

# Fix CFLAGS & LDFLAGS
sed -i 's/=-O -Wall -DHAVE_GETOPT/+=-DHAVE_GETOPT/' Makefile
sed -i 's/$(CC) $(CFLAGS)/$(CC) $(LDFLAGS)/' Makefile


%build
%set_build_flags
%make_build zmakebas


%install
# Install binary
install -d %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}

# Install man page
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/


%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%doc ABOUT README.md ChangeLog


%changelog
* Sun Oct 08 2023 Andrea Musuruane <musuruan@gmail.com> - 1.8.5-1
- Updated to new upstream release

* Sat Aug 22 2020 Andrea Musuruane <musuruan@gmail.com> - 1.6.1-1
- First release
