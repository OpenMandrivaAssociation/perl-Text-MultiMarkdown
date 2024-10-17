%define upstream_name    Text-MultiMarkdown
%define upstream_version 1.000034

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Convert MultiMarkdown syntax to (X)HTML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Encode)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Markdown)

BuildArch:	noarch

%description
Markdown is a text-to-HTML filter; it translates an easy-to-read /
easy-to-write structured text format into HTML. Markdown's text format is
most similar to that of plain text email, and supports features such as
headers, *emphasis*, code blocks, blockquotes, and links.

Markdown's syntax is designed not as a generic markup language, but
specifically to serve as a front-end to (X)HTML. You can use span-level
HTML tags anywhere in a Markdown document, and you can use block level HTML
tags ('<div>', '<table>' etc.). Note that by default Markdown isn't
interpreted in HTML block-level elements, unless you add a 'markdown=1"'
attribute to the element. See the Text::Markdown manpage for details.

This module implements the MultiMarkdown markdown syntax extensions from:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.34-1mdv2011.0
+ Revision: 660021
- update to new version 1.000034

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.0.33-2
+ Revision: 654331
- rebuild for updated spec-helper

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.33-1mdv2011.0
+ Revision: 526464
- update to 1.000033

* Tue Jan 19 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.32-1mdv2010.1
+ Revision: 493588
- update to 1.000032

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.31-1mdv2010.1
+ Revision: 471158
- import perl-Text-MultiMarkdown


* Sun Nov 29 2009 cpan2dist 1.000031-1mdv
- initial mdv release, generated with cpan2dist
