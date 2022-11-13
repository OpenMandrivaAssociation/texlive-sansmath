Name:		texlive-sansmath
Version:	17997
Release:	1
Summary:	Maths in a sans font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sansmath
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmath.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a new math version sans, and a command
\sansmath that behaves somewhat like \boldmath.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sansmath/sansmath.sty
%doc %{_texmfdistdir}/doc/latex/sansmath/miscdoc.sty
%doc %{_texmfdistdir}/doc/latex/sansmath/sansmath.pdf
%doc %{_texmfdistdir}/doc/latex/sansmath/sansmath.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
