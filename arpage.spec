Name:		arpage
Version:	0.2
Release:	4%{?dist}
Summary:	A JACK MIDI arpeggiator

Group:		Applications/Multimedia
License:	GPLv3
URL:		http://arpage.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	gtkmm24-devel intltool
BuildRequires:	desktop-file-utils

# Until a custom icon is available
Requires:	echo-icon-theme

%description

A GTK application that runs up to 4 arpeggiators on incoming MIDI
data, synchronised to JACK.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} arpagedocdir=%{_defaultdocdir}/%{name}-%{version}

desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog
%{_bindir}/%{name}
%{_bindir}/zonage
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop

%changelog
* Sat May  1 2010 Adam Huffman <bloch@verdurin.com> - 0.2-4
- add .desktop file to files section
- add Echo icon theme to requires

* Sun Apr 11 2010  Adam Huffman <bloch@verdurin.com> - 0.2-3
- add desktop file
- specify icon

* Wed Apr  7 2010 Adam Huffman <bloch@verdurin.com> - 0.2-2
- fix directory ownership
- add desktop file infrastructure

* Sun Jan 31 2010 Adam Huffman <bloch@verdurin.com> - 0.2-1
- initial version
- Makefile variable set to move doc files to standard location
- delete empty doc files
