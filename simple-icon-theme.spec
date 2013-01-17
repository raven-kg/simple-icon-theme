%global icons_name Simple
%define _iconsdir %{_datadir}/icons

Name: simple-icon-theme
Version: 2.1
Release: 1%{?dist}

Summary: Additonal sets of icons for the GNOME, LXDE and Xfce
License: GPL
URL: http://www.gnome-look.org/content/show.php/Simple?content=99470

Group: Graphical desktop/GNOME
Source0: Simple-%{version}.tar.bz2
Source1: actions-%{version}.tar.bz2
BuildArch: noarch

%description
Sets of icons for GTK desktop environments based on original icons - OxygenRefit2

%prep
# %setup -q -n simple-icon-theme-%{version}-%{release}

%install
install -m755 -d %{buildroot}%{_iconsdir}
tar xjf %SOURCE0 -C %{buildroot}%{_iconsdir}/
tar xjf %SOURCE1 -C %{buildroot}%{_iconsdir}/
mv -f %{buildroot}%{_iconsdir}/actions-%{version}/* %{buildroot}%{_iconsdir}/%{icons_name}-%{version}/scalable/actions/
rm -rf %{buildroot}%{_iconsdir}/actions-%{version}
mv %{buildroot}%{_iconsdir}/%{icons_name}-%{version} %{buildroot}%{_iconsdir}/%{icons_name}
ln -s %{_iconsdir}/%{icons_name}/scalable/apps/clock.png %{buildroot}%{_iconsdir}/%{icons_name}/scalable/apps/xfce4-clock.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
for dir in /usr/share/icons/*; do
  if test -d "$dir"; then
    if test -f "$dir/index.theme"; then
      /usr/bin/gtk-update-icon-cache --quiet "$dir" || :
    fi
  fi
done

%files
%{_iconsdir}/%{icons_name}

%changelog
* Tue Dec 18 2012 Raven <raven_kg@megaline.kg> 2.1-1
- First build for SL


