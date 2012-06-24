Summary:	SendIP is a commandline tool to allow sending arbitrary IP packets
Summary(pl):	Narz�dzie do wysy�ania dowolnych pakiet�w IP
Name:		sendip
Version:	2.5
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.earth.li/projectpurple/files/%{name}-%{version}.tar.gz
# Source0-md5:	35fa3306f39bfd46d83371da63eec3ad
URL:		http://www.earth.li/projectpurple/progs/sendip.html
Requires:	%{name}-libs = %{epoch}:%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SendIP is a command-line tool to send arbitrary IP packets. It has a
large number of options to specify the content of every header of a
RIP, RIPng, BGP, TCP, UDP, ICMP, or raw IPv4/IPv6 packet. It also
allows any data to be added to the packet. Checksums can be calculated
automatically, but if you wish to send out wrong checksums, that is
supported too.

%description -l pl
SendIP jest narz�dziem pozwalaj�cym wysy�a� dowolne pakiety IP. SendIP
posiada olbrzymi� liczb� opcji pozwalaj�cych opisa� zawarto�� ka�dego
pola nag�owka RIP, RIPng, BGP, TCP, UDP, ICMP, lub surowego pakietu
IPv4/IPv6. SendIP pozwala doda� do pakietu dowolne dane. Sumy
kontrolne s� obliczane automagicznie, ale je�eli sobie �yczysz mo�e
by� wys�ana b��dna suma kontrolna.

%package 	libs
Summary:	SendIP shared libraries
Summary(pl):	Biblioteki wsp�dzielone SendIP
Group:		Libraries

%description libs
SendIP shared libraries.

%description libs -l pl
Biblioteki wsp�dzielone SendIP.

%prep
%setup -q

%build
%{__make} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	 PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*

%files 	libs
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
