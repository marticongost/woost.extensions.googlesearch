"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.persistence import migration_step


@migration_step
def preserve_woost2_info(e):
    from woost.models import Configuration, Website

    for cls in (Configuration, Website):
        for obj in cls.select():
            for key in (
                "engine_id",
                "api_key",
                "results_page"
            ):
                old_key = "_google_search_" + key
                try:
                    value = getattr(obj, old_key)
                except AttributeError:
                    pass
                else:
                    delattr(obj, old_key)
                    new_key = "x_googlesearch_" + key
                    setattr(obj, new_key, value)

