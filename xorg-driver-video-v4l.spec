Summary:	X.org video driver for video4linux cards
Summary(pl.UTF-8):   Sterownik obrazu X.org dla kart video4linux
Name:		xorg-driver-video-v4l
Version:	0.1.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-v4l-%{version}.tar.bz2
# Source0-md5:	69339c38eba2cebc357d67e7a755d734
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
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

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/v4l_drv.so
%{_mandir}/man4/v4l.4*
