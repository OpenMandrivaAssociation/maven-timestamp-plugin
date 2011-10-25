Name:           maven-timestamp-plugin
Version:        1.0
Release:        6
Summary:        Provides formatted timestamps for maven builds

Group:          Development/Java
License:        ASL 2.0
URL:            http://code.google.com/p/maven-timestamp-plugin
### upstream only provides binaries or source without build scripts
# tar creation instructions
# svn export http://maven-timestamp-plugin.googlecode.com/svn/tags/maven-timestamp-plugin-1.0 maven-timestamp-plugin
# tar cf maven-timestamp-plugin-1.0.tar maven-timestamp-plugin 
# xz maven-timestamp-plugin-1.0.tar
Source0:        maven-timestamp-plugin-1.0.tar.xz
# remove previous timestamp plugin version from build
Patch0:         001_build_without_timestamps.patch
BuildArch:      noarch

BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4

Requires:       java 
Requires:       jpackage-utils

Requires(post):   jpackage-utils
Requires(postun): jpackage-utils

%description
There are a few ways to get a timestamp in your maven build. Unfortunately 
most of them make you jump through giant hoops. This maven plugin makes it 
as simple as 1-2-3 to create a timestamp at your disposal.
Also, it enables you to use the syntax of SimpleDateFormat to form custom 
formatted dates. 


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}
%patch0 -p 1
cat > README << EOT
%{name}-%{version}

%{description}
EOT


%build
mvn-local install javadoc:javadoc


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_javadir}

# jar
install -Dp -m 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 pom.xml  \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

%add_to_maven_depmap com.keyboardsamurais.maven %{name} %{version} JPP %{name}


%files
%defattr(-,root,root,-)
%doc README
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}

%post
%update_maven_depmap

%postun
%update_maven_depmap

