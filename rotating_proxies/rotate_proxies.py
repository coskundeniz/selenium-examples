import os
from itertools import cycle
from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import FirefoxOptions, ChromeOptions
from selenium.common.exceptions import WebDriverException
from webdriver_setup import get_webdriver_for


os.environ["WDM_LOG_LEVEL"] = "0"


def get_proxies():
    """Return list of proxies that are elite proxy and has https support

    :rtype: list
    :returns: List of proxies
    """

    url = "https://free-proxy-list.net/"

    response = requests.get(url)
    parsed_page = BeautifulSoup(response.content, "html.parser")

    ip_table = parsed_page.find(id="list")
    rows = ip_table.select("tbody > tr")

    # filter proxies whose last checked time is less than 1 hour
    rows_for_last_hour = [row for row in rows if "hour" not in row.select("td:last-child")[0].text]

    proxies = []

    for row in rows_for_last_hour:

        anonymity = row.select("td:nth-child(5)")[0].text
        https_support = row.select("td:nth-child(7)")[0].text

        if "elite" in anonymity and https_support == "yes":
            host = row.select("td:first-child")[0].text
            port = row.select("td:nth-child(2)")[0].text
            proxy = f"{host}:{port}"
            proxies.append(proxy)

    return proxies


def setup_proxy(browser, proxy):
    """Make proxy settings for the given browser

    :type browser: str
    :param browser: Name of the browser
    :type proxy: str
    :param proxy: Proxy string in the host:port form
    :rtype: FirefoxOptions or DesiredCapabilities
    :returns: FirefoxOptions for Firefox browser, capabilities for Chrome browser
    """

    print(f"Switching proxy to {proxy}...")

    if browser == "firefox":
        host = proxy.split(":")[0]
        port = proxy.split(":")[1]

        firefox_options = FirefoxOptions()
        firefox_options.set_preference("network.proxy.type", 1)  # 1 for MANUAL
        firefox_options.set_preference("network.proxy.http", host)
        firefox_options.set_preference("network.proxy.http_port", int(port))
        firefox_options.set_preference("network.proxy.ssl", host)
        firefox_options.set_preference("network.proxy.ssl_port", int(port))

        return firefox_options

    elif browser == "chrome":
        proxy_config = Proxy()
        proxy_config.proxy_type = ProxyType.MANUAL
        proxy_config.http_proxy = proxy
        proxy_config.ssl_proxy = proxy

        capabilities = DesiredCapabilities.CHROME.copy()
        proxy_config.add_to_capabilities(capabilities)

        return capabilities

    else:
        raise SystemExit("Invalid browser! Should be firefox or chrome.")


def create_webdriver(browser, proxy_config):
    """Create webdriver instance for the given browser and proxy setting

    :type browser: str
    :param browser: Name of the browser
    :type proxy_config: FirefoxOptions or DesiredCapabilities
    :param proxy_config: Proxy configuration
    :rtype: selenium.webdriver
    :returns: Firefox or Chrome webdriver instance
    """

    if browser == "firefox":
        firefox_options = proxy_config
        firefox_options.headless = True
        driver = get_webdriver_for(browser, options=firefox_options)

    elif browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.headless = True
        driver = get_webdriver_for(
            browser, options=chrome_options, desired_capabilities=proxy_config
        )

    return driver


def make_request_with_proxy(browser, proxy_config):
    """Make a request to check new IP

    Skip if connection fails.

    :type browser: str
    :param browser: Name of the browser
    :type proxy_config: FirefoxOptions or DesiredCapabilities
    :param proxy_config: Proxy configuration
    """

    driver = create_webdriver(browser, proxy_config)

    sleep(1)

    try:
        driver.get("https://www.myip.com/")
        print(f"IP: {driver.find_element(By.ID, 'ip').text}")

    except WebDriverException:
        print("Connection error! Skipping...")

    driver.quit()


def main():

    proxies = get_proxies()
    proxy_pool = cycle(proxies)

    browser = "chrome"

    for _ in range(5):
        proxy = next(proxy_pool)
        proxy_config = setup_proxy(browser, proxy)
        make_request_with_proxy(browser, proxy_config)


if __name__ == "__main__":

    main()
