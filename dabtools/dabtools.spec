%global commit 8b0b2258b02020d314efd4d0d33a56c8097de0d1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           dabtools
Version:        0
Release:        0.1.20180405git8b0b225%{?dist}
Summary:        DAB/DAB+ software for RTL-SDR dongles and the Psion Wavefinder
License:        GPLv3+
URL:            https://github.com/Opendigitalradio/dabtools
Source0:        %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  rtl-sdr-devel
BuildRequires:  fftw-devel

%description
dabtools is a set of tools for reception, recording and playback of DAB and 
DAB+ digital radio broadcasts. It currently supports the Psion Wavefinder 
USB DAB tuner and any SDR tuner supported by the RTL-SDR project.

dabtools currently consists of the following tools:

dab2eti - receive a DAB ensemble and output an ETI stream to STDOUT
eti2mpa - extract an MPEG audio stream from an ETI stream.

ETI is the standard file format for the storage and transport of a DAB 
ensemble. It is defined in ETSI 300 799.


%prep
%autosetup -n %{name}-%{commit}


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%{_bindir}/dab2eti
%{_bindir}/eti2mpa
%license COPYING
%doc README.md TODO.md


%changelog
* Wed Aug 16 2023 Andrea Musuruane <musuruan@gmail.com> - 0-0.1.20180405git8b0b225
- First release
