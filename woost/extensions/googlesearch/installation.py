"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from woost.models import ExtensionAssets, Page, CustomBlock


def install():
    """Creates the assets required by the googlesearch extension."""

    assets = ExtensionAssets("googlesearch")

    assets.require(
        Page,
        "results_page",
        title = assets.TRANSLATIONS,
        blocks = [
            assets.require(
                CustomBlock,
                "results_block",
                view_class = "woost.extensions.googlesearch.GoogleCSEResults"
            )
        ]
    )

