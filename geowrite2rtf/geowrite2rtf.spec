%global commit e4cebb2bc6f978e48d2819248c39adec002c43d8 
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           geowrite2rtf
Version:        0
Release:        2.20150202git.e4cebb2%{?dist}
Summary:        Convert C64/C128 GEOS GeoWrite documents to RTF format

License:        BSD
URL:            https://github.com/mist64/geowrite2rtf
Source0:        https://github.com/mist64/geowrite2rtf/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
geowrite2rtf is a simple tool that converts a C64/C128 GEOS GeoWrite document
in .CVT format into RTF format. 

The tool can optionally write HTML or plain-text as well, though at a loss of
some or all formatting.

Use a tool like c1541 to extract the file from a D64/D71/D81/etc. disk image
into a .CVT first.


%prep
%autosetup -n %{name}-%{commit}

# Fix Makefile
sed -i 's/cc -o $@ $</cc $(CFLAGS) $(LDFLAGS) -o $@ $</' Makefile


%build
%set_build_flags
%make_build


%install
install -d %{buildroot}%{_bindir}
install -pm 0755 %{name} %{buildroot}%{_bindir}


%files
%{_bindir}/%{name}
%doc README.md


%changelog
* Sun Dec 24 2023 Andrea Musuruane <musuruan@gmail.com> - 0-2.20150202git.e4cebb2
- Modernized spec file

* Fri May 11 2018 Andrea Musuruane <musuruan@gmail.com> - 0-1.20150202git.e4cebb2
- First release
