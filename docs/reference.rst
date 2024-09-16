=============
API Reference
=============

.. note:: If you want to check the extra documentation on permissions, check the :doc:`permissions` documentation

.. py:class:: auth(client_id, scope, redirect_uri, permissions)

  the base of the authorization url

  :param client_id: The client id of your app
  :param scope: A list of Discord scopes
  :param redirect_uri: The redirect uri you want to use
  :param permissions: The permissions of the bot, Optional
  :type client_id: str
  :type scope: List[str]
  :type redirect_uri: str
  :type permissions: int or the :class:`permissions` class

  .. py:method:: url()
    :async:

    Makes the actual url and returns it

    :return: The auth link
    :rtype: str

.. py:class:: discord(client_id, client_secret, scope, redirect_uri)

  Where you can get your access token, and use some Discord API links

  :param client_id: The client id of your app
  :param client_secret: The client secret of your app
  :param scope: a list of the scopes you authorized for
  :param redirect_uri: The redirect_uri you want to use
  :type client_id: str
  :type client_secret: str
  :type scope: List[str]
  :type redirect_uri: str

  .. py:method:: token(code)
    :async:

    Makes a request to discord to get an access token

    :param code: The code that you get after the user gets redirected to your application
    :type code: str
    :return: The response recieved after the request is made
    :rtype: dict[str, str]

  .. py:class:: user(token)

    The links for the User API in Discord

    :param token: The access token you get after using the :meth:`accessToken` method in the :class:`discordApi` class

    .. versionchanged:: 2.0
      Renamed to :class:`discord.user` from :class:`discordApi.User`

    .. py:method:: fetch()
      :async:

      Uses the access token provided to request the current user from discord api

      :return: The response from the Discord API
      :rtype: :class:`UserObj`

      .. versionchanged:: 2.0
        Renamed from :meth:`discordApi.User.get_current_user` to :meth:`discord.user.fetch` 

    .. py:method:: guilds()
      :async:

      Gets the users guilds from Discord

      :return: A list of partial Guild objects
      :rtype: List[str]

      .. versionadded:: 1.1
        Used to get the users guilds.

      .. versionchanged:: 2.0
        Renamed to :meth:`discord.user.guilds` from the previous :meth:`discordApi.User.get_user_guilds`

    .. py:method:: modify(username)
      :async:

      Changes the username or avatar url of the user

      :param username: The username of the user that you would like to modify, this is NOT the user's display name. Defaults to none, and uses the access token as the user
      :type username: str | None
      :return: The json returned by Discord API

      .. versionadded:: 2.1

    .. py:method:: leaveGuild(guild)
      :async:

      Makes a user leave a guild

      :param guild: The id of the guild
      :type guild: str | int
      :return: Whether the user had left. Returns true if successful, and false if not
      :rtype: bool

      .. versionadded:: 2.1

    .. py:method:: dm(id, tokens, nicks)
      :async:
      
      DM a user or group of users

      :param id: The id of the user you want to DM. This does not apply to group DM's
      :param tokens: The access tokens of the users you would like to DM. This does not apply to DMing a single user
      :param nicks: The nicks of the users. This does not apply to DMing a single user
      :type id: str | None = None
      :type tokens: List[str] | None = None
      :type nicks: Dict[str, str] | None = None
      :return: The json response returned by Discord API

      .. versionadded:: 2.1

    .. py:method:: connections(id)
      :async:

      Can get a user's regular and application connections. Must use the ``connections`` scope for regular connections, and ``role_connections.write`` for application connections

      :param id: The id of the application connected to a user
      :type: str | None = None
      :return: The json response returned by Discord API

      .. versionadded:: 2.1

    .. py:method:: modifyConnections(id)
      :async:

      Modifies a user's application connections

      :param id: The id of the application
      :return: The json response returned by Discord API

      .. versionadded:: 2.1

  .. py:class:: guild(token)

    Provides access to the guild links in the Discord API

    .. versionadded:: 2.0
        Mainly used to hold the :meth:`discord.guild.fetch` method

    :param token: A user token

    .. py:method:: fetch(id, with_counts)
      :async:

      Gets a guild from the Guild ID

      :param id: The id of the guild you want
      :param with_counts: an optional parameter that indicates you want (True) Discord to return :py:attr:`approximate_member_count` :py:attr:`approximate_presence_count` or not (False). Defaults to False
      :type id: bool or None
      :type with_counts: int or None
      :return: The guild object for the given id
      :rtype: :class:`GuildObj`
    
    .. versionadded:: 1.2
        Based off of the ``GET /guilds/<id>`` endpoint

    .. versionchanged:: 2.0
        Moved to the :class:`discord.guild` class from the :class:`discord.user` class

.. py:class:: bot(client_id, permissions)

  Makes an auth url, but for bots

  :param client_id: The client id of your bot
  :param permissions: The permissions of your bot
  :type permissions: int or :class:`permissions`

  .. py:method:: url()
    :async:

    Returns the url for the bot auth    

    :return: The url for bot auth
    :rtype: str

.. py:class:: permissions(permissions)

  Updates, removes, and adds permissions that you want to use

  .. versionadded:: 1.3

  :param permissions: The permissions you want to use. Optional
  :type permissions: List of int or str, int, str, dictionary with keys as either int or str and values as bools, or None

  .. py:method:: update(permissions)
    :async:

    Updates the permissions to what you want

    :param permissions: The permissions you want to update
    :type permissions: List of int or str, str, int, Dictionary of int or str as keys and a bool as the value

  .. py:method:: add(permissions)
    :async:

    Adds the permissions provided to the value, and if the permissions is already added, doesn't change it.

    :param permissions: The permissions you want to add
    :type permissions: int, str, or list of int or str

  .. py:method:: remove(permissions)
    :async:

    Removes the permissions provided, and if the permissions were already False, it doesn't change it.

    :param permissions: The permissions you want to remove
    :type permissions: int, str, or list of int or str

  .. py:method:: all()
    :async:

    Adds all of the permissions to the permission value

  .. py:method:: none()
    :async:

    Sets all permissions to false

  .. py:method:: general()
    :async:

    sets the permission value to include the following permissions:

      - manage_guild
      - manage_roles
      - manage_channels
      - manage_guild_expressions
      - manage_webhooks
      - view_audit_log
      - view_channel
      - view_guild_insights

  .. py:method:: allChannel()
    :async:

    sets the permission value to include the following permissions:

      - manage_roles
      - manage_channels
      - create_instant_invite
      - manage_webhooks
      - view_channel
      - send_messages
      - use_external_sticker
      - create_public_threads
      - create_private_threads
      - send_tts_messages
      - send_messages
      - manage_threads
      - embed_links
      - attach_files
      - read_message_history
      - mention_everyone
      - add_reactions
      - use_external_emojis
      - moderate_members
      - use_application_commands
      - connect
      - speak
      - mute_members
      - deafen_members
      - move_members
      - use_vad
      - priority_speaker
      - request_to_speak
      - stream
      - use_soundboard

  .. py:method:: membership()
    :async:

    sets the permission value to include the following permissions:

      - kick_members
      - ban_members
      - create_instant_invite
      - manage_nicknames
      - change_nickname
      - moderate_members

  .. py:method:: text()
    :async:

    sets the permission value to include the following permissions:

      - send_messages
      - use_external_sticker
      - create_public_threads
      - create_private_threads
      - send_tts_messages
      - manage_messages
      - embed_links
      - attach_files
      - read_message_history
      - mention_everyone
      - add_reactions
      - use_external_emojis
      - moderate_members
      - use_application_commands
      - send_voice_messages

  .. py:method:: voice()
    :async:

    sets the permission value to include the following permissions:

      - connect
      - speak
      - mute_members
      - deafen_members
      - use_vad
      - priority_speaker
      - stream
      - use_embedded_activities
      - use_soundboard
      - use_external_sounds

  .. py:method:: stage()
    :async:

    sets the permission value to include the following permissions:

      - request_to_speak

  .. py:method:: stage_moderator()
    :async:

    sets the permission value to include the following permissions:

      - manage_channels
      - mute_members
      - move_members

  .. py:method:: elevated()
    :async:

    sets the permission value to include the following permissions:

      - administrator
      - manage_guild
      - manage_roles
      - manage_channels
      - kick_members
      - ban_members
      - manage_guild_expressions
      - manage_guild
      - moderate_members
      - manage_messages
      - manage_threads

  .. py:method:: advanced()
    :async:

    sets the permission value to include the following permissions:

      - administrator

Models
------

.. important:: 

  None of the classes, functions, methods, or objects mentioned below are meant to be set by the user, only by the package

The models are what I use to return a object that is sent from Discord Api

.. py:class:: UserObj(payload)
    
  .. py:property:: id

    The user's id

  .. property:: username

    The user's username (not always unique)

    :type: str
    
  .. property:: discriminator

    the user's Discord-Tag

    :type: str

  .. property:: global_name

    The display name. For bots, it's the application name

    :type: str or None
    
  .. property:: avatar

    The user's avatar hash

    :type: str or None
    
  .. property:: bot

    Whether the user is a bot or not

    :type: bool
    
  .. property:: system

    Whether the user is a part of the Discord System or not

    :type: bool
    
  .. property:: mfa_enabled

    Whether the user has Multi-Factor Authentication on or not

    :type: bool
    
  .. property:: banner

    The user's banner hash.

    :type: str or None
    
  .. property:: accent_color

    The user's banner color, as a hexadecimal

    :type: int or None
    
  .. property:: locale

    The user's selected language option

    :type: str
    
  .. property:: verified

    Whether the user's email is verified or not

    :type: bool
    
  .. property:: email

    The user's email

    :type: str or None
    
  .. property:: flags

    The flags on the user's account

    :type: int or None
    
  .. property:: premium_type

    The type of nitro the user has

    :type: int or None
    
  .. property:: public_flags

    The public flags on a user's account

    :type: int or None
    
  .. property:: avatar_decoration

    The user's avatar decoration hash

    :type: str or None
    

.. class:: GuildObj

  .. versionadded:: 1.2

    Represents a guild object returned by Discord
    
  .. property:: id

    The id of the Guild

  .. property:: name

    The name of the guild

    :type: str

  .. property:: icon

    The icon hash of the guild

    :type: str or None

  .. property:: icon_url

    The url for the guild's icon

    :type: str or None

  .. property:: splash

    The splash hash of the guild

    :type: str or None

  .. property:: discovery_splash

    The discovery splash hash of the guild

    :type: str or None

  .. property:: owner

    Whether the user is the owner of the guild. Returned only when using the :meth:`get_user_guilds()` method

    :type: bool or None

  .. property:: owner_id

    the user id of the owner of the guild

  .. property:: permissions

    The permissions of the user in the current guild

    :type: str or None

  .. property:: perms

    The shortened name of permissions

    .. seealso::

      Property :py:attr:`permissions`
        The regular name

    :type: str or None
    
  .. property:: region

    .. depreciated:: 
      This was only added to follow the guild object from Discord. Replaced by channel.rtc_region

    the region of the guild

    :type: str or None

  .. property:: afk_channel_id

    the channel id where afk users go

  .. property:: afk_timeout

    The time it takes for a afk user to be sent to the afk channel

  .. property:: widget_enabled

    Whether a widget is enabled or not

    :type: bool or None

  .. property:: widget_channel_id

    The channel the widget is in

  .. property:: verification_level

    The level of verification in the guild

    :type: int or None

  .. property:: default_message_notifications

    The default notification level of the guild

    :type: int or None

  .. property:: explicit_content_filter

    The content filter level of the guild

    :type: int or None

  .. property:: roles

    The roles of the guild, as an array

  .. property:: emojis

    The emojis of the guild, as an array of emoji object

  .. property:: features

    The features of the guild

  .. property:: mfa_level

    The required level of MFA (Multi-Factor Authentication) for the guild

    :type: int

  .. property:: application_id

    ID of the application that made the guild, if it is bot-created

  .. property:: system_channel_id

    the id of the channel where guild notices such as welcome messages and boost events are posted

  .. property:: system_channel_flags

    System channel flags

    :type: integer

  .. property:: rules_channel_id

    the id of the channel where Community guilds can display rules and/or guidelines

  .. property:: max_presences

    the maximum number of presences for the guild (None is always returned apart from the largest of guilds)

    :type: int or None

  .. property:: max_members

    the maximum number of members for the guild

    :type: int or None

  .. property:: vanity_url_code

    the vanity url code for the guild

    :type: str or None

  .. property:: description

    the description of the guild

    :type: str or None

  .. property:: banner

    The banner hash

    :type: str or None

  .. property:: premium_tier

    The guild's premium tier (Server Boost level)

    :type: int

  .. property:: premium_subscription_count

    the number of boosts this guild currently has

    :type: int or None

  .. property:: preferred_locale

    The preferred locale of a community guild; userd in server discovery and notices from Discord, and sent in interactions; defaults to "en-US"

    :type: str

  .. property:: public_updates_channel_id

    The id of the channel where admins and moderators of Community guilds recieve notices from Discord

  .. property:: max_video_channel_users

    The maximum amount of users in a video channel

    :type: int

  .. property:: max_stage_video_channel_users

    the maximum amount of users in a stage video channel

    :type: int

  .. property:: approximate_member_count

    approximate number of members in this guild, returned from :meth:`get_guild` and :meth`get_user_guilds` when ``with_counts`` is ``True``

    :type: int

  .. property:: approximate_presence_count

    approximate number of non-offline members in this guild, returned from the :meth:`get_guild` and :meth:`get_user_guilds` when ``with_counts`` is ``True``

    :type: int

  .. property:: welcome_screen

    the welcome screen of a Community guild, shown to new members, returned in an Invite's guild object

    :type: Discord welcome screen object

  .. property:: nsfw_level

    The guild's nsfw level

    :type: int

  .. property:: stickers

    The guild's custom stickers

  .. property:: premium_progress_bar_enabled

    whether the guild has the boost progress bar enabled

    :type: bool

  .. property:: safety_alerts_channel_id

    the id of the channel where admins and moderators of Community guilds recieve safety alerts from Discord
