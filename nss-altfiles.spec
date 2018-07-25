Name:           nss-altfiles
Version:        2.23.0
Release:        1%{?dist}
License:        LGPL 2.1
Summary:        NSS module for reading user information from /usr/etc/ instead of /etc/

URL:            https://github.com/coreos/nss-altfiles
Source0:        https://github.com/coreos/nss-altfiles/archive/v2.23.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  autoconf automake gcc

%description
NSS module for reading user information from /usr/etc/ instead of /etc/

%prep
%setup -q


%build
%configure
make 


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/lib64/libnss_altfiles.so.2

