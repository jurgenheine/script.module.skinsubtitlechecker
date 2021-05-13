from skinsubtitlekodi import normalize_string, get_clean_movie_title

class BaseVideoItem:
    item =  None        

    def __init__(self):
        self.item = None
                    
    def __enter__(self):
        return self

    def set_parameter_listitem(self, params,language_iso_639_2):
        self.item = self.create_item(params.get('year', ''),
                                     params.get('season', ''),
                                     params.get('episode', ''),
                                     params.get('tvshow', ''),
                                     params.get('originaltitle', ''),
                                     params.get('title', ''),
                                     params.get('filename', ''),
                                     language_iso_639_2)

    def get_querystring(self):
        querystring = "year=%s&season=%s&episode=%s&tvshow=%s&title=%s&filename=%s&searchlanguage=%s"
        searchlanguage = item['3let_language'][0]
        return querystring % (item['year'],item['season'],item['episode'],item['tvshow'],item['title'],item['filename'],searchlanguage)

    def create_item(self, year, season, episode, tvshow, originaltitle, title, filename,language_iso_639_2):
        item = {'year': normalize_string(year),  # Year
                'season': normalize_string(season),  # Season
                'episode': normalize_string(episode),  # Episode
                'tvshow': normalize_string(tvshow),
                'title': normalize_string(originaltitle),  # try to get original title
                'filename': normalize_string(filename),
                '3let_language': []}

        item['3let_language'].append(language_iso_639_2)
        
        if item['title'] == "":
            item['title'] = normalize_string(title)      # no original title, get just Title
        
        if item['year'] == "":
            item['title'], year = get_clean_movie_title(item['title'])
            item['year'] = str(year)
                    
        if item['episode'].lower().find("s") > -1:  # Check if season is "Special"
            item['season'] = "0"
            item['episode'] = item['episode'][-1:]
        
        return item

    def __exit__(self, exc_type, exc_value, traceback):
        self.item = None
        del self.item

