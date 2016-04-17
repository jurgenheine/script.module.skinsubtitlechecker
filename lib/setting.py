import xbmc
import xbmcaddon
from json import loads
from lib import kodi

class Setting:
    def __init__(self):
        pass
                    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass       

    def get_setting(self, name):
        return kodi.__addon__.getSetting(name)

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

    def get_script_path(self):
        return kodi.__cwd__

    def get_kodi_setting(self, name):
        return kodi.get_kodi_setting(name)

    