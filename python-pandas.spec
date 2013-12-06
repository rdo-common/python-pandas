%{?filter_setup:
%filter_provides_in %{python_sitearch}.*\.so$
%filter_setup
}


Name:           python-pandas
Version:        0.12.0
Release:        2%{?dist}
Summary:        Python library providing high-performance data analysis tools

Group:          Development/Languages
License:        BSD
URL:            http://pandas.pydata.org/
Source0:        http://pypi.python.org/packages/source/p/pandas/pandas-%{version}.tar.gz

BuildRequires:  python-devel, python-setuptools, python-matplotlib
Requires:       pytz
Requires:       python-dateutil
Requires:       numpy
Requires:       scipy
Requires:       python-tables
Requires:       python-matplotlib
Requires:       python-bottleneck
Requires:       python-numexpr

%description
pandas is an open source, BSD-licensed library providing 
high-performance, easy-to-use data structures and data 
analysis tools for the Python programming language.

%prep
%setup -q -n pandas-%{version}


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT




%files
%doc PKG-INFO README.rst LICENSE
%{python_sitearch}/pandas*


%changelog
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

