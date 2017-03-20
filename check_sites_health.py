import os
import datetime
import argparse
import urllib.parse
import requests
import whois


ONE_MONTH = datetime.timedelta(days=30)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="Путь до файла с url")
    return parser.parse_args()


def load_text_file(path):
    if os.path.exists(path):
        with open(path, "r") as file_handler:
            return file_handler.readlines()


def load_urls(file):
    return [line.strip() for line in file]


def is_server_respond_with_200(url):
    request = requests.get(url)
    return request.status_code == 200


def parse_domain_name(url):
    return urllib.parse.urlparse(url).netloc[4:]


def get_domain_expiration_date(domain_name):
    request = whois.whois(domain_name)
    if type(request.expiration_date) is list:
        return request.expiration_date[0]
    return request.expiration_date


def is_domain_expiration_date_ok(exp_date, today, timedelta):
    if exp_date is not None:
        return (exp_date - timedelta) >= today
    else:
        return False


def print_results(urls):
    today = datetime.datetime.today()
    for url in urls:
        domain_name = parse_domain_name(url)
        response_status = is_server_respond_with_200(url)
        expiration_status = is_domain_expiration_date_ok(
                                    get_domain_expiration_date(domain_name),
                                    today,
                                    ONE_MONTH)
        print("Статус {} : ответ от сервера - {response}, "
                "оплачен на месяц - "
                "{expires}".format(url,
                            response="Ok" if response_status else "Not Ok",
                            expires="Ok" if expiration_status else "Not Ok"))


if __name__ == '__main__':
    args = parse_args()
    file_with_urls = load_text_file(args.filepath)
    if file_with_urls is not None:
        today = datetime.datetime.today()
        urls = load_urls(file_with_urls)
        print_results(urls)
    else:
        print("Неккоректный путь до файла")
