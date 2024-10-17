Name:		texlive-texdoctk
Version:	62186
Release:	2
Summary:	Easy access to package documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/texdoctk
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdoctk.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdoctk.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A Perl/Tk-based GUI for easy access to package documentation
for TeX on Unix platforms; the databases it uses are based on
the texmf/doc subtrees of teTeX, but database files for local
configurations with modified/extended directories can be
derived from them. Note that texdoctk is not a viewer itself,
but an interface for finding documentation files and opening
them with the appropriate viewer; so it relies on appropriate
programs to be installed on the system. However, the choice of
these programs can be configured by the sysadmin or user. Now
only distributed as part of TeX Live, which includes a Windows
executable.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/texdoctk
%{_texmfdistdir}/texmf-dist/scripts/texdoctk
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texdoctk.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texdoctk.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
