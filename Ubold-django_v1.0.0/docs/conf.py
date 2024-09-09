# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
import django

if os.getenv("READTHEDOCS", default=False) == "True":
    sys.path.insert(0, os.path.abspath(".."))
    os.environ["DJANGO_READ_DOT_ENV_FILE"] = "True"
    os.environ["USE_DOCKER"] = "no"
else:
    sys.path.insert(0, os.path.abspath(".."))
os.environ["DATABASE_URL"] = "sqlite:///readthedocs.db"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

# -- Project information -----------------------------------------------------

project = "Ubold Django"
copyright = """2021, Coderthemes Design (coderthemes.com)"""
author = "Coderthemes Design"
version = "v1.0"

html_show_sphinx = False
html_show_sourcelink = False

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = [
    'custom.css',
]

html_logo = "logo.png"

html_theme_options = {
    "sidebar_hide_name": True,
    "light_css_variables": {
        "font-stack": "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol",
        "font-stack-monospace": "Courier, monospace",
        "font-size-normal": "75%",
        "color-background-primary": "#ffffff",
        "color-sidebar-background": "#f5f8fa",
        "color-brand-primary": "#2892fd",
        "color-brand-content": "#f75964",
        "color-admonition-background": "#ffffff",
    },
}