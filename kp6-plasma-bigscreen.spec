#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.7.2
%define		qtver		6.11.0
%define		kpname		plasma-bigscreen
%define		kfver		6.26.0

Summary:	plasma-bigscreen
Name:		kp6-%{kpname}
Version:	6.7.2
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	fcd500e168d514bb10540de62b647277
URL:		https://plasma-bigscreen.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Multimedia-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Qml-devel >= %{qtver}
BuildRequires:	Qt6Quick-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext
BuildRequires:	kf6-extra-cmake-modules >= %{kfver}
BuildRequires:	kf6-kauth-devel >= %{kfver}
BuildRequires:	kf6-kcmutils-devel >= %{kfver}
BuildRequires:	kf6-kcodecs-devel >= %{kfver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kfver}
BuildRequires:	kf6-kdeclarative-devel >= %{kfver}
BuildRequires:	kf6-ki18n-devel >= %{kfver}
BuildRequires:	kf6-kio-devel >= %{kfver}
BuildRequires:	kf6-kirigami-devel >= %{kfver}
BuildRequires:	kf6-kjobwidgets-devel >= %{kfver}
BuildRequires:	kf6-knotifications-devel >= %{kfver}
BuildRequires:	kf6-kpackage-devel >= %{kfver}
BuildRequires:	kf6-kservice-devel >= %{kfver}
BuildRequires:	kf6-kwindowsystem-devel >= %{kfver}
BuildRequires:	kf6-solid-devel >= %{kfver}
BuildRequires:	kp6-kwayland-devel >= %{kdeplasmaver}
BuildRequires:	kp6-plasma-activities-devel >= %{kdeplasmaver}
BuildRequires:	kp6-plasma-activities-stats-devel >= %{kdeplasmaver}
BuildRequires:	kp6-plasma-workspace-devel >= %{kdeplasmaver}
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
Obsoletes:	kp5-plasma-phone-components < 5.24.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
An open-source TV interface for Linux. Your TV, your way.

%description -l pl.UTF-8
Otwartoźródłowy interfejs TV dla Linuksa. Twoja telewizja, twój
sposób.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build
#sed -i -e 's|bin/env python3|bin/python3|' $RPM_BUILD_ROOT%{_bindir}/mycroft-skill-launcher.py

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plasma-bigscreen-common-env
%attr(755,root,root) %{_bindir}/plasma-bigscreen-envmanager
%attr(755,root,root) %{_bindir}/plasma-bigscreen-inputhandler
%attr(755,root,root) %{_bindir}/plasma-bigscreen-settings
%attr(755,root,root) %{_bindir}/plasma-bigscreen-swap-session
%attr(755,root,root) %{_bindir}/plasma-bigscreen-uvcviewer
%attr(755,root,root) %{_bindir}/plasma-bigscreen-wayland
%attr(755,root,root) %{_bindir}/plasma-bigscreen-webapp
%{_libdir}/qt6/plugins/kf6/kded/kded_plasma_bigscreen_start.so
%{_libdir}/qt6/plugins/plasma/applets/org.kde.bigscreen.homescreen.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mediacenter_audiodevice.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mediacenter_bigscreen_settings.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mediacenter_bluetooth.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mediacenter_display.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mediacenter_input.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mediacenter_kdeconnect.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mediacenter_wallpaper.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mediacenter_webapps.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mediacenter_wifi.so
%{_libdir}/qt6/qml/org/kde/bigscreen
%{_libdir}/udev/rules.d/40-uinput.rules
%{_desktopdir}/kcm_mediacenter_audiodevice.desktop
%{_desktopdir}/kcm_mediacenter_bigscreen_settings.desktop
%{_desktopdir}/kcm_mediacenter_bluetooth.desktop
%{_desktopdir}/kcm_mediacenter_display.desktop
%{_desktopdir}/kcm_mediacenter_input.desktop
%{_desktopdir}/kcm_mediacenter_kdeconnect.desktop
%{_desktopdir}/kcm_mediacenter_wallpaper.desktop
%{_desktopdir}/kcm_mediacenter_webapps.desktop
%{_desktopdir}/kcm_mediacenter_wifi.desktop
%{_desktopdir}/org.kde.plasma.bigscreen.inputhandler.desktop
%{_desktopdir}/org.kde.plasma.bigscreen.uvcviewer.desktop
%{_desktopdir}/plasma-bigscreen-swap-session.desktop
%{_datadir}/dbus-1/interfaces/org.kde.biglauncher.xml
%{_datadir}/metainfo/org.kde.bigscreen.homescreen.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.bigscreen.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.bigscreen.metainfo.xml
%{_datadir}/plasma/look-and-feel/org.kde.plasma.bigscreen
%{_datadir}/plasma/plasmoids/org.kde.bigscreen.homescreen
%{_datadir}/plasma/shells/org.kde.plasma.bigscreen
%{_datadir}/sounds/plasma-bigscreen
%{_datadir}/wayland-sessions/plasma-bigscreen-wayland.desktop
