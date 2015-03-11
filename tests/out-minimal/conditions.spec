#
# spec file for package conditions
#
# Copyright (c) 2013 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Version:        2.8.2
Release:        0
Summary:        AppArmor userlevel parser utility
License:        GPL-2.0+
Group:          Productivity/Networking/Security
Source0:        apparmor-%{version}.tar.gz
Source1:        apparmor-%{version}.tar.gz.asc
Source2:        %{name}.keyring
%if %{distro} == "suse"
PreReq:         %insserv_prereq
PreReq:         aaa_base
%endif
BuildRequires:  pkg-config
BuildRequires:  python
%if %{with editor}
%ifarch ppc64
Requires:       naughty-stuff
%endif # test commentary
BuildRequires:  gcc-c++
BuildRequires:  update-desktop-files
%endif
BuildRequires:  bbb
Requires:       insserv
BuildRoot: %{_tmppath}/%{name}-%{version}-build
