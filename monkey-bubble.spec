Summary:	Monkey Bubble - the gnome bust'a'move clone
Summary(pl):	Monkey Bubble - klon gry bust'a'move dla GNOME
Name:		monkey-bubble
Version:	0.3.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://home.gna.org/monkeybubble/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	37e91fa4cdbab9ec06b2ee2a5aa0683c
Patch0:		%{name}-gcc34.patch
URL:		http://home.gna.org/monkeybubble/
BuildRequires:	GConf2-devel
BuildRequires:	gcc-c++
BuildRequires:	gstreamer-GConf-devel >= 0.8.1
BuildRequires:	librsvg-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	scrollkeeper
Requires(post):	GConf2
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monkey Bubble - the gnome bust'a'move clone.

%description -l pl
Monkey Bubble - klon gry bust'a'move dla GNOME.

%prep
%setup -q
%patch0 -p1

%build
%configure
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
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}
