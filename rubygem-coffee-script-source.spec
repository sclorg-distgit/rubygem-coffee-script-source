%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

#Generated from coffee-script-source-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name coffee-script-source

%global coffee_script_version 1.10.0
%global coffee_script_require js-coffee-script = %{coffee_script_version}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: %{coffee_script_version}
Release: 3%{?dist}
Summary: The CoffeeScript Compiler
Group: Development/Languages
License: MIT
URL: http://jashkenas.github.com/coffee-script/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:      %{?scl_prefix_ruby}ruby(release)
Requires:      %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides:      %{?scl_prefix}rubygem(%{gem_name}) = %{version}

# Explicitly require runtime subpackage, as long as older scl-utils do not generate it
Requires: %{?scl_prefix}runtime
Provides:      bundled(js-coffee-script) = %{coffee_script_version}

%description
CoffeeScript is a little language that compiles into JavaScript.
Underneath all of those embarrassing braces and semicolons,
JavaScript has always had a gorgeous object model at its heart.
CoffeeScript is an attempt to expose the good parts of JavaScript
in a simple way.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Keep bundled 
#ln -sf %{_jsdir}/coffee-script/coffee-script.js \
#  %{buildroot}%{gem_libdir}/coffee_script/coffee-script.js

%check
# No test suite included. Some tests are included in rubygem-coffee-script,
# which is the only consumer of this package.

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Wed Feb 24 2016 Pavel Valena <pvalena@redhat.com> - 1.10.0-3
- Update to 1.10.0

* Mon Jan 26 2015 Josef Stribny <jstribny@redhat.com> - 1.6.3-1
- Update to 1.6.3

* Fri Mar 21 2014 Vít Ondruch <vondruch@redhat.com> - 1.3.3-5
- Rebuid against new scl-utils to depend on -runtime package.
  Resolves: rhbz#1069109

* Wed Jun 12 2013 Josef Stribny <jstribny@redhat.com> - 1.3.3-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.3.3-3
- Imported from Fedora again.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Vít Ondruch <vondruch@redhat.com> - 1.3.3-1
- Updated to the coffee-script-source 1.3.3.

* Wed Feb 29 2012 Fotios Lindiakos <fotios@redhat.com> - 1.2.0-2
- Rebuilt with new gem_* macros

* Mon Feb 27 2012 Fotios Lindiakos <fotios@redhat.com> - 1.2.0-1
- Initial package
