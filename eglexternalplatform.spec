Summary:	EGL External Platform Interface
Summary(pl.UTF-8):	Interfejs EGL External Platform
Name:		eglexternalplatform
# see interface/eglexternalplatformversion.h
Version:	1.0.0
%define	gitref	e3b182e3253f92bdbb03a71fdbd958bfb69cf3e3
%define	snap	20180316
Release:	0.%{snap}.1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://github.com/NVIDIA/eglexternalplatform/releases
# ...but no releases yet, so use snapshot
Source0:	https://github.com/NVIDIA/eglexternalplatform/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	fc3aa30a0351acbb790a2d2428369c28
URL:		https://github.com/NVIDIA/eglexternalplatform
BuildRequires:	rpmbuild(macros) >= 1.446
Requires:	EGL-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a work-in-progress specification of the EGL External Platform
interface for writing EGL platforms and their interactions with modern
window systems on top of existing low-level EGL platform
implementations. This keeps window system implementation specifics out
of EGL drivers by using application-facing EGL functions.

Examples of low-level EGL platforms are EGL_EXT_platform_device or
EGL_KHR_platform_gbm.

%description -l pl.UTF-8
Ten pakiet zawiera będącą w trakcie tworzenia specyfikację interfejsu
EGL External Platform (platform zewnętrznych EGL) do pisania platform
EGL oraz ich interakcji ze współczesnymi systemami okienkowymi,
opartymi na istniejących niskopoziomowych implementacjach platform
EGL. Dzięki temu specyfika implementacji systemu okien jest oddzielona
od sterowników EGL poprzez użycie aplikacyjnych funkcji EGL.

Przykładami niskopoziomowych platform EGL są EGL_EXT_platform_device
czy EGL_KHR_platform_gbm.

%prep
%setup -q -n %{name}-%{gitref}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/EGL,%{_npkgconfigdir}}

cp -p interface/*.h $RPM_BUILD_ROOT%{_includedir}/EGL
cp -p eglexternalplatform.pc $RPM_BUILD_ROOT%{_npkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_includedir}/EGL/eglexternalplatform.h
%attr(755,root,root) %{_includedir}/EGL/eglexternalplatformversion.h
%{_npkgconfigdir}/eglexternalplatform.pc
