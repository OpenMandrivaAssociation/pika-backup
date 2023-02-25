%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
Name:           pika-backup
Version:        0.4.2
Release:        0
Summary:        Simple backups based on borg
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/pika-backup
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
Patch0:         disable-update-desktop-database-and-gtk-update-icon-cache.patch
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  rust-packaging
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  itstool
Requires:       borgbackup
Requires:       python3-msgpack

%lang_package

%description
Doing backups the easy way. Plugin your USB drive and let the Pika do the rest for you.

%prep
%setup -qa1
mkdir .cargo
cp %{SOURCE2} .cargo/config
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/pika-backup
%{_bindir}/pika-backup-monitor
%config %{_sysconfdir}/xdg/autostart/org.gnome.World.PikaBackup.Monitor.desktop
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/dbus-1/services/*.service

%files lang -f %{name}.lang
