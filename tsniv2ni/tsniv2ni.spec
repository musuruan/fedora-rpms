%global commit b26f07e9f0872806ae5acdb52c77f40029af0a09
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           tsniv2ni
Version:        0
Release:        0.1.20201122git%{?dist}
Summary:        Converts TS ETI V.11 streams to ETI NI G.703

License:        GPLv3+
URL:            https://github.com/newspaperman/tsniv2ni
Source0:        https://github.com/newspaperman/tsniv2ni/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# Fix building with GCC 11
# https://github.com/newspaperman/tsniv2ni/issues/5
Patch0:         %{name}-0-gcc11.patch

BuildRequires:  gcc-c++
BuildRequires:  make

%description
Converts TS ETI V.11 streams to ETI NI G.703


%prep
%autosetup -n %{name}-%{commit} -p1


%build
%set_build_flags
%make_build


%install
%make_install


%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md


%changelog
* Thu Sep 16 2021 Andrea Musuruane <musuruan@gmail.com> - 0-0.1.20201122git
- First release
