Name:           mtkbabel
Version:        0.8.4
Release:        1%{?dist}
Summary:        Program to Operate the i-Blue 747 GPS Data Logger
License:        GPLv2+
Url:            https://sourceforge.net/projects/mtkbabel
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Requires:       perl(Device::SerialPort)
Requires:       perl(Date::Format)

BuildArch:      noarch

%description
MTKBabel is a Perl program to operate the i-Blue 747 GPS data logger.
It should work also with other GPS devices based on the MediaTek MTK
chipset. It is free software released under the GPL license.

The main capabilities are:

  * Command line interface
  * Save data log in GPX and raw binary format
  * If required retrieve all the data, also the old one being overlapped
  * Change logging criteria: time, distance, speed
  * Change log format
  * START/STOP logging
  * Set OVERLAP or STOP method on memory full
  * Erase the internal memory

The program is written in Perl, and it was tested on Linux via USB
connection. One goal is easy portability to C and small RAM footprint.


%prep
%autosetup


%build
# Nothing to do


%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 %{name} %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1/
install -p -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/


%files
%license copyright
%doc MtkExtensionsv1.xsd README changelog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Sun Jun 26 2022 Andrea Musuruane <musuruan@gmail.com> - 0.8.4-1
- bump to new upstream release 0.8.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr 13 2010 Daniel Rindt <drindt@visetics.com> 0.8.2-1
- bump to new upstream release 0.8.2

* Sat Mar 27 2010 Daniel Rindt <drindt@visetics.com> 0.8.1-1
- bump to new upstream release 0.8.1

* Fri Aug 3 2009 Daniel Rindt <drindt@visetics.com> 0.8-1
- Created new package, version 0.8.
