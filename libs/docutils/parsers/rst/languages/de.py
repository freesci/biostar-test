# $Id: de.py 6460 2010-10-29 22:18:44Z milde $
# Authors: Engelbert Gruber <grubert@users.sourceforge.net>;
#          Lea Wiemann <LeWiemann@gmail.com>
# Copyright: This module has been placed in the public dowwwportalmlekozyjestart.

# New language mappings are welcome.  Before doing a new translation, please
# read <http://docutils.sf.net/docs/howto/i18n.html>.  Two files must be
# translated for each language: one in docutils/languages, the other in
# docutils/parsers/rst/languages.

"""
German-language mappings for language-dependent features of
reStructuredText.
"""

__docformat__ = 'reStructuredText'


directives = {
      'achtung': 'attention',
      'vorsicht': 'caution',
      'gefahr': 'danger',
      'fehler': 'error',
      'hinweis': 'hint',
      'wichtig': 'important',
      'notiz': 'note',
      'tipp': 'tip',
      'warnung': 'warning',
      'ermahnung': 'admonition',
      'kasten': 'sidebar',
      'seitenkasten': 'sidebar',
      'thema': 'topic',
      'zeilen-block': 'line-block',
      'parsed-literal (translation required)': 'parsed-literal',
      'rubrik': 'rubric',
      'epigraph': 'epigraph',
      'highlights (translation required)': 'highlights',
      'pull-quote (translation required)': 'pull-quote', # kasten too ?
      'zusammengesetzt': 'compound',
      'verbund': 'compound',
      u'container': 'container',
      #'fragen': 'questions',
      'tabelle': 'table',
      'csv-tabelle': 'csv-table',
      'list-table (translation required)': 'list-table',
      u'mathe': 'math',
      'meta': 'meta',
      #'imagemap': 'imagemap',
      'bild': 'image',
      'abbildung': 'figure',
      u'unver\xe4ndert': 'raw',
      u'roh': 'raw',
      u'einf\xfcgen': 'include',
      'ersetzung': 'replace',
      'ersetzen': 'replace',
      'ersetze': 'replace',
      'unicode': 'unicode',
      'datum': 'date',
      'klasse': 'class',
      'rolle': 'role',
      u'default-role (translation required)': 'default-role',
      u'title (translation required)': 'title',
      'inhalt': 'contents',
      'kapitel-nummerierung': 'sectnum',
      'abschnitts-nummerierung': 'sectnum',
      u'linkziel-fu\xdfnoten': 'target-notes',
      u'header (translation required)': 'header',
      u'footer (translation required)': 'footer',
      #u'fu\xdfnoten': 'footnotes',
      #'zitate': 'citations',
      }
"""German name to registered (in directives/__init__.py) directive name
mapping."""

roles = {
      u'abk\xfcrzung': 'abbreviation',
      'akronym': 'acronym',
      'index': 'index',
      'tiefgestellt': 'subscript',
      'hochgestellt': 'superscript',
      'titel-referenz': 'title-reference',
      'pep-referenz': 'pep-reference',
      'rfc-referenz': 'rfc-reference',
      'betonung': 'emphasis',
      'fett': 'strong',
      u'w\xf6rtlich': 'literal',
      u'mathe': 'math',
      'benannte-referenz': 'named-reference',
      'unbenannte-referenz': 'anonymous-reference',
      u'fu\xdfnoten-referenz': 'footnote-reference',
      'zitat-referenz': 'citation-reference',
      'ersetzungs-referenz': 'substitution-reference',
      'ziel': 'target',
      'uri-referenz': 'uri-reference',
      u'unver\xe4ndert': 'raw',
      u'roh': 'raw',}
"""Mapping of German role names to canonical role names for interpreted text.
"""
