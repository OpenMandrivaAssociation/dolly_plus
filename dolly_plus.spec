%define name dolly_plus
%define version 0.93
%define release 8

Summary: Clone the installation of one machine to many other machines
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: dolly_plus-Makefile.patch
Patch1: dolly_plus-Client.patch
Source2: dolly_plus.cfg
License: GPL
Group: System/Servers
Url: https://corvus.kek.jp/~manabe/pcf/dolly/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
In administrating a large scale PC cluster, installation and updating both
of kernel and utility software to whole the system are very troublesome, 
especially if the numbers of PC exceeds a hundred. In installation, people 
usually make dead copies of a hard disk image in which software systems are
previously installed and then they are distributed among node PCs by CDs or
hard disk themselves.
Though some software do such a process through networks, they commonly have 
an performance bottleneck at server where the original image are hold. 
A cloning program `dolly' developed in ETH(Swiss Federal Institute of 
Technology) avoids such bottleneck by using a "ring" type connection rather 
than 'hub' type connection among one server and many clients.
I have extended its concept with multi-threading and pipeline technique.
It speeds up installation process very much. One-to-ten copying, for example,
finishes in almost same minutes for one-to-one copy. 
In addition, time out sensing 'bypass' mechanism makes the copy process
pretty robust in the case of a client machine trouble.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}
install -m755 $RPM_BUILD_DIR/%name-%version/dollyS %{buildroot}/%{_bindir}/dollyS
install -m755 $RPM_BUILD_DIR/%name-%version/dollyC %{buildroot}/%{_bindir}/dollyC
install -m755 $RPM_BUILD_DIR/%name-%version/dping %{buildroot}/%{_bindir}/dping
install -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/dolly_plus.cfg.sample

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc index.html
%config %{_sysconfdir}/dolly_plus.cfg.sample
%{_bindir}/dollyS
%{_bindir}/dollyC
%{_bindir}/dping




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.93-7mdv2011.0
+ Revision: 610267
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.93-6mdv2009.0
+ Revision: 244452
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.93-4mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 02 2007 Antoine Ginies <aginies@mandriva.com> 0.93-4mdv2007.0
+ Revision: 130967
- need to increment the release to build it on cooker
- Import dolly_plus

* Thu Apr 06 2006 Antoine Ginies <aginies@mandriva.com> 0.93-2mdk
- add default configuration file
- use mkrel

* Thu Nov 17 2005 Antoine Ginies <aginies@mandriva.com> 0.93-1mdk
- first mdk release

