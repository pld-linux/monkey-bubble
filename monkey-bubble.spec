Summary:	Monkey Bubble - the gnome bust'a'move clone
Summary(pl.UTF-8):	Monkey Bubble - klon gry bust'a'move dla GNOME
Name:		monkey-bubble
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://home.gna.org/monkeybubble/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	0de8a05c8c15e08326d244534dc30f22
Patch0:	%{name}-build-fix.patch
URL:		http://home.gna.org/monkeybubble/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gstreamer-devel >= 0.10.0
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	intltool
BuildRequires:	librsvg-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	scrollkeeper
Requires(post):	GConf2
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monkey Bubble - the gnome bust'a'move clone.

%description -l pl.UTF-8
Monkey Bubble - klon gry bust'a'move dla GNOME.

%prep
%setup -q
%patch -P0 -p1

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
  --disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}
