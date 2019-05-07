"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.translations import translations
from cocktail.events import when
from woost.admin.sections import Settings
from woost.admin.sections.contentsection import ContentSection

translations.load_bundle("woost.extensions.googlesearch.admin.sections")


class GoogleSearchSettings(Settings):

    icon_uri = "woost.extensions.googlesearch.admin.ui://images/googlesearch.svg"

    members = [
        "x_googlesearch_api_key",
        "x_googlesearch_engine_id",
        "x_googlesearch_results_page"
    ]


@when(ContentSection.declared)
def fill(e):
    e.source.append(GoogleSearchSettings("googlesearch"))

