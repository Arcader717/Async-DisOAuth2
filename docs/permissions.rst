Permissions
===========

The permissions can be setup using:

- the names of the permissions, or
- numbers based off of the value in the discord documentation for permissions

The permissions is imported using the :class:`permissions` class

.. code-block:: python
  :linenos:
  :caption: perms.py

  from discoauth import permissions

Permissions
-----------

To set multiple permission with the names when the :class:`permissions` class is first initialized, use a list of the names, or numbers(ints), like in the examples below

.. code-block:: python
  :lineno-start: 3
  :caption: Multiple perms, init, name

  perms = permissions(["kick_members", "ban_members"])

.. code-block:: python
  :lineno-start: 3
  :caption: Multiple perms, init, numbers

  perms = permissions([1, 2])

+-------------------------------------+--------+
| Permissions (name)                  | Number |
+=====================================+========+
| create_instant_invite               | 0      |
+-------------------------------------+--------+
| kick_members                        | 1      |
+-------------------------------------+--------+
| ban_members                         | 2      |
+-------------------------------------+--------+
| administrator                       | 3      |
+-------------------------------------+--------+
| manage_channels                     | 4      |
+-------------------------------------+--------+
| manage_guild                        | 5      |
+-------------------------------------+--------+
| add_reactions                       | 6      |
+-------------------------------------+--------+
| view_audit_log                      | 7      |
+-------------------------------------+--------+
| priority_speaker                    | 8      |
+-------------------------------------+--------+
| stream                              | 9      |
+-------------------------------------+--------+
| view_channel                        | 10     |
+-------------------------------------+--------+
| send_messages                       | 11     |
+-------------------------------------+--------+
| send_tts_messages                   | 12     |
+-------------------------------------+--------+
| manage_messages                     | 13     |
+-------------------------------------+--------+
| embed_links                         | 14     |
+-------------------------------------+--------+
| attach_files                        | 15     |
+-------------------------------------+--------+
| read_message_history                | 16     |
+-------------------------------------+--------+
| mention_everyone                    | 17     |
+-------------------------------------+--------+
| use_external_emojis                 | 18     |
+-------------------------------------+--------+
| view_guild_insights                 | 19     |
+-------------------------------------+--------+
| connect                             | 20     |
+-------------------------------------+--------+
| speak                               | 21     |
+-------------------------------------+--------+
| mute_members                        | 22     |
+-------------------------------------+--------+
| deafen_members                      | 23     |
+-------------------------------------+--------+
| move_members                        | 24     |
+-------------------------------------+--------+
| use_vad                             | 25     |
+-------------------------------------+--------+
| change_nickname                     | 26     |
+-------------------------------------+--------+
| manage_nicknames                    | 27     |
+-------------------------------------+--------+
| manage_roles                        | 28     |
+-------------------------------------+--------+
| manage_webhooks                     | 29     |
+-------------------------------------+--------+
| manage_guild_expressions            | 30     |
+-------------------------------------+--------+
| use_application_commands            | 31     |
+-------------------------------------+--------+
| request_to_speak                    | 32     |
+-------------------------------------+--------+
| manage_events                       | 33     |
+-------------------------------------+--------+
| manage_threads                      | 34     |
+-------------------------------------+--------+
| create_public_threads               | 35     |
+-------------------------------------+--------+
| create_private_threads              | 36     |
+-------------------------------------+--------+
| moderate_members                    | 37     |
+-------------------------------------+--------+
| use_external_sticker                | 38     |
+-------------------------------------+--------+
| use_embedded_activities             | 39     |
+-------------------------------------+--------+
| moderate_members                    | 40     |
+-------------------------------------+--------+
| view_creator_monetization_analytics | 41     |
+-------------------------------------+--------+
| use_soundboard                      | 42     |
+-------------------------------------+--------+
| use_external_sounds                 | 45     |
+-------------------------------------+--------+
| send_voice_messages                 | 46     |
+-------------------------------------+--------+
