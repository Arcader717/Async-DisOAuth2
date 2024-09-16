from typing import Any, Dict

class UserObj:
    def __init__(self,
                 response) -> None:
        r = response
        self.id = r['id']
        self.username = r['username']
        self.discriminator = r['discriminator']
        if 'global_name' in r:
            self.global_name = r['global_name']
        if 'avatar' in r:
            self.avatar = r['avatar']
        if 'bot' in r:
            self.bot = r['bot']
        else:
            self.bot = False
        if 'system' in r:
            self.system = r['system']
        else:
            self.system = False
        self.mfa_enabled = r['mfa_enabled']
        self.banner = r['banner']
        self.accent_color = r['accent_color']
        self.locale = r['locale']
        if 'verified' in r:
            self.verified = r['verified']
        else:
            self.verified = None
        if 'email' in r:
            self.email = r['email']
        else:
            self.email = None
        self.flags = r['flags']
        self.premium_type = r['premium_type']
        self.public_flags = r['public_flags']
        if 'avatar_decoration' in r:
            self.avatar_decoration = r['avatar_decoration']
        else:
            self.avatar_decoration = None

    def __getitem__ (self, key):
        return getattr(self, key)

    def __dict__(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'username': self.username,
            'discriminator': self.discriminator,
            'global_name': self.global_name,
            'avatar': self.avatar,
            'bot': self.bot,
            'system': self.system,
            'mfa_enabled': self.mfa_enabled,
            'banner': self.banner,
            'accent_color': self.accent_color,
            'locale': self.locale,
            'verified': self.verified,
            'email': self.email,
            'flags': self.flags,
            'premium_type': self.premium_type,
            'public_flags': self.public_flags,
            'avatar_decoration': self.avatar_decoration
        }


class GuildObj:
    def __init__(self,
                 response: dict) -> None:
        self.keys = [
            'id', 'name', 'icon',
            'icon_url', 'splash', 'discovery_splash',
            'owner', 'owner_id', 'permissions',
            'perms', 'region', 'afk_channel_id',
            'afk_timeout', 'widget_enabled', 'widget_channel_id',
            'verification_level', 'default_message_notifications', 'explicit_content_filter',
            'roles', 'emojis', 'features',
            'mfa_level', 'application_id', 'system_channel_id',
            'system_channel_flags', 'rules_channel_id', 'max_presences',
            'max_members', 'vanity_url_code', 'description',
            'banner', 'premium_tier', 'premium_subscription_count',
            'preferred_locale', 'public_updates_channel_id', 'max_video_channel_users',
            'max_stage_video_channel_users', 'approximate_member_count', 'approximate_presence_count',
            'welcome_screen', 'nsfw_level', 'stickers',
            'premium_progress_bar_enabled', 'safety_alert_channel_id'
        ]
        self.id = response.get('id', None)
        self.name = response.get('name', None)
        if "icon" in response:
            self.icon = response['icon']
            self.icon_url = f"https://cdn.discordapp.com/icons/{self.id}/{self.icon}.png"
        else:
            self.icon = None
            self.icon_url = None
        self.splash = response.get('splash', None)
        self.discovery_splash = response.get('discovery_splash', None)
        self.owner = response.get('owner', None)
        self.onwer_id = response['owner_id']
        self.permissions = response.get('permissions', None)
        self.perms = response.get('permissions', None)
        self.region = response.get('region', None)
        self.afk_channel_id = response.get('afk_channel_id', None)
        self.afk_timeout = response.get('afk_timeout', None)
        if "widget_enabled" in response:
            self.widget_enabled = True
        else:
            self.widget_enabled = False
        if "widget_channel_id" in response:
            self.widget_channel_id = response['widget_channel_id']
        else:
            self.widget_channel_id = None
        self.verification_level = response['verification_level']
        self.default_message_notifications = response['default_message_notifications']
        self.explicit_content_filter = response['explicit_content_filter']
        self.roles = response['roles']
        self.emojis = response['emojis']
        self.features = response['features']
        self.mfa_level = response['mfa_level']
        if "application_id" in response:
            self.application_id = response['application_id']
        else:
            self.application_id = None
        if "system_channel_id" in response:
            self.system_channel_id = response['system_channel_id']
        else:
            self.system_channel_id = None
        if "system_channel_flags" in response:
            self.system_channel_flags = response['system_channel_flags']
        else:
            self.system_channel_flags = None
        if "rules_channel_id" in response:
            self.rules_channel_id = response['rules_channel_id']
        else:
            self.rules_channel_id = None
        if "max_presences" in response:
            self.max_presences = response['max_presences']
        else:
            self.max_presences = None
        if "max_members" in response:
            self.max_members = response['max_members']
        else:
            self.max_members = None
        if "vanity_url_code" in response:
            self.vanity_url_code = response['vanity_url_code']
        else:
            self.vanity_url_code = None
        if "description" in response:
            self.description = response['description']
        else:
            self.description = None
        if "banner" in response:
            self.banner = response['banner']
        else:
            self.banner = None
        self.premium_tier = response['premium_tier']
        if "premium_subscription_count" in response:
            self.premium_subscription_count = response['premium_subscription_count']
        else:
            self.premium_subscription_count = None
        if "preferred_locale" in response:
            self.preferred_locale = response['preferred_locale']
        else:
            self.preferred_locale = None
        if "public_updates_channel_id" in response:
            self.public_updates_channel_id = response['public_updates_channel_id']
        else:
            self.public_updates_channel_id = None
        if "max_video_channel_users" in response:
            self.max_video_channel_users = response['max_video_channel_users']
        else:
            self.max_video_channel_users = None
        if "max_stage_video_channel_users" in response:
            self.max_stage_video_channel_users = response['max_stage_video_channel_users']
        else:
            self.max_stage_video_channel_users = None
        if "approximate_member_count" in response:
            self.approximate_member_count = response['approximate_member_count']
        else:
            self.approximate_member_count = None
        if "approximate_presence_count" in response:
            self.approximate_presence_count = response['approximate_presence_count']
        else:
            self.approximate_presence_count = None
        if "welcome_screen" in response:
            self.welcome_screen = response['welcome_screen']
        else:
            self.welcome_screen = None
        if "nsfw_level" in response:
            self.nsfw_level = response['nsfw_level']
        else:
            self.nsfw_level = None
        if "stickers" in response:
            self.stickers = response['stickers']
        else:
            self.stickers = None
        if "premium_progress_bar_enabled" in response:
            self.premium_progress_bar_enabled = response['premium_progress_bar_enabled']
        else:
            self.premium_progress_bar_enabled = False
        if "safety_alerts_channel_id" in response:
            self.safety_alerts_channel_id = response['safety_alerts_channel_id']
        else:
            self.safety_alerts_channel_id = None

    def __getitem__(self, key):
        return getattr(self, key)
