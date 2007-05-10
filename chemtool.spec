%define	name	chemtool
%define version 1.6.10
%define release %mkrel 1

Summary:	Chemtool is a program for 2D drawing organic molecules
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sciences/Chemistry
Source0:	http://ruby.chemie.uni-freiburg.de/~martin/chemtool/%{name}-%{version}.tar.bz2
Url:		http://ruby.chemie.uni-freiburg.de/~martin/chemtool/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	transfig openbabel
BuildRequires:	gtk2-devel
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
Patch0:		chemtool-1.6.8-compilationfix.patch

%description
Chemtool is a program for drawing organic molecules easily and store them as
a X bitmap, Xfig or EPS file. It runs under the X Window System using 
the GTK widget set.

%prep
%setup -q
%patch0 -p1 

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_datadir}/%name-%version/examples
for L in `ls locales`; do \
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$L/LC_MESSAGES; done

install -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m755 src-cht/cht -D $RPM_BUILD_ROOT%{_bindir}/cht
install -m644 examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/examples
install -m644 {%{name}.1,cht.1} $RPM_BUILD_ROOT%{_mandir}/man1/
for L in `ls locales`; do \
	install -m644 locales/$L/chemtool.mo \
	$RPM_BUILD_ROOT%{_datadir}/locale/$L/LC_MESSAGES; done

# menu entry
install -d $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}):\
command="%{_bindir}/chemtool"\
title="Chemtool"\
longtitle="A program for drawing organic molecules"\
needs="x11"\
icon="chemtool.png"\
section="More Applications/Sciences/Chemistry" \
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Chemtool
Comment=A program for drawing organic molecules
Exec=%{_bindir}/%{name} 
Icon=chemtool
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Sciences-Chemistry;Science;Chemistry;
EOF


# icons
%{__install} -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
%{__install} -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
%{__install} -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %{name}.lang
%defattr(-,root,root)
%doc TODO README ChangeLog
%_bindir/*
%_datadir/%{name}-%{version}
%_mandir/man1/*
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


