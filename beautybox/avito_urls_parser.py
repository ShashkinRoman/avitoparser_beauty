from datetime import datetime
from beautybox.models import Url, Region, category_parsing_dict
# from avitoparser.utils import UrlsBuilder, flats_request_avito
from beautybox.webdriver_start import Operadriver, path
from selenium.common.exceptions import NoSuchElementException
from beautybox.utils import ulr_builder
from time import sleep
from random import randint

def find_last_page(driver):
    try:
        last_page = driver.find_elements_by_class_name('pagination-item-1WyVp')[-2].text
    except IndexError:
        last_page = 0
    except Exception as e:
        last_page = 0
        print('Unexpected error', e)
    return last_page


def get_urls(driver_desktop, region, repeat_counter, search_request):
    urls_ads_obj = driver_desktop.find_elements_by_class_name('iva-item-titleStep-2bjuh')
    if len(urls_ads_obj) == 0:
        print(f'check urls_avito_parser/def get_urls/urls_ads_ob {datetime.now().isoformat()}')
    counter = 0
    for url in urls_ads_obj:
        try:
            url_ = url.find_element_by_tag_name('a').get_attribute('href')
            try:
                Url.objects.get(url=url_)
                counter += 1
            except Url.DoesNotExist:
                Url.objects.create(
                    url=url_,
                    region=Region.objects.get(region_name=region),
                    search_request=search_request
                )
                print(f"{url_} added  {datetime.now().isoformat()}'")
        except NoSuchElementException:
            print(f'check urls_avito_parser/def get_urls/url_  {datetime.now().isoformat()}')
        except:
            print(f"for {url} urls not parsed")
        if counter >= 45:
            repeat_counter += 1
    print(f"repeat_counter {repeat_counter}")


def check_baning(driver_desktop):
    return False


def main():
    # todo add receive via argument category_regions, object_parse, search_recuests
    category_regions = category_parsing_dict.get('small')
    object_parse = 'beauty'
    search_requests = ['ресницы']
    # todo add receiving argument, and request regions of database depending on category_regions
    regions = []
    [regions.append(i[0]) for i in list(Region.objects.filter(category_parsing=category_regions).values_list('region_name'))]
    # regions = ['balakovo']
    driver_obj = Operadriver().start_driver()
    driver_desktop = Operadriver().opera(driver_obj, path[2])
    reboot_counter = 0
    for region in regions:
        for search_request in search_requests:
            url_with_ads = ulr_builder(region, object_parse, search_request)
            driver_desktop.get(url_with_ads)
            sleep(randint(1, 4))
            last_page = int(find_last_page(driver_desktop)) + 1
            repeat_counter = 0
            for i in range(0, last_page):
                randint(1, 2)
                url_ = url_with_ads + str(i)
                driver_desktop.get(url_)
                reboot_counter += 1
                if check_baning(driver_desktop):
                    driver_desktop.quit()
                    driver_desktop = Operadriver().opera(driver_obj, path[2])
                else:
                    get_urls(driver_desktop, region, repeat_counter, search_request)
                if repeat_counter >= 5:
                    print(f'unique ads ended on {i} page, region {region}'
                          f'for urls {url_with_ads}')
                if reboot_counter > 20:
                    driver_desktop.quit()
                    driver_desktop = Operadriver().opera(driver_obj, path[2])


if __name__ == '__main__':
    main()