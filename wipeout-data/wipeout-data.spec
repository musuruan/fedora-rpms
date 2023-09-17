# DO NOT DISTRIBUTE PACKAGED RPMS FROM THIS SPEC FILE!

Name:           wipeout-data
Version:        0.1 
Release:        1%{?dist}
Summary:        Data files for Wipeout

License:        Commercial
URL:            https://phoboslab.org/log/2023/08/rewriting-wipeout
Source0:        https://phoboslab.org/files/wipeout-data-v01.zip

BuildArch:      noarch

%description
Wipeout is a racing game that is set in 2052, where players compete in the
F3600 anti-gravity racing league.

This package contains the data file for Wipeout.


%prep
%autosetup -n wipeout


%build
# Nothing to do


%install
# Install data
install -d %{buildroot}%{_datadir}/wipeout
cp -pr * %{buildroot}%{_datadir}/wipeout


%files
%{_datadir}/wipeout


%changelog
* Sun Sep 17 2023 Andrea Musuruane <musuruan@gmail.com> - 0.1-1
- First release
