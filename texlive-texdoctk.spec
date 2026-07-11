%global tl_name texdoctk
%global tl_revision 62186

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6.0
Release:	%{tl_revision}.1
Summary:	Easy access to package documentation
Group:		Publishing
URL:		https://www.ctan.org/pkg/texdoctk
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdoctk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdoctk.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(kpathsea)
Requires:	texlive(texdoctk.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A Perl/Tk-based GUI for easy access to package documentation for TeX on
Unix platforms; the databases it uses are based on the texmf/doc
subtrees of teTeX, but database files for local configurations with
modified/extended directories can be derived from them. Note that
texdoctk is not a viewer itself, but an interface for finding
documentation files and opening them with the appropriate viewer; so it
relies on appropriate programs to be installed on the system. However,
the choice of these programs can be configured by the sysadmin or user.
Now only distributed as part of TeX Live, which includes a Windows
executable.

