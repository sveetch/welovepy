.. _Django: https://www.djangoproject.com/
.. _autobreadcrumbs: http://pypi.python.org/pypi/autobreadcrumbs
.. _django-braces: https://github.com/sveetch/django-braces
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _Sveetchies-accounts: https://github.com/sveetch/sveeaccounts
.. _Sveetchies-documents: http://pypi.python.org/pypi/sveedocuments

Introduction
============

This is a Django webapplication to promote the "WE LOVE PYTHON" alliance and manage client demands.

The Alliance has member (registred user with a profile), each member link to their structure and to the tools and skills they use.

The Homepage display structures, tools and skills that have at less one member.

Requires
========

* Python >= 2.6;
* `Django`_ 1.3;
* `autobreadcrumbs`_;
* `django-crispy-forms`_;
* My `django-braces`_ fork;
* `Sveetchies-accounts`_;

PostgreSQL is recommanded (other SGBD have not been tested).

Optionnally for development you will need to install :

* Less for his command line tool ``lessc`` (to compile Bootstrap and the webapp layout theme);
* Django debug toolbar (you will have to enable it in the settings);

.. NOTE:: The webapp embed some settings for `Sveetchies-documents`_ but actually this 
          is not used so you won't need to install it. This should be deprecated or 
          enable in the future.
