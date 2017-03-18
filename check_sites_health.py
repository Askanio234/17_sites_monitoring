import os
import datetime
import argparse
import requests
import whois


ONE_MONTH = datetime.timedelta(days=30)


def load_text_file(path):
    if os.path.exists(path):
        with open(path, "r") as file_handler:
            return file_handler.readlines()


def load_urls(file):
    return [line.strip() for line in file]


def is_server_respond_with_200(url):
    request = requests.get(url)
    return request.status_code == 200


def get_domain_expiration_date(url):
    if "https://www." in url:
        domain_name = url.replace("https://www.", "")
    elif "http://www." in url:
        domain_name = url.replace("http://www.", "")
    else:
        domain_name = url
    request = whois.whois(domain_name)
    if type(request.expiration_date) is list:
        return request.expiration_date[0]
    return request.expiration_date


def is_domain_expiration_date_ok(exp_date, today, timedelta):
    return (exp_date - timedelta) >= today


def parse_criteria(expiration_status, response_status):
    if expiration_status and response_status:
        return "Ok!"
    else:
        return "NOT Ok! attention is required!"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="Путь до файла с url")
    args = parser.parse_args()
    file_with_urls = load_text_file(args.filepath)
    if file_with_urls is not None:
        today = datetime.datetime.today()
        urls = load_urls(file_with_urls)
        for url in urls:
            expiration_status = is_domain_expiration_date_ok(
                                            get_domain_expiration_date(url),
                                            today,
                                            ONE_MONTH)
            response_status = is_server_respond_with_200(url)
            print("{} статус - {}".format(url, parse_criteria(
                                                            expiration_status,
                                                            response_status)))
    else:
        print("Неккоректный путь до файла")
