%global srcname pandas

%if 0%{?fedora}
%bcond_without python3
%else
%bcond_with python3
%endif

Name:           python-%{srcname}
Version:        0.19.1
Release:        2%{?dist}.2
Summary:        Python library providing high-performance data analysis tools

License:        BSD
URL:            http://pandas.pydata.org/
Source0:        https://pypi.io/packages/source/p/pandas/%{srcname}-%{version}.tar.gz

%global __provides_exclude_from ^(%{python2_sitearch}|%{python3_sitearch})/.*\\.so$

%description
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data
analysis tools for the Python programming language.

%package -n python2-%{srcname}
Summary:        Python library providing high-performance data analysis tools
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-matplotlib
BuildRequires:  python2-Cython
Requires:       pytz
Requires:       python-dateutil
Requires:       python2-numpy
Requires:       python2-scipy
# TODO: fix that package to provide python2-tables
Requires:       python-tables
Requires:       python2-matplotlib
Requires:       python-Bottleneck
Requires:       python2-numexpr
%if 0%{?fedora}
Recommends:     python2-pandas-datareader
Recommends:     python2-xlrd
Recommends:     python2-xlwt
%endif

%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data
analysis tools for the Python programming language.

Python 2 version.

%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary:        Python library providing high-performance data analysis tools
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-matplotlib
BuildRequires:  python3-Cython
Requires:       python3-pytz
Requires:       python3-dateutil
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-tables
Requires:       python3-matplotlib
Requires:       python3-Bottleneck
Requires:       python3-numexpr
%if 0%{?fedora}
Recommends:     python3-pandas-datareader
Recommends:     python3-xlrd
Recommends:     python3-xlwt
%endif

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data
analysis tools for the Python programming language.

Python 3 version.
%endif # with_python3

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif # with_python3

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif # with_python3

%files -n python2-%{srcname}
%doc RELEASE.md
%license LICENSE
%{python2_sitearch}/%{srcname}*

%if 0%{?with_python3}
%files -n python3-pandas
%doc RELEASE.md
%license LICENSE
%{python3_sitearch}/%{srcname}*
%endif # with_python3

%changelog
* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.19.1-2
- Rebuild for Python 3.6

* Wed Nov 09 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.19.1-1
- New upstream version (0.19.1)

* Wed Oct 19 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.19.0-1
- New upstream version (0.19.0)
- Brings pandas-datareader using recommends

* Sat Oct 15 2016 Peter Robinson <pbrobinson@fedoraproject.org> - 0.18.1-3
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.18.1-1
- New upstream version (0.18.1)
- Update pypi url

* Sat Apr 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.18.0-3
- Fix broken deps

* Sat Apr 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.18.0-2
- Fix python_provide macros usage (FTBFS for some packages)

* Wed Mar 30 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.18.0-1
- New upstream version (0.18.0)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.17.1-1
- New upstream version (0.17.1)
- Add new dependecy as weak dep (fixes bz #1288919)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 28 2015 Orion Poplawski <orion@cora.nwra.com> - 0.17.0-2
- Use common build directory, new python macros
- Filter provides
- Fix provides

* Mon Oct 12 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.17.0-1
- New release of pandas 0.17.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.16.2-1
- New release of pandas 0.16.2

* Mon May 18 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.16.1-1
- New release of pandas 0.16.1

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.16.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 24 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.16.0-1
- New release of pandas 0.16.0
- Use license macro
- Don't use py3dir (new python guidelines)

* Tue Jan 20 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-3
- Pandas actually supports dateutil 2

* Mon Jan 19 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-2
- Update dependency on dateutil to dateutil15 (bz #1183368)

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

