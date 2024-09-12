Name:           osinfor
Version:        1.0.0
Release:        1%{?dist}
Summary:        An example Rust application

License:        MIT
URL:            https://gitee.com/openeuler/osinfor
Source0:        osinfor-%{version}.tar.gz

%description
This is a project written in the Rust language, which includes functions such as obtaining system arch and version.

%prep
%setup -q

%build
cargo build 

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm755 target/debug/osinfor %{buildroot}%{_bindir}/osinfor

%files
%{_bindir}/osinfor

%changelog
* Sun Sep 08 2024 Colommar yfxx_weiyx@163.com> - 1.0.0-1
- First release
