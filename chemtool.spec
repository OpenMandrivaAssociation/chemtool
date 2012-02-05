%define	name	chemtool
%define version 1.6.13
%define release 1

Summary:	Program for 2D drawing organic molecules
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sciences/Chemistry
Source0:	http://ruby.chemie.uni-freiburg.de/~martin/chemtool/%{name}-%{version}.tar.gz
Url:		http://ruby.chemie.uni-freiburg.de/~martin/chemtool/
Requires:	transfig openbabel
BuildRequires:	gtk2-devel gettext-devel desktop-file-utils
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

%build
%configure2_5x
%make

%install
%makeinstall_std

mkdir -p %buildroot%_datadir/%{name}-%{version}
install -m644 examples/* %buildroot%_datadir/%{name}-%{version}/

mkdir -p %buildroot%{_datadir}/applications

# (tv) fix 'error: value "chemtool.png" for key "Icon" in group "Desktop Entry"
# is an icon name with an extension, but there should be no extension as
# described in the Icon Theme Specification if the value is not an absolute
# path':
perl -pi -e 's!^(Icon=).*/([^/]*)$!\1\2!; s!.png$!!' %{name}.desktop

desktop-file-install --vendor='' \
	--dir=%buildroot%{_datadir}/applications/ \
	--remove-category='Application' \
	--add-category='GTK' \
	--add-category='Science' \
	%{name}.desktop

install -D -m644 kde/icons/hicolor/32x32/mimetypes/chemtool.png %buildroot%{_iconsdir}/hicolor/32x32/mimetypes/chemtool.png

# icons
%{__install} -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
%{__install} -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
%{__install} -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
%{__install} -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{__install} -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{__install} -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%{find_lang} %{name}

%files -f %{name}.lang
%doc TODO README ChangeLog
%_bindir/*
%_datadir/%{name}-%{version}
%_mandir/man1/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
