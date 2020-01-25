# TODO
# - use rhino from PLD package
# - do not embed jargs into yuicompressor.jar
#
# Conditional build:
%bcond_without	tests		# don't build and run tests

Summary:	YUI Compressor - JavaScript compressor
Summary(pl.UTF-8):	Narzędzie do kompresji kodu JavaScript
Name:		yuicompressor
Version:	2.4.8
Release:	1
License:	BSD
Group:		Applications/WWW
# Source0Download: https://github.com/yui/yuicompressor/releases
Source0:	https://github.com/yui/yuicompressor/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a5a0b0d3c99e0a52e24a1da1560560eb
Source1:	%{name}.sh
URL:		http://yui.github.io/yuicompressor/
BuildRequires:	ant
BuildRequires:	java-jargs
BuildRequires:	jdk >= 1.4
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
%if %{with tests}
BuildRequires:	bash
%endif
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The YUI Compressor is a JavaScript/CSS minifier.

Its level of compaction is higher than the Dojo compressor, and it is
as safe as JSMin.

Tests on the YUI library have shown savings of about 18% compared to
JSMin and 10% compared to the Dojo compressor (these respectively
become 10% and 5% after HTTP compression)

%description -l pl.UTF-8
YUI Compressor jest narzędziem do kompresji kodu JavaScript.

Poziom kompresji osiągany przez YUI Compressor jest większy niż w
przypadku Dojo compressor przy czym jest nie mniej bezpieczny niż
JSMin.

Testy wykonane na bibliotece YUI wykazały, że 18% zysk względem JSMin
i 10% zysk względem Dojo Compressor (odpowiednio 10% i 5% po kompresji
HTTP).

%prep
%setup -q

rm -rf build
# Do not remove lib/rhino-1.6R7.jar It does not work with our java-rhino-1.7
rm lib/jargs-1.0.jar

chmod a+x tests/suite.sh

%build
JARGS_JAR=$(find-jar jargs)
ln -sf $JARGS_JAR lib/jargs-1.0.jar

required_jars='jargs'
CLASSPATH=$(build-classpath $required_jars)
%ant -Dbuild.sysclasspath=first

%if %{with tests}
./tests/suite.sh
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -p build/yuicompressor-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.TXT doc/*
%attr(755,root,root) %{_bindir}/%{name}
%{_javadir}/*.jar
