# -*- coding: utf-8 -*-
from skinsubtitlekodi import convert_language,ISO_639_2,ENGLISH_NAME
from skinsubtitlesetting import Setting
 
class LanguageHelper:
    def __init__(self):
        self.__init_languages()
        self.__init_translationlanguages()
                            
    def __enter__(self):
        return self

    def get_ISO_639_2(self, language):
        isocode = self.__get_translationIso(language)
        if(isocode == None):
            return convert_language(language, ISO_639_2)
        return isocode

    def get_english_name(self, iso_639_2_code):
        language = self.__get_translationLanguage(iso_639_2_code)
        if(language == None):
            return convert_language(iso_639_2_code, ENGLISH_NAME)
        return language

    def get_podnapisi_code(self,iso_639_2_code):
        for x in self.translationlanguage:
            if language == x[3]:
                return x[1]

    def get_kodi_translation_code(self,iso_639_2_code):
        for x in self.translationlanguage:
            if language == x[3]:
                return x[5]

    def get_kodi_setting_code(self,iso_639_2_code):
        for x in self.translationlanguage:
            if language == x[3]:
                return x[4]

    def __get_translationIso(self,language):
        for x in self.translationlanguage:
            if language == x[0]:
                return x[3]
        return None

    def __get_translationLanguage(self,iso_639_2_code):
        for x in self.translationlanguage:
            if iso_639_2_code == x[3]:
                return x[0]
        return None

    def get_ISO_639_2_B(self, iso_639_2_code):
        for x in self.languages:
            if iso_639_2_code == x[2] or iso_639_2_code == x[3]:
                return x[2]
        return iso_639_2_code

    def get_ISO_639_2_T(self, iso_639_2_code):
        for x in self.languages:
            if iso_639_2_code == x[2] or iso_639_2_code == x[3]:
                return x[3]
        return iso_639_2_code

    def __exit__(self, exc_type, exc_value, traceback):
        self.languages = None
        self.translationlanguage = None
        del self.languages
        del self.translationlanguage

    def __init_languages(self):
       self.languages = (

                            # Full Language name[0]       ISO 639-1          ISO 639-2B             ISO 639-2T

                            ("Albanian"                   , "sq",            "alb",                 "sqi"  ),
                            ("Armenian"                   , "hy",            "arm",                 "hye"  ),
                            ("Basque"                     , "eu",            "baq",                 "eus"  ),
                            ("Burmese"                    , "my",            "bur",                 "mya"  ),
                            ("Chinese"                    , "zh",            "chi",                 "zho"  ),
                            ("Czech"                      , "cs",            "cze",                 "ces"  ),
                            ("Dutch"                      , "nl",            "dut",                 "nld"  ),
                            ("French"                     , "fr",            "fre",                 "fra"  ),
                            ("Georgian"                   , "ka",            "geo",                 "kat"  ),
                            ("German"                     , "de",            "ger",                 "deu"  ),
                            ("Greek"                      , "el",            "gre",                 "ell"  ),
                            ("Icelandic"                  , "is",            "ice",                 "isl"  ),
                            ("Persian"                    , "fa",            "per",                 "fas"  ),
                            ("Macedonian"                 , "mk",            "mac",                 "mkd"  ),
                            ("Malay"                      , "ms",            "may",                 "msa"  ),
                            ("Maori"                      , "mi",            "mao",                 "mri"  ),
                            ("Romanian"                   , "ro",            "rum",                 "ron"  ),
                            ("Slovak"                     , "sk",            "slo",                 "slk"  ),
                            ("Tibetan"                    , "bo",            "tib",                 "bod"  ),
                            ("Welsh"                      , "cy",            "wel",                 "cym"  ),
                        )

    def __init_translationlanguages(self):        
        self.translationlanguage = (

    # Full Language name[0]     podnapisi[1]  ISO 639-1[2]   ISO 639-2 Code[3]   Script Setting Language[4]   localized name id number[5]

    ("Albanian"                   , "29",       "sq",            "alb",                 "0",                     30201  ),
    ("Arabic"                     , "12",       "ar",            "ara",                 "1",                     30202  ),
    ("Belarusian"                 , "0" ,       "hy",            "arm",                 "2",                     30203  ),
    ("Bosnian"                    , "10",       "bs",            "bos",                 "3",                     30204  ),
    ("BosnianLatin"               , "10",       "bs",            "bos",                 "3",                     30204  ),
    ("Bulgarian"                  , "33",       "bg",            "bul",                 "4",                     30205  ),
    ("Catalan"                    , "53",       "ca",            "cat",                 "5",                     30206  ),
    ("Chinese"                    , "17",       "zh",            "chi",                 "6",                     30207  ),
    ("Chinese (Traditional)"      , "17",       "zh",            "chi",                 "6",                     30207  ),
    ("Chinese (Simplified)"       , "17",       "zh",            "chi",                 "6",                     30207  ),
    ("Croatian"                   , "38",       "hr",            "hrv",                 "7",                     30208  ),
    ("Czech"                      , "7",        "cs",            "cze",                 "8",                     30209  ),
    ("Danish"                     , "24",       "da",            "dan",                 "9",                     30210  ),
    ("Dutch"                      , "23",       "nl",            "dut",                 "10",                    30211  ),
    ("English"                    , "2",        "en",            "eng",                 "11",                    30212  ),
    ("English (US)"               , "2",        "en",            "eng",                 "11",                    30212  ),
    ("English (UK)"               , "2",        "en",            "eng",                 "11",                    30212  ),
    ("Estonian"                   , "20",       "et",            "est",                 "12",                    30213  ),
    ("Finnish"                    , "31",       "fi",            "fin",                 "14",                    30214  ),
    ("French"                     , "8",        "fr",            "fre",                 "15",                    30215  ),
    ("German"                     , "5",        "de",            "ger",                 "16",                    30216  ),
    ("Greek"                      , "16",       "el",            "ell",                 "17",                    30217  ),
    ("Hebrew"                     , "22",       "he",            "heb",                 "18",                    30218  ),
    ("Hindi"                      , "42",       "hi",            "hin",                 "19",                    30219  ),
    ("Hungarian"                  , "15",       "hu",            "hun",                 "20",                    30220  ),
    ("Icelandic"                  , "6",        "is",            "ice",                 "21",                    30221  ),
    ("Indonesian"                 , "0",        "id",            "ind",                 "22",                    30222  ),
    ("Italian"                    , "9",        "it",            "ita",                 "23",                    30224  ),
    ("Japanese"                   , "11",       "ja",            "jpn",                 "24",                    30225  ),
    ("Korean"                     , "4",        "ko",            "kor",                 "25",                    30226  ),
    ("Latvian"                    , "21",       "lv",            "lav",                 "26",                    30227  ),
    ("Lithuanian"                 , "0",        "lt",            "lit",                 "27",                    30228  ),
    ("Macedonian"                 , "35",       "mk",            "mac",                 "28",                    30229  ),
    ("Malay"                      , "0",        "ms",            "may",                 "29",                    30248  ),    
    ("Norwegian"                  , "3",        "no",            "nor",                 "30",                    30230  ),
    ("Polish"                     , "26",       "pl",            "pol",                 "31",                    30232  ),
    ("Portuguese"                 , "32",       "pt",            "por",                 "32",                    30233  ),
    ("Portuguese (Brazil)"        , "48",       "pb",            "pob",                 "33",                    30234  ),
    ("PortugueseBrazil"           , "48",       "pb",            "pob",                 "33",                    30234  ),
    ("Portuguese (Brazilian)"     , "48",       "pb",            "pob",                 "33",                    30234  ),
    ("Portuguese-BR"              , "48",       "pb",            "pob",                 "33",                    30234  ),
    ("Brazilian"                  , "48",       "pb",            "pob",                 "33",                    30234  ),
    ("Romanian"                   , "13",       "ro",            "rum",                 "34",                    30235  ),
    ("Russian"                    , "27",       "ru",            "rus",                 "35",                    30236  ),
    ("Serbian"                    , "36",       "sr",            "scc",                 "36",                    30237  ),
    ("SerbianLatin"               , "36",       "sr",            "scc",                 "36",                    30237  ),
    ("Slovak"                     , "37",       "sk",            "slo",                 "37",                    30238  ),
    ("Slovenian"                  , "1",        "sl",            "slv",                 "38",                    30239  ),
    ("Spanish"                    , "28",       "es",            "spa",                 "39",                    30240  ),
    ("Espa?ol (Latinoam?rica)"    , "28",       "es",            "spa",                 "39",                    30240  ),
    ("Espa?ol (Espa?a)"           , "28",       "es",            "spa",                 "39",                    30240  ),
    ("Spanish (Latin America)"    , "28",       "es",            "spa",                 "39",                    30240  ),
    ("Espa?ol"                    , "28",       "es",            "spa",                 "39",                    30240  ),
    ("Spanish (Spain)"            , "28",       "es",            "spa",                 "39",                    30240  ),
    ("Swedish"                    , "25",       "sv",            "swe",                 "40",                    30242  ),
    ("Thai"                       , "0",        "th",            "tha",                 "41",                    30243  ),
    ("Turkish"                    , "30",       "tr",            "tur",                 "42",                    30244  ),
    ("Ukrainian"                  , "46",       "uk",            "ukr",                 "43",                    30245  ),
    ("Vietnamese"                 , "51",       "vi",            "vie",                 "44",                    30246  ),
    ("Persian"                    , "52",       "fa",            "per",                 "13",                    30247  ),
    ("Farsi"                      , "52",       "fa",            "per",                 "13",                    30247  ))
