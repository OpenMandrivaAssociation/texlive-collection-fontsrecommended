%global tl_name collection-fontsrecommended
%global tl_revision 54074

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Recommended fonts
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-fontsrecommended
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-fontsrecommended.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(avantgar)
Requires:	texlive(bookman)
Requires:	texlive(charter)
Requires:	texlive(cm-super)
Requires:	texlive(cmextra)
Requires:	texlive(collection-basic)
Requires:	texlive(courier)
Requires:	texlive(euro)
Requires:	texlive(euro-ce)
Requires:	texlive(eurosym)
Requires:	texlive(fpl)
Requires:	texlive(helvetic)
Requires:	texlive(lm)
Requires:	texlive(lm-math)
Requires:	texlive(manfnt-font)
Requires:	texlive(marvosym)
Requires:	texlive(mathpazo)
Requires:	texlive(mflogo-font)
Requires:	texlive(ncntrsbk)
Requires:	texlive(palatino)
Requires:	texlive(pxfonts)
Requires:	texlive(rsfs)
Requires:	texlive(symbol)
Requires:	texlive(tex-gyre)
Requires:	texlive(tex-gyre-math)
Requires:	texlive(times)
Requires:	texlive(tipa)
Requires:	texlive(txfonts)
Requires:	texlive(utopia)
Requires:	texlive(wasy)
Requires:	texlive(wasy-type1)
Requires:	texlive(wasysym)
Requires:	texlive(zapfchan)
Requires:	texlive(zapfding)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Recommended fonts, including the base 35 PostScript fonts, Latin Modern,
TeX Gyre, and T1 and other encoding support for Computer Modern, in
outline form.

