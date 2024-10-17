%define name searchmonkey
%define version 0.8.1
%define release %mkrel 1

Summary: Power searching without the pain
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: GPLv2.1
Group: File tools 
Url: https://searchmonkey.embeddediq.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
The Searchmonkey project aims to bring innovative and precise file searching to the world. To achieve this, Searchmonkey provides efficient and optimised software with an emphasis on achieving exact results.

searchmonkey is a GTK2 application designed to replace the find/grep command line tools.

The aim of this utility it to provide fast, slick text search ability to the GTK community.

%prep
%setup -q

%build
#configure2_5x
./configure
%make

%install
rm -rf %{buildroot}
%makeinstall

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=SearchMonkey
Comment=Power searching without the pain
Exec=searchmonkey
Icon=searchmonkey
Terminal=false
Type=Application
Categories=Utility;GTK;
EOF

%find_lang %{name}
%if %mdkversion < 201010
%post
%update_menus
%endif

%if %mdkversion < 201010
%postun
%clean_menus
%endif



%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc INSTALL NEWS README COPYING.LESSER AUTHORS
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}/readme-searchmonkey-icon.txt
%{_datadir}/pixmaps/%{name}/%{name}-*.png
%{_datadir}/applications/%{name}.desktop
