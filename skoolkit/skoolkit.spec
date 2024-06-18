Name:           skoolkit
Version:        9.2
Release:        1%{?dist}
Summary:        Tools for creating disassemblies of ZX Spectrum programs
License:        GPL-3.0-or-later
URL:            https://skoolkit.ca
Source0:        https://skoolkit.ca/downloads/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%{?python_enable_dependency_generator}

%description
SkoolKit is a collection of utilities that can be used to disassemble a
Spectrum game (or indeed any piece of Spectrum software written in machine
code) into a format known as a skool file. Then, from this skool file, you can
use SkoolKit to create a browsable disassembly in HTML format, or a
re-assemblable disassembly in ASM format. So the skool file is - from start to
finish as you develop it by organizing and annotating the code - the common
'source' for both the reader-friendly HTML version of the disassembly, and the
developer- and assembler-friendly ASM version of the disassembly.


%prep
%autosetup


%build
%py3_build


%install
%py3_install

# Install man pages
install -d %{buildroot}%{_mandir}/man1
install -m 644 -p man/man1/* %{buildroot}%{_mandir}/man1

# Install examples
install -d %{buildroot}%{_datadir}/%{name}
cp -a examples %{buildroot}%{_datadir}/%{name}


%files
%license COPYING
%doc docs/*
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_datadir}/%{name}/*
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}-*.egg-info


%changelog
* Mon Jun 17 2024 Andrea Musuruane <musuruan@gmail.com> - 9.2-1
- Updated to new upstream release

* Sat Mar 02 2024 Andrea Musuruane <musuruan@gmail.com> 9.1-1
- First release
