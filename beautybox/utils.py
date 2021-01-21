from datetime import datetime
def ulr_builder(region: str, object_parse: str, search_request: str):
    """
    Сompose url for collect urls with ads.
    :param region:
    :param object_parse:
    :param search_request:
    :return: url: str
    """
    if object_parse == 'beauty':
        url_with_ads = 'https://www.avito.ru/' + region \
              + '/predlozheniya_uslug/krasota_zdorove-ASgBAgICAUSYC6qfAQ?q=' \
              + search_request + '&p='
        return url_with_ads
