Name:		anaconda-installclass-goose
Version:	0.1
Release:	1%{?dist}
Summary:	GoOSe Linux installclass for Anaconda

Group:		Applications/System
License:	GPLv2+
URL:		https://github.com/gooseproject/%{name}/
Source0:	https://github.com/gooseproject/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:  noarch

BuildRequires:	anaconda
Requires:	anaconda

%description
Anaconda installclasses provide options for types of installations. Rather
than providing just 'Minimal' as an install task, anaconda-installclass-goose
provides different options like 'Web Server', 'Desktop' and others


%prep
%setup -q


%build
echo OK

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{python_sitearch}/pyanaconda/installclasses/
install -p pyanaconda/installclasses/goose.py $RPM_BUILD_ROOT/%{python_sitearch}/pyanaconda/installclasses/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README
%{python_sitearch}/pyanaconda/installclasses/goose.py*


%changelog
* Tue Mar 13 2012 Clint Savage <herlo@gooseproject.org> - 0.1-1
- Initial package

