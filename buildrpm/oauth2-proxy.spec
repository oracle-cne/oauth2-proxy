

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global app_name                oauth2-proxy
%global app_version             7.14.1
%global oracle_release_version  1
%global _buildhost              build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:           %{app_name}
Version:        %{app_version}
Release:        %{oracle_release_version}%{?dist}
Summary:        OAuth2-Proxy is a flexible, open-source tool that can act as either a standalone reverse proxy or a middleware component integrated into existing reverse proxy or load balancer setups.
License:        MIT
Group:          System/Management
Url:            https://github.com/oauth2-proxy/oauth2-proxy
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  golang
BuildRequires:	make

%description
OAuth2-Proxy is a flexible, open-source tool that can act as either a standalone reverse proxy or a middleware component integrated into existing reverse proxy or load balancer setups.

%prep

%setup -q -n %{name}-%{version}

%build
make build

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 oauth2-proxy %{buildroot}%{_bindir}

%files
%license LICENSE THIRD_PARTY_LICENSES.txt olm/SECURITY.md
%{_bindir}/oauth2-proxy

%changelog
* Fri Jan 23 2026 Oracle Cloud Native Environment Authors <noreply@oracle.com> - 7.14.1-1
- Added Oracle specific build files for oauth2-proxy

