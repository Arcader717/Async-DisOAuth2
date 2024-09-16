=========
Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[`Unreleased`_]
===============

Added
-----

* Get User Function, using a user id, added to the :meth:`discord.user.fetch` method of the :class:`discord.user` class
* Modify Current User
* Get Current Guild Member
* Leave Guild
* Create DM
* Create Guild DM

Fixed
-----

* The documentation in the :doc:`permissions` page
* The documentation in the :doc:`migration` page

[`2.0.0`_] - November 13, 2023
==============================

`Diff`_ for 2.0.0 and 1.4.0 

Not much difference between 2.0.0 and 2.0.0-rc.1

Changed
-------

* The name of the project to **`discoauth`**

[`2.0.0-rc.1`_] - November 13, 2023
===================================

Used to release the final version to Async-DisOAuth

Added
-----

- [`#70 <https://github.com/disoauth/DiscoAuth/pull/70>`_]A :code:`deprecated` folder to hold the deprecated functions 
- New subclass of :class:`discord`, :class:`discord.guild`, to help get specific guilds instead of user guilds

Deprecated
----------

- :class:`AuthUrl`, replaced with :class:`auth`

  - :meth:`AuthUrl.makeUrl`, replaced with :meth:`auth.url`

- :class:`discordApi`, replaced with :class:`discord`

  - :meth:`discordApi.accessToken`, replaced with :meth:`discord.token`
  - :class:`discordApi.User`, replaced with :class:`discord.user` 

    - :meth:`discordApi.User.get_current_user`, replaced with :meth:`discord.user.fetch`
    - :meth:`discordApi.User.get_user_guilds`, replaced with :meth:`discord.user.guilds`
    - :meth:`discordApi.User.get_guild`, replaced with :meth:`discord.guild.fetch` (replace the :class:`discord.user` class with :class:`discord.guild`, to get this to work)


[`1.4.0`_] - November 13, 2023
==============================

Added
-----

- [`#53 <https://github.com/disoauth/DiscoAuth/pull/53>`_] CLI Update (The big point of the next version)
- [`#59 <https://github.com/disoauth/DiscoAuth/pull/59>`_] Tests (Kinda realized that they are really helpful)

Changed
-------

* Moved the docs from ``../docs/source`` to ``../docs``

Fixed
-----

* [`#55 <https://github.com/disoauth/DiscoAuth/pull/55>`_] The scope of the auth url

Removed
-------

* The markdown documentation, for MKDocs, which I am no longer using

[`1.3.0`_] - November 8, 2023
=============================

Added
-----

* [`#33 <https://github.com/disoauth/DiscoAuth/pull/33>`_] :class:`bot` Class, for bot auth

 * :class:`permissions` class, to help with the bot auth

* Documentation:

 * New Contributing Page
 * New deprecate page, for the upcoming renaming of ``DisOAuth`` to ``discoauth``

[`1.2.0`_] - November 6, 2023
=============================

Added
-----

* The all-contributors bot
* A CONTRIBUTING.md
* Guild Object
* A new method in the :class:`User` class, that returns a guild object
* A :code:`with_count` parameter to the methods that return a guild object
* documentation for the guild object

Changed
-------

* The repo name from ``Arcader717/DiscordOAuth2`` to ``disoauth/DiscoAuth``

[`1.1.5`_] - October 31, 2023
=============================

Fixed
-----

* the scope of the auth url

[`1.1.5b1`_] - October 30, 2023
===============================

Fixed
-----

* The scope of the auth url

[`1.1.4`_] - October 30, 2023 
=============================

Fixed
-----

* The scope of the auth url

[`1.1.3`_] - October 27, 2023
=============================

Changed
-------

* [`#21 <https://github.com/disoauth/DiscoAuth/pull/21>`_] Moved the user model to :code:`models.py`

[`1.1.2`_] - October 25, 2023
=============================

Added
-------

* Added the :class:`UserObj` to the documentation


[`1.1.1`_] - October 25, 2023
=============================

Changed
-------

* The goals in the README from the v1.0.0 goals to v2.0.0 goals

[`1.1.0`_] - October 25, 2023
=============================

Added
-----

* Documentation, using `Read The Docs <https://readthedocs.io>`_ and `Sphinx <https://www.sphinx-doc.org/en/master/usage/index.html>`_
* [`#18 <https://github.com/disoauth/DiscoAuth/pull/18>`_] A model for user data

[`1.0.1`_] - September 22, 2023
===============================

Nothing important happened for this update

[`1.0.0`_] - September 22, 2023
===============================

Added
-----

* [`#7 <https://github.com/disoauth/DiscoAuth/pull/7>`_] The subclass, :class:`User` to :class:`discordApi`
* A method in the new :class:`User` class to get user data
* A method to make the auth url in the AuthUrl class

Fixed
-----

* The state generation

[`0.2.1`_] - September 18, 2023
===============================

Changed
-------

* Renamed Package from :code:`DisOAuth` to :code:`Async-DisOAuth` to accomodate for the Sync version of :code:`DisOAuth`

  * (Later, the Sync version would be discontinued)

[`0.2.0`_] - September 15, 2023
===================================================================================

Added
-----

* The :class:`discordApi` class
* The :meth:`discordApi.accessToken` method, to get the access token of a user
* A method of :class:`discordApi` to check the app's auth info
* MIT License

[`0.1.4`_] - September 13, 2023
===================================================================================

Changed
-------

* Package renamed from :code:`DiscordOAuth2` to :code:`DisOAuth`

[`0.1.3`_] - September 13, 2023
===================================================================================

Changed
-------

* Package renamed from :code:`DiscordOAuth-Helper` to :code:`DiscordOAuth2` 

[`0.1.2`_] - September 13, 2023
===================================================================================

Added
-----

* The authors in pyproject.toml [`Commit <https://github.com/disoauth/DiscoAuth/commit/dd673466ba882fa6dca4bd1dbfa793158878b2d3>`_]

[`0.1.1`_] - September 13, 2023
===================================================================================

Changed
-------

* publish.yml (The workflow to publish the package) was moved to DiscordOAuth2(the earlier name of the repo)/.gituhb/workflows from the root directory

[`0.1.0`_] - September 13, 2023
=================================================================================

Added
-----

* The AuthUrl class, that would return the auth url
  * Added a function to make the state for the auth url

.. _Unreleased: https://github.com/disoauth/DiscoAuth/compare/v2.0.0...add/Arcader717-User-functions
.. _Diff: https://github.com/disoauth/DiscoAuth/compare/v1.4.0...v2.0.0
.. _2.0.0: https://github.com/disoauth/DiscoAuth/compare/v2.0.0-rc.1...v2.0.0
.. _2.0.0-rc.1: https://github.com/disoauth/DiscoAuth/compare/v1.4.0...v2.0.0-rc.1
.. _1.4.0: https://github.com/disoauth/DiscoAuth/compare/v1.3.0...v1.4.0
.. _1.3.0: https://github.com/disoauth/DiscoAuth/compare/v1.2.0...v1.3.0
.. _1.2.0: https://github.com/disoauth/DiscoAuth/compare/v1.1.5...v1.2.0
.. _1.1.5: https://github.com/disoauth/DiscoAuth/compare/v1.1.5b1...v1.1.5
.. _1.1.5b1: https://github.com/disoauth/DiscoAuth/compare/v1.1.4...v1.1.5b1
.. _1.1.4: https://github.com/disoauth/DiscoAuth/compare/v1.1.3...v1.1.4
.. _1.1.3: https://github.com/disoauth/DiscoAuth/compare/v1.1.2...v1.1.3
.. _1.1.2: https://github.com/disoauth/DiscoAuth/compare/v1.1.1...v1.1.2
.. _1.1.1: https://github.com/disoauth/DiscoAuth/compare/v1.1.0...v1.1.1
.. _1.1.0: https://github.com/disoauth/DiscoAuth/compare/v1.0.1...v1.1.0
.. _1.0.1: https://github.com/disoauth/DiscoAuth/compare/v1.0.0...v1.0.1
.. _1.0.0: https://github.com/disoauth/DiscoAuth/compare/v0.2.1...v1.0.0
.. _0.2.1: https://github.com/disoauth/DiscoAuth/compare/v0.2.0...v0.2.1
.. _0.2.0: https://github.com/disoauth/DiscoAuth/compare/v0.1.4...v0.2.0
.. _0.1.4: https://github.com/disoauth/DiscoAuth/compare/v0.1.3...v0.1.4
.. _0.1.3: https://github.com/disoauth/DiscoAuth/compare/v0.1.2...v0.1.3
.. _0.1.2: https://github.com/disoauth/DiscoAuth/compare/v0.1.1...v0.1.2
.. _0.1.1: https://github.com/disoauth/DiscoAuth/compare/v0.1...v0.1.1
.. _0.1.0: https://github.com/disoauth/DiscoAuth/tree/v0.1
