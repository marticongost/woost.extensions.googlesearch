"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail import schema
from cocktail.translations import translations
from woost.models import add_setting, Document

translations.load_bundle("woost.extensions.googlesearch.settings")

add_setting(
    schema.String(
        "x_googlesearch_api_key"
    )
)

add_setting(
    schema.String(
        "x_googlesearch_engine_id"
    )
)

add_setting(
    schema.Reference(
        "x_googlesearch_results_page",
        type = Document
    )
)

