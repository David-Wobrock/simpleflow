# Order of masks is important !
FOLLOW_MASKS = [
    (0, "follow"),
    (8, "config_nofollow"),
    (4, "robots_nofollow"),
    (2, "meta_nofollow"),
    (1, "link_nofollow"),
]


def follow_mask(val):
    mask = int(val)
    for bitmask, term in FOLLOW_MASKS:
        if bitmask & mask == bitmask:
            return term


STREAMS_FILES = {
    'urlids': 'patterns',
    'urlinfos': 'infos',
    'urlcontents': 'contents',
    'urllinks': 'outlinks',
    'urlinlinks': 'inlinks',
    'url_properties': 'properties'
}

STREAMS_HEADERS = {
    'PATTERNS': (
        ('id', int),
        ('protocol', str),
        ('host', str),
        ('path', str),
        ('query_string', str),
    ),
    'INFOS': (
        ('id', int),
        ('infos_mask', int),
        ('content_type', str),
        ('depth', int),
        ('date_crawled', int),
        ('http_code', int),
        ('byte_size', int),
        ('delay1', int),
        ('delay2', int),
    ),
    'CONTENTS': (
        ('id', int),
        ('content_type', int),
        ('hash', str),
        ('txt', str)
    ),
    'OUTLINKS': (
        ('id', int),
        ('link_type', str),
        ('follow', follow_mask),
        ('dst_url_id', int),
        ('external_url', str)
    ),
    'INLINKS': (
        ('id', int),
        ('link_type', str),
        ('follow', follow_mask),
        ('src_url_id', int),
    ),
    'PROPERTIES': (
        ('id', int),
        ('resource_type', str)
    )
}

CONTENT_TYPE_INDEX = {
    1: 'title',
    2: 'h1',
    3: 'h2',
    4: 'description'
}

MANDATORY_CONTENT_TYPES = ('title', 'h1', 'description')
