=========
Migration
=========

As I noticed during testing, and making changes, the move to v2.0.0 from v1.4.0 can be difficult, but this guide is here to make it a whole lot easier

This guide intends to follow `The Zen of Python <https://peps.python.org/pep-0020/>`_,'s quote in line 7,

    Readability counts.

So all of the names will be shortened, non-captialized, and simple to remember. Which is 90% of the reason I'm deprecating a lot in version 2.0.0, to make it more readable

So, instead of

.. code-block::
    :language: python
    :linenos:

    from DisOAuth import AuthUrl, DiscordApi, bot, permissions

We can use

.. code-block::
    :language: python
    :linenos:

    from discoauth import auth, discord, bot, permissions

I highly suggest using the :code:`ctrl + F` shortcut, to find the old names and replace it with the new names

The following list shows what classes and methods are replaced with what name

* :code:`AuthUrl` --> :class:`auth`
* :code:`discordApi` --> :class:`discord`
* :code:`makeUrl` --> :meth:`auth.url`
* :code:`accessToken` --> :meth:`discord.token`
* :code:`User` --> :class:`user`
* :code:`get_current_user` --> :meth:`discord.user.fetch`
* :code:`get_user_guilds` --> :meth:`discord.user.guilds`
* :code:`get_guild` --> :meth:`discord.guild.fetch`

Special Cases
=============

There is one thing I should metion before I close this out, the :code:`get_guild` method that got changed to :code:`fetch`, got moved to a new class called :code:`guild`, so look for the :code:`user` in those statements and replace them with :code:`guild`

