`djff` provides highlighting of unified diffs for django.

It's based on the `django-vcs`_ port of `lodgeit`_'s diff highlighting code.

.. _django-vcs: https://github.com/alex/django-vcs/
.. _lodgeit: http://www.pocoo.org/projects/lodgeit/

Usage
~~~~~

 * Add ``'djff'`` to ``INSTALLED_APPS``.
 * Add ``'django.template.loaders.app_directories.Loader'`` to ``TEMPLATE_LOADERS`` or make the djff/udiff.html template available otherwise
 * Use the builtin filter ``{% load djff_tags %} {{ diffstring|udiff }}``
 * Include ``static/djff.css`` or use custom CSS


