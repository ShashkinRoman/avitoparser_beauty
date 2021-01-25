import json
import random
from time import sleep
from beautybox.models import Region, Ad, Url
from beautybox.webdriver_start import Operadriver, path
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def price(driver):
    try:
        price_obj = driver.find_element_by_class_name('price-value-string')
        price_ = price_obj.find_element_by_tag_name('span').get_attribute('content')
    except:
        price_ = None
    return price_


def title_ads(driver):
    try:
        title = driver.find_element_by_class_name('title-info-title-text').text
    except:
        title = None
    return title


def created_ads(driver):
    created = driver.find_element_by_class_name('title-info-metadata-item-redesign').text
    return created


def owner_ads(driver):
    try:
        name_lines = driver.find_element_by_class_name('seller-info-prop').find_elements_by_tag_name('div')
        name = list(set([line.text for line in name_lines]))
    except:
        name = None
    return name


def contact_name(driver):
    try:
        contact_name_lines = driver.find_element_by_class_name('seller-info-prop_short_margin').find_elements_by_tag_name('div')
        name_line = list(set([line.text for line in contact_name_lines]))
    except:
        name_line = None
    return name_line


def param_list(driver):
    try:
        param_box = driver.find_element_by_class_name('item-params-list').find_elements_by_class_name('item-params-list-item')
        params_list = []
        [params_list.append(param.text) for param in param_box]
    except:
        params_list = None
    return params_list


def address_info(driver):
    address_box = driver.find_element_by_class_name('item-address').text
    return address_box


def description_info(driver):
    try:
        description = driver.find_element_by_class_name('item-description-text').text
    except NoSuchElementException:
        description = None
    return description


def phone_info(driver_mobile, url):
    driver_mobile.get(url)
    sleep(2)
    button = driver_mobile.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]/a')

    if button.text == 'Позвонить':
        button.click()
        sleep(3)
        phone = driver_mobile.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div[1]/span[2]').text[1:]
    else:
        if button.text == 'Написать':
            phone = None
            print('net nomera')
        else:
            phone = 'undefined error'
            print(phone)
    return phone


def driver_reboot(driver_desktop, driver_mobile, driver_obj):
    driver_mobile.quit()
    driver_desktop.quit()
    return Operadriver().opera(driver_obj, path[2]), Operadriver().opera(driver_obj, path[3])


def main():
    urls = Url.objects.filter(parsing_status=2).order_by('-date')
    driver_obj = Operadriver().start_driver()
    driver_desktop = Operadriver().opera(driver_obj, path[2])
    driver_mobile = Operadriver().opera(driver_obj, path[3])
    counter_for_reboot = 0
    for url_ in urls:
        url = url_.url
        region = url_.region
        driver_desktop.get(url)
        sleep(random.randint(1, 3))
        try:  # check ad removed from publication
            a = 1/0
            check_publication = driver_desktop.find_element_by_class_name(
                'a10a3f92e9--container--1In69').text == 'Объявление снято с публикации'
            url_.parsing_status = 4
            print(f"{url}, ad removed from publication)")
            url_.save()
        except:
            try:
                Ad.objects.create(
                    price=price(driver_desktop),
                    # type_ads=type_ads,
                    title=title_ads(driver_desktop),
                    created=created_ads(driver_desktop),
                    owner_info=owner_ads(driver_desktop),
                    contact_name=contact_name(driver_desktop),
                    address=address_info(driver_desktop),
                    description=description_info(driver_desktop),
                    region=region,
                    phone=phone_info(driver_mobile, url),
                    url=url_
                )
                url_.parsing_status = 1
                url_.save()
                if counter_for_reboot > 50:
                    driver_desktop, driver_mobile = driver_reboot(driver_desktop, driver_mobile, driver_obj)
                    counter_for_reboot = 0
                    print('driver rebooted')
            except TimeoutException:
                driver_desktop, driver_mobile = driver_reboot(driver_desktop, driver_mobile, driver_obj)
            except Exception as e:
                print(f"{url}, exception: {e}")
                url_.parsing_status = 3
                url_.save()
            counter_for_reboot += 1


if __name__ == '__main__':
    main()
