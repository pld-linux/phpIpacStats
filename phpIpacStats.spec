Summary:	Web interface to ipac-ng statistics
Summary(pl):	Interfejs WWW do statystyk ipac-ng
Name:		phpIpacStats
Version:	0.4.1
Release:	1
License:	LGPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/phpipacstats/%{name}-%{version}.tar.bz2
Patch0:		%{name}-conf.patch
URL:		http://phpipacstats.sourceforge.net/
Requires:	webserver
Requires:	php
Requires:	ipac-ng
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web interface to ipac-ng statistics.

%description -l pl
Interfejs WWW do statystyk ipac-ng.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/httpd/html/services/pic

install *.php $RPM_BUILD_ROOT/home/httpd/html/services/pic
cp -a data includes templates $RPM_BUILD_ROOT/home/httpd/html/services/pic

%clean
rm -rf $RPM_BUILD_ROOT

%post
chgrp http /etc/ipac-ng/ipac.conf && chmod g+r /etc/ipac-ng/ipac.conf > /dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc TODO doc/*.html *.diff
%dir /home/httpd/html/services/pic
/home/httpd/html/services/pic/*.php
/home/httpd/html/services/pic/includes
/home/httpd/html/services/pic/templates
%attr(775,root,http) /home/httpd/html/services/pic/data
