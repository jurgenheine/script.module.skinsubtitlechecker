# -*- coding: utf-8 -*- 
import os
import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs
import unicodedata
from json import loads

__addon__ = xbmcaddon.Addon()
__scriptname__ = __addon__.getAddonInfo('name')
__version__ = __addon__.getAddonInfo('version')
__cwd__ = xbmc.translatePath(__addon__.getAddonInfo('path')).decode("utf-8")
__monitor__ = xbmc.Monitor()

LOGDEBUG = xbmc.LOGDEBUG
LOGERROR = xbmc.LOGERROR
LOGFATAL = xbmc.LOGFATAL
LOGINFO = xbmc.LOGINFO
LOGNONE = xbmc.LOGNONE
LOGNOTICE = xbmc.LOGNOTICE
LOGSEVERE = xbmc.LOGSEVERE
LOGWARNING = xbmc.LOGWARNING
ISO_639_1 =xbmc.ISO_639_1
ISO_639_2 =xbmc.ISO_639_2
ENGLISH_NAME =xbmc.ENGLISH_NAME


def get_version():
    return __version__

def get_kodi_version():
    return int(xbmc.getInfoLabel("System.BuildVersion").split(".")[0])

def get_params(args, index):
    param = {}
    if len(args) > index:
        log(__name__, "params: %s" % args[index])
        paramstring = args[index]
        if len(paramstring) >= 2:
            params = paramstring
            cleanedparams = params.replace('?', '')
            pairsofparams = cleanedparams.split('&')
            param = {}
            for i in range(len(pairsofparams)):
                splitparams = pairsofparams[i].split('=')
                if (len(splitparams)) == 2:
                    param[splitparams[0]] = splitparams[1]
    return param

def log(module, msg, level=xbmc.LOGDEBUG):
    try:
        if isinstance(msg, unicode):
            msg = '%s (ENCODED)' % (msg.encode('utf-8'))

        xbmc.log('%s [%s]: %s' % (__scriptname__, module, msg), level)
    except Exception as e:
        # noinspection PyBroadException
        try:
            xbmc.log('Logging Failure: %s' % e, level)
        except:
            pass  # just give up


def normalize_string(stri):
    return unicodedata.normalize(
         'NFKD', unicode(unicode(stri, 'utf-8'))
         ).encode('ascii', 'ignore')


def translate_path(path):
    return xbmc.translatePath(path).decode('utf-8')


def get_script_path():
    return __cwd__


def convert_language(language, format):
    return xbmc.convertLanguage(language,format)


def get_clean_movie_title(path, usefoldername=False):
    return xbmc.getCleanMovieTitle(path, usefoldername)


def get_condition_visibility(value):
    return xbmc.getCondVisibility(value)


def get_window(id):
    return xbmcgui.Window(id)


def get_info_label(name):
    return xbmc.getInfoLabel(name)


def abort_requested():
    return  __monitor__.abortRequested()


def sleep( time):
    xbmc.sleep(time)


def wait_for_abort(time):
    return __monitor__.waitForAbort(time)


def file_exists(path):
    return xbmcvfs.exists(path)


def mkdirs(path):
    try:
        xbmcvfs.mkdirs(path)
    except:
        os.mkdir(path)


def dirname(path):
    return os.path.dirname(path)


def get_list_item(language, subtitlepressent):
    return xbmcgui.ListItem(label=language, label2=subtitlepressent)


def add_subtitle_list(addon_handle, list):
    length = len(list)
    if length>0:
        xbmcplugin.addDirectoryItems(addon_handle, list, length)
    # set the content of the directory
    xbmcplugin.setContent(addon_handle, 'files')
    xbmcplugin.endOfDirectory(addon_handle)


def send_notification(header, message, time):
    try:
        xbmcgui.Dialog().notification(header, message, xbmcgui.NOTIFICATION_INFO, time, False)
    except:
        command = "Notification(%s,%s, %s)"
        xbmc.executebuiltin(command % (header,message,time))


def get_kodi_setting(name):
        command = '''{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "Settings.GetSettingValue",
    "params": {
        "setting": "%s"
    }
}'''
        result = execute_json_rpc(command % name)
        py = loads(result)
        if 'result' in py and 'value' in py['result']:
            sublang = py['result']['value']
        else:
            log(__scriptname__,"Could not load Subtitle language with Json-RPC, use current kodi language",LOGWARNING)
            return get_interface_language() 

def get_interface_language():
    return xbmc.getLanguage() 

def get_localized_string(id):
    return __addon__.getLocalizedString(id)

def get_addons():
        command = '''{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "Addons.GetAddons",
    "params": { "type": "xbmc.python.script", "enabled": "all" }
    }
}'''
        result = execute_json_rpc(command)
        py = loads(result)
        addons=[]
        for addonObj in json.loads(installedJson)[u'result'][u'addons']:
            
            id = addonObj[u'addonid'] 
            log(__name__,'check addon with id: ' + id,LOGDEBUG)
            if id.startswith('script.skinsubtitlechecker.provider'):
                addons.append(id)
                log(__name__,'add addon with id: ' + id,LOGDEBUG)
        return addons
# example result: {"id":1,"jsonrpc":"2.0","result":{"addons":[ { "path": "/home/xbmc/.xbmc/addons/webinterface.awxi", "type": "xbmc.gui.webinterface", "addonid": "webinterface.awxi" },{ "path": "/home/xbmc/.xbmc/addons/webinterface.awxi", "type": "xbmc.gui.webinterface", "addonid": "webinterface.awxi" }],"limits":{"end":2,"start":0,"total":2}}}


def get_provider_data(name, querystring):
        command = '''{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "Files.GetDirectory",
    "params": {
        "directory": "plugin://%s?%s"
    }
}'''
        result = execute_json_rpc(command % (name, querystring))
        py = loads(result)
        subresult=[]
        if 'result' in py and 'files' in py['result']:
            for file in py['result']['files']:
                item = {'Language':file['label'],'SubtitlePresent':file['label2']}
                subresult.append(item)
        return subresult
# example result: {"id":1,"jsonrpc":"2.0","result":{"files":[{"file":"Media/Big_Buck_Bunny_720.strm","filetype":"file","label":"Big_Buck_Bunny_720.strm","type":"unknown"},{"file":"Media/Big_Buck_Bunny_1080p.mov","filetype":"file","label":"Big_Buck_Bunny_1080p.mov","type":"unknown"}],"limits":{"end":2,"start":0,"total":2}}}


def execute_json_rpc(jsonrpccommand):
    return xbmc.executeJSONRPC(jsonrpccommand)