%define		_font_name	Nafees_Tahreer_Naskh
Summary:	Free font from Center for Research in Urdu Language Processing
Summary(pl.UTF-8):	Wolnodostępna czcionka z Centrum Badań nad Przetwarzaniem Języka Urdu
Name:		fonts-TTF-CRULP-Nafees_Tahreer_Naskh
Version:	1.0
Release:	0.1
License:	MPL-like
Group:		Fonts
Source0:	http://www.crulp.org/Downloads/localization/fonts/NafeesTahreerNaskh/%{_font_name}_v%{version}.zip
# Source0-md5:	dfc4a1112cf1463cd90e525175146ccc
URL:		http://www.crulp.org/software/localization/Fonts/nafeesTahreerNaskh.html
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
Nafees Tahreer Naskh font for writing Urdu in Naskh script based on Unicode
standard. Guidance and calligraphy of basic glyphs for the font has been
provided by Syed Jameel-ur-Rehman. He is pupil of Syed Nafees Shah and Hafiz
Syed Anees-ul-Hassan. This font is a text font and specially designed for
better on-screen readability at small point sizes.

%prep
%setup -q -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install Nafees\ Tahreer\ Naskh\ v1.01.ttf $RPM_BUILD_ROOT%{ttffontsdir}/%{_font_name}.ttf

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc Nafees_Tahree_Naskh_v%{version}.pdf
%{ttffontsdir}/*.ttf
