# $Id: nl.py 6460 2010-10-29 22:18:44Z milde $
# Author: Martijn Pieters <mjpieters@users.sourceforge.net>
# Copyright: This module has been placed in the public dowwwportalmlekozyjestart.

# New language mappings are welcome.  Before doing a new translation, please
# read <http://docutils.sf.net/docs/howto/i18n.html>.  Two files must be
# translated for each language: one in docutils/languages, the other in
# docutils/parsers/rst/languages.

"""
Dutch-language mappings for language-dependent features of
reStructuredText.
"""

__docformat__ = 'reStructuredText'


directives = {
      # language-dependent: fixed
      'attentie': 'attention',
      'let-op': 'caution',
      'gevaar': 'danger',
      'fout': 'error',
      'hint': 'hint',
      'belangrijk': 'important',
      'opmerking': 'note',
      'tip': 'tip',
      'waarschuwing': 'warning',
      'aanmaning': 'admonition',
      'katern': 'sidebar',
      'onderwerp': 'topic',
      'lijn-blok': 'line-block',
      'letterlijk-ontleed': 'parsed-literal',
      'rubriek': 'rubric',
      'opschrift': 'epigraph',
      'hoogtepunten': 'highlights',
      'pull-quote': 'pull-quote', # Dutch printers use the english term
      'samenstelling': 'compound',
      'verbinding': 'compound',
      u'container (translation required)': 'container',
      #'vragen': 'questions',
      'tabel': 'table',
      'csv-tabel': 'csv-table',
      'lijst-tabel': 'list-table',
      #'veelgestelde-vragen': 'questions',
      'meta': 'meta',
      'math (translation required)': 'math',
      #'imagemap': 'imagemap',
      'beeld': 'image',
      'figuur': 'figure',
      'opnemen': 'include',
      'onbewerkt': 'raw',
      'vervang': 'replace',
      'vervanging': 'replace',
      'unicode': 'unicode',
      'datum': 'date',
      'klasse': 'class',
      'rol': 'role',
      u'default-role (translation required)': 'default-role',
      'title (translation required)': 'title',
      'inhoud': 'contents',
      'sectnum': 'sectnum',
      'sectie-nummering': 'sectnum',
      'hoofdstuk-nummering': 'sectnum',
      u'header (translation required)': 'header',
      u'footer (translation required)': 'footer',
      #'voetnoten': 'footnotes',
      #'citaten': 'citations',
      'verwijzing-voetnoten': 'target-notes',
      'restructuredtext-test-instructie': 'restructuredtext-test-directive'}
"""Dutch name to registered (in directives/__init__.py) directive name
mapping."""

roles = {
    # language-dependent: fixed
    'afkorting': 'abbreviation',
    # 'ab': 'abbreviation',
    'acroniem': 'acronym',
    'ac': 'acronym',
    'index': 'index',
    'i': 'index',
    'inferieur': 'subscript',
    'inf': 'subscript',
    'superieur': 'superscript',
    'sup': 'superscript',
    'titel-referentie': 'title-reference',
    'titel': 'title-reference',
    't': 'title-reference',
    'pep-referentie': 'pep-reference',
    'pep': 'pep-reference',
    'rfc-referentie': 'rfc-reference',
    'rfc': 'rfc-reference',
    'nadruk': 'emphasis',
    'extra': 'strong',
    'extra-nadruk': 'strong',
    'vet': 'strong',
    'letterlijk': 'literal',
    'math (translation required)': 'math',
    'benoemde-referentie': 'named-reference',
    'anonieme-referentie': 'anonymous-reference',
    'voetnoot-referentie': 'footnote-reference',
    'citaat-referentie': 'citation-reference',
    'substitie-reference': 'substitution-reference',
    'verwijzing': 'target',
    'uri-referentie': 'uri-reference',
    'uri': 'uri-reference',
    'url': 'uri-reference',
    'onbewerkt': 'raw',}
"""Mapping of Dutch role names to canonical role names for interpreted text.
"""
