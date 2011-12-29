# revision 17997
# category Package
# catalog-ctan /macros/latex/contrib/sansmath
# catalog-date 2010-04-29 07:59:03 +0200
# catalog-license pd
# catalog-version 1.1
Name:		texlive-sansmath
Version:	1.1
Release:	1
Summary:	Maths in a sans font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sansmath
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmath.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
