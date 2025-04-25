Summary:	EGL External Platform Interface
Summary(pl.UTF-8):	Interfejs EGL External Platform
Name:		eglexternalplatform
Version:	1.2.1
Release:	1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://github.com/NVIDIA/eglexternalplatform/releases
Source0:	https://github.com/NVIDIA/eglexternalplatform/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a255995b7926ee185310239e7cac1a1c
URL:		https://github.com/NVIDIA/eglexternalplatform
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 2.042
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
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_includedir}/eglexternalplatform.h
%attr(755,root,root) %{_includedir}/eglexternalplatformversion.h
%{_npkgconfigdir}/eglexternalplatform.pc
