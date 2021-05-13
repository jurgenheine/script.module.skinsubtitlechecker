import xbmcaddon
import xbmcvfs

from skinsubtitlekodi import get_kodi_setting
from skinsubtitlenotificationmethod import NotificationMethod

__addon__ = xbmcaddon.Addon()
__cwd__ = xbmcvfs.translatePath(__addon__.getAddonInfo('path'))

class Setting:
    def __init__(self):
        pass
                    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass       

    def get_setting(self, name):
        return __addon__.getSetting(name)

    def get_cache_not_found_timeout(self):
        cachetimenotfound = self.get_setting("CacheTimeNotFound")
        if not cachetimenotfound:
            cachetimenotfound = "2"
        return 60 * 60 * float(cachetimenotfound)

    def get_cache_found_timeout(self):
        cachetimefound = self.get_setting("CacheTimeFound")
        if not cachetimefound:
            cachetimefound = "30"
        return 60 * 60 * 24 * float(cachetimefound)

    def get_polling_interval(self):
        interval = self.get_setting("SkinPollingInterval")
        if not interval:
            interval = "200"
        return int(interval)
    
    def get_provider_search_interval(self):
        cachetimefound = self.get_setting("ProviderSearchInterval")
        if not cachetimefound:
            cachetimefound = "1800"
        return 60 * float(cachetimefound)
    
    def get_notification_delay(self):
        delay = self.get_setting("NotificationPollingInterval")
        if not delay:
            delay = "2000"
        return int(delay)

    def get_notification_method(self):
        method = self.get_setting("NotificationMethod")
        if method=="0":
            return NotificationMethod.AUTO
        if method=="1": 
            return NotificationMethod.POPUP
        return NotificationMethod.SKIN

    def get_notification_duration(self):
        duration = self.get_setting("NotificationDuration")
        if not duration:
            duration = "2"
        return 1000 * float(duration)

    def get_script_path(self):
        return __cwd__

    def get_kodi_setting(self, name):
        return get_kodi_setting(name)

    