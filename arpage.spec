Name:		arpage
Version:	0.2
Release:	1%{?dist}
Summary:	A JACK MIDI arpeggiator

Group:		Applications/Multimedia
License:	GPLv3
URL:		http://arpage.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	gtkmm24-devel
BuildRequires:	intltool

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


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog
%{_bindir}/%{name}
%{_bindir}/zonage
%{_datadir}/%{name}/ui/*.ui


%changelog
* Sun Jan 31 2010 Adam Huffman <bloch@verdurin.com> - 0.2-1
- initial version
- Makefile variable set to move doc files to standard location
- delete empty doc files
