
%{?filter_setup:
%filter_provides_in %{python_sitearch}.*\.so$
%filter_setup
}


Name:           python-pandas
Version:        0.10.0
Release:        1%{?dist}
Summary:        Python library providing high-performance data analysis tools

Group:          Development/Languages
License:        BSD
URL:            http://pandas.pydata.org/
Source0:        http://pypi.python.org/packages/source/p/pandas/pandas-%{version}.tar.gz

BuildRequires:  python-devel, python-setuptools-devel, python-matplotlib
Requires:       pytz
Requires:       python-dateutil
Requires:       numpy
Requires:       scipy
Requires:       python-tables
Requires:       python-matplotlib

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

