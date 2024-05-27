%global commit 0a18da3c913c6e50b82b00eb634e63f3b498c632
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           eti-tools
Version:        0
Release:        0.2.20210830git%{?dist}
Summary:        ETI conversion software

License:        MPLv2.0
URL:            https://github.com/piratfm/eti-tools
Source0:        https://github.com/piratfm/eti-tools/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  gcc-g++
BuildRequires:  make
#BuildRequires:  cmake
#BuildRequires:  libfec-devel
BuildRequires:  libshout-devel
#BuildRequires:  zeromq3-devel

%description
The main purpose of these apps is to convert/manipulate ETI-NA/ETI-NI streams
(by using pipelines).

With these software tools you can create your own IceCast2 internet-radio
server which will use your local DAB/DAB+ transmitter as source for the
stations streams. You also can re-multiplex some (needed) stations from one
ETI-stream to another by using ZeroMQ feature of the ni2http application and
ODR-DabMUX.

This software also allows to receive and convert special formatted Satellite
DAB(+) streams (so-called feeds) into regular ETI-NI which then can be used
to play in dablin or even feed modulator software/hardware (check local laws!)
or to create internet-station from that source.


%prep
%autosetup -n %{name}-%{commit}

# Clean up
rm libshout-2.2.2.tar.gz

# Patch Makefile
sed -i 's|CFLAGS =-O2 -Wall|CFLAGS += -O2 -Wall|' Makefile
sed -i 's|-Ilibshout-2.2.2/include|-I/usr/include/shout/|' Makefile
sed -i 's|libshout-2.2.2/src/.libs/libshout.a $(OBJS_NI2HTTP)|$(OBJS_NI2HTTP)|' Makefile
sed -i 's|libshout-2.2.2/src/.libs/libshout.a -lpthread|-lshout -lpthread|' Makefile


%build
%set_build_flags
%make_build


%install
%make_install


%files
%license LICENSE
%doc README.md
%{_bindir}/*


%changelog
* Sun Sep 12 2021 Andrea Musuruane <musuruan@gmail.com> - 0-0.2.20210830git
- Updated to latest upstream commit

* Thu Jan 04 2018 Andrea Musuruane <musuruan@gmail.com> - 0-0.1.20170801git
- First release
