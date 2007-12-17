
%define name	vdrsync
%define version	0.1.2.2dev2
%define snapshot 050322
%define rel	2
%define release %snapshot.%rel

Summary:	Repack VDR recordings to DVD compatible fromat
Name:		%name
Version:	%version
Release:	%mkrel %release
Group:		Video
License:	GPL
URL:		http://vdrsync.vdr-portal.de/
Source:		http://vdrsync.vdr-portal.de/releases/%name-%snapshot.tar.bz2
BuildArch:	noarch

%description
VDRsync was programmed to allow conversion of a VDR recording into a
DVD compatible format. This conversion requires the "unpacking" of
Video and Audio data from the native VDR format, and the repacking
into a DVD compatible format. During this packing steps important
timing information is lost, leading to Audio-Video synchronisation
problems. In other words, audio is a bit too early or too late for
the video. Watching such a "desynced" movie is a pain.

Not too long ago an excellent tool named ds.jar was available, which
took care of the problem by aligning Audio and Video during the
first "unpacking" step. This tool was unavailable for a certain
period and therefore I decided to try to write a replacement for it
(ds.jar is now available again under the name Project X).

In the meantime I added some features to VDRsync, like cutting the
movie while syncing, and developed some additional tools, like the
sharemarks project.

%prep
%setup -q -n %name-%snapshot

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_bindir}
install -m755 *.pl %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES
%{_bindir}/*.pl

