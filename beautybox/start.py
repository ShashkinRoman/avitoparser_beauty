from beautybox.avito_ads_parser import main as ads_parser
from beautybox.avito_urls_parser import main as urls_parser


def start_ads_parser():
    while True:
        try:
            ads_parser()
            urls_parser()
        except:
            pass