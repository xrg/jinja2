%define git_repo python-jinja2
%define git_head HEAD

%define tarname Jinja2

# jinja requires itself ( as python-sphinx use it ) to build doc
%define enable_doc 1

Summary:	Python template engine
Name:		python-jinja2
Version:	%git_get_ver
Release:	%mkrel %git_get_rel2
Source:		%git_bs_source %{name}-%{version}.tar.gz
Source1:	%{name}-gitrpm.version
Source2:	%{name}-changelog.gitrpm.txt
License:	BSD
Group:		Development/Python
Url:		http://jinja.pocoo.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
# weird, should maybe be removed ( misc ) 17/01/2011
Obsoletes:	python-jinja
Suggests:	python-markupsafe
BuildRequires:	python-devel python-setuptools
%if %enable_doc
BuildRequires:	python-sphinx
%endif

%description
Jinja2 is a library for Python 2.4 and onwards that is designed to be
flexible, fast and secure. If you have any exposure to other
text-based template languages, such as Smarty or Django, you should
feel right at home with Jinja2. It's both designer and developer
friendly by sticking to Python's principles and adding functionality
useful for templating environments.

%prep
%git_get_source
%setup -q

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build 
%if %enable_doc
%make -C docs html
%endif

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
%__rm -rf docs/_build/html/.buildinfo

%check
make test

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc AUTHORS CHANGES LICENSE examples 
%if %enable_doc
%doc docs/_build/html
%endif
