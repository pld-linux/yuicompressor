# TODO
# - build from source
%include	/usr/lib/rpm/macros.java
Summary:	YUI Compressor - JavaScript compressor
Name:		yuicompressor
Version:	2.4.1
Release:	0.1
License:	BSD
Group:		Applications/WWW
Source0:	http://www.julienlecomte.net/yuicompressor/%{name}-%{version}.zip
# Source0-md5:	2dc5f70ad905f5bd1f3d6c1b78d1c0f0
URL:		http://www.julienlecomte.net/yuicompressor/
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Requires:	jre >= 1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The YUI Compressor is a JavaScript minifier.

Its level of compaction is higher than the Dojo compressor, and it is
as safe as JSMin.

Tests on the YUI library have shown savings of about 18% compared to
JSMin and 10% compared to the Dojo compressor (these respectively
become 10% and 5% after HTTP compression)

%prep
%setup -q

cat <<'EOF' >> %{name}
#!/bin/sh
exec java -jar %{_javadir}/%{name}.jar ${1:+"$@"}
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}
install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

# jars
cp -a build/yuicompressor-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/%{name}
%{_javadir}/*.jar
