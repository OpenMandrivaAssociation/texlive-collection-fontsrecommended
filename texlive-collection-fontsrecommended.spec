Name:		texlive-collection-fontsrecommended
Epoch:		1
Version:	54074
Release:	2
Summary:	Recommended fonts
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-fontsrecommended.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-avantgar
Requires:	texlive-bookman
Requires:	texlive-charter
Requires:	texlive-cm-super
Requires:	texlive-cmextra
Requires:	texlive-courier
Requires:	texlive-ec
Requires:	texlive-euro
Requires:	texlive-euro-ce
Requires:	texlive-eurosym
Requires:	texlive-fpl
Requires:	texlive-helvetic
Requires:	texlive-lm
Requires:	texlive-lm-math
Requires:	texlive-marvosym
Requires:	texlive-mathpazo
Requires:	texlive-ncntrsbk
Requires:	texlive-palatino
Requires:	texlive-pxfonts
Requires:	texlive-rsfs
Requires:	texlive-symbol
Requires:	texlive-tex-gyre
Requires:	texlive-tex-gyre-math
Requires:	texlive-times
Requires:	texlive-tipa
Requires:	texlive-txfonts
Requires:	texlive-utopia
Requires:	texlive-wasy
Requires:	texlive-wasysym
Requires:	texlive-zapfchan
Requires:	texlive-zapfding
%rename texlive-fonts
%rename texlive-texmf-fonts

%description
Recommended fonts, including the base 35 PostScript fonts,
Latin Modern, TeX Gyre, and T1 and other encoding support for
Computer Modern, in outline form.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
