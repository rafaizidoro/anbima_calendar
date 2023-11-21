import os
import sys

sys.path.insert(0, os.path.abspath("../../anbima_calendar"))

project = "Anbima Calendar"
copyright = "2023, Rafael Izidoro"
author = "Rafael Izidoro"
release = "0.1.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_baseurl = "https://rizidoro.github.io/anbima_calendar/"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
