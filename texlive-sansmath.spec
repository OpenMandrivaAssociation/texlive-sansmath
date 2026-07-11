%global tl_name sansmath
%global tl_revision 79371

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Maths in a sans font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sansmath
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmath.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines a new math version sans, and a command \sansmath
that behaves somewhat like \boldmath.

