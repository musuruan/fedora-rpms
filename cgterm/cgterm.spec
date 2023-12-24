Name:           cgterm
Version:        1.6
Release:        1%{?dist}
Summary:        C/G telnet client that lets you connect to C64 telnet BBS

License:        BSD
URL:            https://paradroid.automac.se/cgterm/
Source0:        http://paradroid.automac.se/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  SDL-devel

%description
CGTerm is a C/G telnet client that let you connect to C64 telnet BBSes with
the correct colors and the correct font. Also included is a client for 64CHAT
called CGChat. 


%prep
%autosetup

# Fix end-of-line encoding
sed -i 's/\r//' *.txt

# Fix Makefile
sed -i 's/CFLAGS=-O3 -Wall/CFLAGS+=/' Makefile
sed -i 's/LDFLAGS=/LDFLAGS+=/' Makefile
sed -i 's!PREFIX=/usr/local!PREFIX=/usr!' Makefile


%build
%set_build_flags
%make_build


%install
mkdir -p %{buildroot}%{_prefix}
%make_install PREFIX=%{buildroot}%{_prefix}
rmdir %{buildroot}%{_prefix}%{_sysconfdir}


%files
%{_bindir}/%{name}
%{_bindir}/cgchat
%{_datadir}/%{name}
%doc cgchat.txt cgterm.txt history.txt 


%changelog
* Thu Mar 28 2019 Andrea Musuruane <musuruan@gmail.com> - 1.6-1
- First release
 
