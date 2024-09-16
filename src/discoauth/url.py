from typing import Any, List, Type, Dict

import requests

from discoauth.common import generate_token, getToken, htmlEncode, joinUrl, permsByList, bot_perms, bot_perms_key

from discoauth.models import UserObj as uObj, GuildObj as gObj

from discoauth.exceptions import DiscordException

apiUrl = "https://discord.com/api"



class auth:
    def __init__(self,
                 client_id: str,
                 scope: List[str],
                 redirect_uri: str,
                 permissions: Any | None = None,
                 **extras) -> None:
        """
        Makes and returns a url that is used to authorize users

        :param client_id: The client ID of your discord app
        :param scope: A list of scopes you want to use
        :param redirect_uri: The redirect uri you want to use
        :type client_id: str
        :type scope: List[str]
        :type redirect_uri: str
        """
        self._client_id = client_id
        self._scope = scope
        self._redirect_uri = redirect_uri
        if permissions is not None:
            if isinstance(permissions, int):
                self._perms = permissions
            else:
                self._perms = permissions.value
        else:
            self._perms = None
        if len(extras) > 0:
            if "test" in extras:
                self.test = True
        else:
            self.test = False

    async def url(self) -> str:
        """
        Returns the authorization link that was made

        :async:
        :returns: The authorization link. Redirect the user to the link and after they authorize, they will return to your redirect URI.
        :rtype: str
        """
        scope = self._scope
        redirect_uri = self._redirect_uri
        client_id = self._client_id
        if not self.test:
            state = await generate_token()
        elif self.test:
            state = '1'
        self.strScope = ""
        for s in scope:
            self.strScope += s
            self.strScope += " "
        scope1 = self.strScope.rstrip(" ")
        _scope = scope1.replace(" ", "%20")
        redirectUri = await htmlEncode(redirect_uri)
        url = await joinUrl(client_id, _scope, redirectUri, state)
        if self._perms is not None:
            url += f"&permissions={self._perms}"
        return url

class discord:
    def __init__(self,
                 client_id,
                 client_secret,
                 scope: list[str],
                 redirect_uri) -> None:
        """Where you can get an access code, use the api links to get info

        client_id - The client id of your application
        client_secret - The client secret of your application
        scope - a list of the scopes you authorized for
        redirect_uri -- the redirect_uri you want to use
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.redirect_uri = redirect_uri


    async def token(self, code) -> dict[str, str]:
        """Takes values input into discordApi, and the code
        returns the response as a dictionary

        Keyword Arguments:
        code -- The code you got when the user authorized
        """
        tokenDict = getToken(code,
                             self.scope,
                             self.redirect_uri,
                             self.client_id,
                             self.client_secret)
        return await tokenDict


    class user:
        def __init__(self, token):
            if isinstance(token, dict):
                try:
                    self.token = token['access_token']
                except KeyError:
                    raise DiscordException(token['error']) from KeyError
            elif isinstance(token, str):
                self.token = token

        

        async def fetch(self, 
                        id: int | None = None,
                        *extras) -> uObj:
            if isinstance(id, int):
                url = apiUrl + f"/users/{id}"
            else:
                url = apiUrl + "/users/@me"
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer ' + self.token
            }
            r = requests.get(url, headers=headers)
            if 'raw' in extras:
                return r.json()
            return uObj(r.json())

        async def guilds(self,
                                  with_count: bool | None = False,
                         *extras) -> List[gObj]:
            url = apiUrl + "/users/@me/guilds"
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer ' + self.token
            }
            query = {}
            if with_count == True:
                query['with_counts'] = True
            else:
                query['with_counts'] = False
            r = requests.get(url, headers=headers)
            guildList = []
            if 'raw' in extras:
                return r.json()
            for guild in r.json():
                guildList.append(gObj(guild))
            return guildList

        async def modify(self, username: str | None = None):
            url = apiUrl + "/users/@me"
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer ' + self.token
            }
            query = {}
            if isinstance(username, str):
                query['username'] = username
                r = requests.patch(url, headers, json=query)
            else:
                r = requests.patch(url, headers)
            return r.json()

        async def leaveGuild(self, guild: str | int):
            url = apiUrl + f"/users/@me/guilds/{str(id)}"
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer ' + self.token
            }
            r = requests.delete(url, headers)
            if r.status_code == '204':
                return True
            else:
                return False

        async def dm(self, id: str | None = None,
                     tokens: List[str] | None = None,
                     nicks: Dict[str, str] | None = None):
            url = apiUrl + "/users/@me/channels"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.token
            }
            if isinstance(id, str):
                query = {'recipient_id': id}
                r = requests.post(url, headers, json=query)
                if isinstance(access_tokens, list) or isinstance(nicks, dict):
                    raise ValueError("You can't try to make a group DM and a regular dm at the same time")
            elif isinstance(access_tokens, list) and isinstance(nicks, dict):
                query = {'access_tokens': tokens,
                         'nicks': nicks}
                r = requests.post(url, headers, json=query)
            return r.json()

        async def connections(self, id: str | None = None):
            # Requires connections scope, for basic connections, and role_connections.write for application connections
            if isinstance(id, None):
                url = baseUrl + "/users/@me/connections"
            elif isinstance(id, str):
                url = baseUrl + f"/users/@me/applications/{id}/role-connection"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.token
            }
            r = requests.get(url, headers)
            return r.json()
            
                
        async def modifyConnections(self, id: str):
            url = baseUrl + f"/users/@me/applications/{id}/role-connection"
            headers = {
                'Content-Type': 'applcation/json',
                'Authorization': 'Bearer ' + self.token
            }
            r = requests.put(url, headers)
            return r.json()

    class guild:
        def __init__(self, token):
            if isinstance(token, dict):
                self.token = token['access_token']
            elif isinstance(token, str):
                self.token = token

        async def fetch(self,
                        id: int,
                        with_counts: bool | None = False) -> gObj:
            url = apiUrl + f"/guilds/{id}"
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer ' + self.token
            }
            query = {}
            if with_counts == True:
                query['with_counts'] = True
            elif with_counts == False:
                query['with_counts'] = False
            r = requests.get(url, headers=headers, params=query)
            return gObj(r.json())

class bot:
    def __init__(self,
                 client_id,
                 permissions) -> None:
        """
        Makes an auth url for bots
        :param client_id: The client id of your bot
        :param permissions: The permissions of your bot. Either a number or a list of permissions
        :type client_id: int
        :type permissions: int or List[str] 
        """
        self.id = int(client_id)
        if permissions is Type[permissions]:
            self.permissions = permissions.value
        else:
            self.permissions = permissions

    async def url(self) -> str:
        """
        Returns the url for bot auth
        
        :return: The url for bot auth
        :rtype: str
        """
        url = f"https://discord.com/api/oauth2/authorize?client_id={self.id}&permissions={self.permissions}&scope=bot"
        return url

class permissions:
    def __init__(self, permissions=None):
        self.perm_list = [
            "create_instant_invite", "kick_members", "ban_members",
            "administrator", "manage_channels", "manage_guild",
            "add_reactions", "view_audit_log", "priority_speaker", "stream",
            "view_channel", "send_messages", "send_tts_messages",
            "manage_messages", "embed_links", "attach_files",
            "read_message_history", "mention_everyone", "use_external_emojis",
            "view_guild_insights", "connect", "speak", "mute_members",
            "deafen_members", "move_members", "use_vad", "change_nickname",
            "manage_nicknames", "manage_roles", "manage_webhooks",
            "manage_guild_expressions", "use_application_commands",
            "request_to_speak", "manage_events", "manage_threads",
            "create_public_threads", "create_private_threads",
            "use_external_sticker", "send_messages_in_threads",
            "use_embedded_activities", "moderate_members",
            "view_creator_monetization_analytics", "use_soundboard",
            "use_external_sounds", "send_voice_messages"
        ]

        self.value = 0x0

        if permissions is not None:
            self._parse_permissions(permissions)

    def _parse_permissions(self, permissions):
        if isinstance(permissions, (list, int, str, dict)):
            if isinstance(permissions, list):
                for perm in permissions:
                    self._apply_permission(perm)
            elif isinstance(permissions, (int, str)):
                self._apply_permission(permissions)
            elif isinstance(permissions, dict):
                for key, value in permissions.items():
                    self._apply_permission(key, value)
        else:
            raise ValueError("Invalid permissions format")

    def _apply_permission(self, perm, value=True):
        if isinstance(perm, int):
            perm_key = bot_perms_key.get(perm)
        elif isinstance(perm, str):
            perm_key = bot_perms.get(perm.upper())

        if perm_key is None:
            raise ValueError(f"{perm} is not a valid permission")

        if isinstance(perm_key, str):
            perm_value = bot_perms[perm_key.upper()]
        else:
            perm_value = perm_key

        if value:
            self.value |= int(perm_value)
            if isinstance(perm_key, str):
                setattr(self, perm_key.lower(), True)
            elif isinstance(perm_key, int):
                setattr(self, perm.lower(), True)
        else:
            self.value &= ~perm_value
            if isinstance(perm_key, str):
                setattr(self, perm_key.lower(), False)
            elif isinstance(perm_key, int):
                setattr(self, perm.lower(), False)

    def __getattr__(self, name):
        if name in self.perm_list:
            return False
        else:
            raise AttributeError(f"{name} is not a valid permission")

    async def update(
        self, permissions: List[str | int] | str | int | Dict[int | str, bool]
    ) -> None:
        """
        Updates the permissions to update what permissions you want.
        If the permission is already added, updating will remove it, and vice versa

        :param permissions: The permissions you want to update
        :type permissions: List of int or str, str, int, Dictionary of int or str as keys and a bool as the value"""
        self._parse_permissions(permissions=permissions)

    async def add(self, permissions: int | str | List[int | str]) -> None:
        """
        Adds the permissions provided to the value, and if the permissions is already added, doesn't change it.

        :param permissions: The permissions you want to add
        :type permissions: int, str, or list of int or str
        """
        if isinstance(permissions, (int, str)):
            perms = {permissions: True}
            self._parse_permissions(perms)
        elif isinstance(permissions, list):
            perms = {}
            for perm in permissions:
                perms[perm] = True
            self._parse_permissions(perms)

    async def remove(self, permissions: int | str | List[int | str]) -> None:
        """
        Removes the permissions provided to the value, and if the permissions is already removed, doesn't change it.
        
        :param permissions: The permissions you want to add
        :type permissions: int, str, or list of int or str
        """
        if isinstance(permissions, (int, str)):
            perms = {permissions: False}
            self._parse_permissions(perms)
        elif isinstance(permissions, list):
            perms = {}
            for perm in permissions:
                perms[perm] = False

    
    async def all(self) -> None:
        perms = {}
        for perm in self.perm_list:
            perms[perm] = True
            self._parse_permissions(perms)

    async def none(self) -> None:
        perms = {}
        for perm in self.perm_list:
            perms[perm] = False
            self._parse_permissions(perms)

    async def general(self) -> None:
        perm_list = [5, 28, 4, 30, 29, 7, 10, 19]
        self.value = await permsByList(perm_list)
    
    async def allChannel(self) -> None:
        perm_list = [28, 4, 0, 29, 10, 11, 38, 35, 36, 12, 13, 34, 14, 15, 16, 17, 6, 18,
                     37, 31, 20, 21, 22, 23, 24, 25, 8, 32, 9, 42]
        self.value = await permsByList(perm_list)

    async def membership(self) -> None:
        perm_list = [1, 2, 0, 27, 26, 40]
        self.value = await permsByList(perm_list)

    async def text(self) -> None:
        perm_list = [11, 38, 35, 36, 12, 13, 34, 14, 15, 16, 17, 6, 18, 37, 31, 46]
        self.value = await permsByList(perm_list)

    async def voice(self) -> None:
        perm_list = [20, 21, 22, 23, 25, 8, 9, 39, 42, 45]
        self.value = await permsByList(perm_list)

    async def stage(self) -> None:
        perm_list = [32]
        self.value = await permsByList(perm_list)
    
    async def stage_moderator(self) -> None:
        perm_list = [4, 22, 24]
        self.value = await permsByList(perm_list)

    async def elevated(self) -> None:
        perm_list = [3, 5, 28, 4, 1, 2, 30, 29, 40, 13, 34]
        self.value = await permsByList(perm_list)

    async def advanced(self) -> None:
        perm_list = [3]
        self.value = await permsByList(perm_list)


