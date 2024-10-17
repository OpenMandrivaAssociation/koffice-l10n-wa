Name: koffice-l10n-wa
Version: 2.3.2
Release: %mkrel 2
Summary: Language files for KOffice Walloon
Group: System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
URL: https://www.koffice.org
BuildArch: noarch
Source: ftp://ftp.kde.org/pub/kde/stable/koffice-%version/src/koffice-l10n/%name-%version.tar.bz2
BuildRequires: gettext >= 0.15
BuildRequires: kdelibs4-devel
Requires: locales-wa
Requires: koffice-core
Provides: koffice-l10n

%description 
Provides Walloon translations for KOffice.

%files 
%defattr(-,root,root,-)
%{_kde_datadir}/*/*/*

#------------------------------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot


%changelog
* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 2.3.2-2mdv2011.0
+ Revision: 639873
- rebuild

* Fri Feb 18 2011 Funda Wang <fwang@mandriva.org> 2.3.2-1
+ Revision: 638330
- New version 2.3.2

* Thu Jan 20 2011 Funda Wang <fwang@mandriva.org> 2.3.1-1
+ Revision: 631766
- New version 2.3.1

* Sat Aug 28 2010 Funda Wang <fwang@mandriva.org> 2.2.2-1mdv2011.0
+ Revision: 573643
- new version 2.2.2

* Sun Jul 11 2010 Funda Wang <fwang@mandriva.org> 2.2.1-1mdv2011.0
+ Revision: 550708
- new version 2.2.1

* Thu Jan 14 2010 Funda Wang <fwang@mandriva.org> 2.1.1-1mdv2010.1
+ Revision: 491275
- new version 2.1.1

* Tue Nov 24 2009 Funda Wang <fwang@mandriva.org> 2.1.0-1mdv2010.1
+ Revision: 469534
- new version 2.1.0

* Fri Nov 13 2009 Funda Wang <fwang@mandriva.org> 2.0.91-1mdv2010.1
+ Revision: 465563
- new version 2.0.91

* Thu Sep 17 2009 Funda Wang <fwang@mandriva.org> 2.0.82-1mdv2010.0
+ Revision: 443745
- new version 2.0.82

* Thu Aug 13 2009 Funda Wang <fwang@mandriva.org> 2.0.2-1mdv2010.0
+ Revision: 415835
- new version 2.0.2

* Sat Jun 27 2009 Funda Wang <fwang@mandriva.org> 2.0.1-1mdv2010.0
+ Revision: 389663
- new version 2.0.1

* Thu May 28 2009 Funda Wang <fwang@mandriva.org> 2.0.0-1mdv2010.0
+ Revision: 380405
- import koffice-l10n-wa


