%global with_python3 1
%global __provides_exclude_from ^(%{python2_sitearch}|%{python3_sitearch})/.*\\.so$


Name:           python-pandas
Version:        0.15.2
Release:        2%{?dist}
Summary:        Python library providing high-performance data analysis tools

Group:          Development/Languages
License:        BSD
URL:            http://pandas.pydata.org/
Source0:        http://pypi.python.org/packages/source/p/pandas/pandas-%{version}.tar.gz

BuildRequires:  python2-devel, python-setuptools, python-matplotlib
BuildRequires:  Cython
Requires:       pytz
# Update to dateutil 2.x
# https://github.com/pydata/pandas/issues/9305
Requires:       python-dateutil15
Requires:       numpy
Requires:       scipy
Requires:       python-tables
Requires:       python-matplotlib
Requires:       python-Bottleneck
Requires:       python-numexpr

%description
pandas is an open source, BSD-licensed library providing 
high-performance, easy-to-use data structures and data 
analysis tools for the Python programming language.

%if 0%{?with_python3}
%package -n python3-pandas
Summary:        Python library providing high-performance data analysis tools
BuildRequires:  python3-devel, python3-setuptools, python3-matplotlib
BuildRequires:  python3-Cython
Requires:       python3-pytz
Requires:       python3-dateutil15
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-tables
Requires:       python3-matplotlib
Requires:       python3-Bottleneck
Requires:       python3-numexpr

%description -n python3-pandas
pandas is an open source, BSD-licensed library providing 
high-performance, easy-to-use data structures and data 
analysis tools for the Python programming language.

%endif # with_python3

%prep
%setup -q -n pandas-%{version}

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3

%build
CFLAGS=$RPM_OPT_FLAGS %{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS=$RPM_OPT_FLAGS %{__python3} setup.py build
popd
%endif # with_python3


%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
popd
%endif # with_python3

%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT

%files
%doc LICENSE RELEASE.md
%{python2_sitearch}/pandas*

%if 0%{?with_python3}
%files -n python3-pandas
%doc LICENSE RELEASE.md
%{python3_sitearch}/pandas*
%endif # with_python3



%changelog
* Mon Jan 19 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-2
- Update dependence on dateutil to dateutil15 (bz #1183368)

* Wed Dec 17 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-1
- New release of pandas 0.15.2

* Thu Nov 20 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.1-1
- New release of pandas 0.15.1

* Mon Oct 20 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.0-1
- New release of pandas 0.15.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 13 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.14.1-1
- New release of pandas 0.14.1

* Mon Jun 16 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.14.0-1
- New release of pandas 0.14.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 28 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.12.0-4
- Enable python3 build
- Set CFLAGS before build

* Fri Dec 13 2013 Kushal Das <kushal@fedoraproject.org> 0.12.0-3
- Fixed dependency name

* Fri Dec 06 2013 Pierre-Yves Chibon <pingou@pingoured>fr - 0.12.0-2
- Change BR from python-setuptools-devel to python-setuptools
  See https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel

* Fri Sep 20 2013 Kushal Das <kushal@fedoraproject.org> 0.12.0-1
- New release of pandas 0.12.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 24 2012 Kushal Das <kushal@fedoraproject.org> 0.10.0-1
- New release of pandas 0.10.0

* Thu Nov 08 2012 Kushal Das <kushal@fedoraproject.org> 0.10.0-1
- New release of pandas 0.10.0

* Thu Nov 08 2012 Kushal Das <kushal@fedoraproject.org> 0.9-1
- New release of pandas

* Fri Aug 03 2012 Kushal Das <kushal@fedoraproject.org> 0.8.1-2
- Fixes from review request

* Tue Jul 10 2012 Kushal Das <kushal@fedoraproject.org> 0.8.1-1
- Initial release in Fedora

