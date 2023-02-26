# workaround empty debug
%define _empty_manifest_terminate_build 0
Name:           pika-backup
Version:        0.5.2
Release:        1
Summary:        Simple backups based on borg
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/pika-backup
Source0:        https://gitlab.gnome.org/World/pika-backup/-/archive/v%{version}/pika-backup-v%{version}.tar.bz2
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  meson
BuildRequires:  git
BuildRequires:  pkgconfig
BuildRequires:  rust-packaging
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  itstool
Requires:       borgbackup
Requires:       python3dist(msgpack)

%description
Doing backups the easy way. Plugin your USB drive and let the Pika do the rest for you.

%prep
%autosetup -n %{name}-v%{version} -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config


%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%doc %{_datadir}/help/*
%{_bindir}/pika-backup
%{_bindir}/pika-backup-monitor
%config %{_sysconfdir}/xdg/autostart/org.gnome.World.PikaBackup.Monitor.desktop
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/dbus-1/services/*.service

