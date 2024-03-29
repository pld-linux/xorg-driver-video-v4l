Summary:	X.org video driver for video4linux cards
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart video4linux
Name:		xorg-driver-video-v4l
Version:	0.3.0
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-v4l-%{version}.tar.bz2
# Source0-md5:	167b82a486859dafd076ec0ab12d7d40
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.0.99.901
Provides:	xorg-driver-video
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for video4linux cards. It provides a Xvideo
extension port for video overlay. This driver works with every piece
of hardware which is supported by a video4linux (kernel-) device
driver and is able to handle video overlay. bt848/bt878-based TV cards
are the most popular hardware these days.

%description -l pl.UTF-8
Sterownik obrazu X.org dla kart video4linux. Udostępnia port
rozszerzenia Xvideo dla nakładki obrazu. Działa z każdym kawałkiem
sprzętu obsługiwanym przez sterownik jądra video4linux, potrafiącym
obsłużyć nakładkę obrazu. Najpopularniejsze z nich to karty
telewizyjne bt848/bt878.

%prep
%setup -q -n xf86-video-v4l-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/v4l_drv.so
%{_mandir}/man4/v4l.4*
