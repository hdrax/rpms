# $Id$
# Authority: dries

Summary: GNUstep base library package
Name: gnustep-base
Version: 1.9.1
Release: 1
License: GPL
Group: Development/Libraries
URL: http://www.gnustep.org/

Source: http://ftp.gnustep.org/pub/gnustep/core/gnustep-base-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: /usr/GNUstep/System/Library/Makefiles/GNUstep.sh, diffutils, openssl-devel, gcc-objc, ffcall, gnustep-make
Requires: ffcall

%description
The GNUstep Base Library is a library of general-purpose,
non-graphical Objective C objects.  For example, it includes classes
for strings, object collections, byte streams, typed coders,
invocations, notifications, notification dispatchers, moments in time,
network ports, remote object messaging support (distributed objects),
and event loops.

%prep
%setup

%build
source /usr/GNUstep/System/Library/Makefiles/GNUstep.sh
%configure \
	--prefix="%{_prefix}/GNUstep"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /usr/GNUstep/System/Library/Makefiles/GNUstep.sh
#%{__install} -d -m0755 %{buildroot}
%makeinstall \
	INSTALL_ROOT_DIR="%{buildroot}" \
	GNUSTEP_INSTALLATION_DIR="%{buildroot}%{_prefix}/GNUstep"
chmod -s-t %{buildroot}%{_prefix}/GNUstep/Tools/gdomap

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_prefix}/GNUstep/

%changelog
* Thu Jun 10 2004 Dag Wieers <dag@wieers.com> - 1.9.1-1
- Updated to release 1.9.1.
- Cosmetic cleanup.

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-4
- added some BuildRequires
- removed the setuid of gdomap

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-3
- cleanup of spec file

* Tue Nov 11 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-2
- fixed the make install

* Mon Nov 10 2003 Dries Verachtert <dries@ulyssis.org> 1.8.0-1
- first packaging for Fedora Core 1
