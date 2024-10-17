%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-timestamp-plugin
Version:        1.1
Release:        9.1%{?dist}
Summary:        Provides formatted timestamps for maven builds
License:        ASL 2.0
URL:            https://code.google.com/p/maven-timestamp-plugin
### upstream only provides binaries or source without build scripts
# tar creation instructions
# svn export http://maven-timestamp-plugin.googlecode.com/svn/tags/maven-timestamp-plugin-1.1 maven-timestamp-plugin
# tar caf maven-timestamp-plugin-1.1.tar.xz maven-timestamp-plugin 
Source0:        maven-timestamp-plugin-1.1.tar.xz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven:maven-project)

%description
There are a few ways to get a timestamp in your maven build. Unfortunately 
most of them make you jump through giant hoops. This maven plugin makes it 
as simple as 1-2-3 to create a timestamp at your disposal.
Also, it enables you to use the syntax of SimpleDateFormat to form custom 
formatted dates. 

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc readme.txt
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-8
- Update to current packaging guidelines

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Nov 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-5
- Install license file
- Resolves: rhbz#875044

* Mon Oct 15 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-4
- Remove unneeded BR: maven-timestamp-plugin

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 5 2011 Alexander Kurtakov <akurtako@redhat.com> 1.1-1
- Update to new upstream release (1.1).
- Fix FTBFS.
- Adapt to current guidelines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 05 2011 Guido Grazioli <guido.grazioli@gmail.com> - 1.0-5
- Build with maven 3
- Updated patch: use maven-release-plugin
- Updated patch: remove maven-source-plugin double declaration

* Mon Dec 13 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-4
- Adapt to current guidelines.

* Fri Apr 30 2010 Guido Grazioli <guido.grazioli@gmail.com> - 1.0-3
- Fix javadoc subpackage Requires

* Sat Apr 24 2010 Guido Grazioli <guido.grazioli@gmail.com> - 1.0-2
- Sanitize %%files section

* Sat Apr 10 2010 Guido Grazioli <guido.grazioli@gmail.com> - 1.0-1
- Initial packaging
