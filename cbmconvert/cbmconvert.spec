Name:           cbmconvert
Version:        2.1.6
Release:        1%{?dist}
Summary:        Create, extract and convert 8-bit Commodore binary archives

License:        GPLv2+
URL:            https://github.com/dr-m/cbmconvert
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc-g++
BuildRequires:  cmake

%description
cbmconvert extracts files from most known archive file formats that are used
on 8-bit Commodore computer platforms and writes them to several different
formats, including some formats used by some emulators.

%prep
%autosetup -n %{name}-%{name}-%{version}


%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%{_bindir}/cbmconvert
%{_bindir}/disk2zip
%{_bindir}/zip2disk
%{_mandir}/man1/cbmconvert.1*
%{_mandir}/man1/disk2zip.1*
%{_mandir}/man1/zip2disk.1*
%license COPYING
%doc README.md TODO.md cbmconvert.html


%changelog
* Mon Sep 16 2024 Andrea Musuruane <musuruan@gmail.com> - 2.1.6-1
- Update to new upstream realese

* Thu Dec 21 2023 Andrea Musuruane <musuruan@gmail.com> - 2.1.5-1
- Update to new upstream realese

* Thu Feb 17 2022 Andrea Musuruane <musuruan@gmail.com> - 2.1.4-1
- Update to new upstream realese

* Sun Apr 29 2018 Andrea Musuruane <musuruan@gmail.com> - 2.1.3-1
- First release
