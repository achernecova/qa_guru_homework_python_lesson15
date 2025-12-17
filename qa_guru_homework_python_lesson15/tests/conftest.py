# import os
#
# import pytest
# from dotenv import load_dotenv
# from selene import browser
# from selenium.webdriver.chrome.options import Options

#
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# DEFAULT_BROWSER_VERSION = "127.0"
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browserVersion",
#         help="Версия браузера в котором будут запущены тесты",
#         default="127.0",
#     )
#
#
# @pytest.fixture(scope="session", autouse=True)
# def load_env():
#     load_dotenv()
#
# @pytest.fixture(scope="function", autouse=True)
# def driver(request):
#     _browserVersion = request.config.getoption("--browserVersion")
#     _browserVersion = (
#         _browserVersion if _browserVersion != "" else DEFAULT_BROWSER_VERSION
#     )
#     options = Options()
#     options.set_capability("browserName", "chrome")
#     options.set_capability("browserVersion", _browserVersion)
#     options.set_capability("pageLoadStrategy", "normal")
#     # options.add_argument("--window-size=1280,900")
#     options.add_argument("--start-maximized")
#     options.set_capability("selenoid:options", {"enableVNC": True, "enableVideo": True})
#
#     login = os.getenv("LOGIN")
#     password = os.getenv("PASSWORD")
#     host_selenoid = os.getenv("HOST")
#
#     browser.config.driver_remote_url = f"https://{login}:{password}@{host_selenoid}"
#     browser.config.driver_options = options
#     browser.config.timeout = 6
#
#     yield
#
#     # browser.driver.maximize_window()
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_html(browser)
#     attach.add_video(browser)
#
#     browser.quit()
# @pytest.fixture(scope="function", autouse=True)
# def driver_setup():
#     '''Фикстура для запуска локально'''
#     chrome_options = Options()
#     # chrome_options.add_argument("--headless")
#     # chrome_options.page_load_strategy = "none"
#     chrome_options.add_argument("--start-maximized")
#
#     # Todo - для firefox другие переменные передаются в расширение:
#     # chrome_options.add_argument("--width=1920")
#     # chrome_options.add_argument("--height=1080")
#     driver = webdriver.Chrome(options=chrome_options)
#
#     # Передаем драйвер в Selene
#     browser.config.driver = driver
#
#     yield driver
#     browser.driver.maximize_window()
#     # attach.add_screenshot(browser)
#     # attach.add_logs(browser)
#     # attach.add_html(browser)
#     # attach.add_video(browser)
#     browser.quit()

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions


@pytest.fixture(params=["Chrome", "Firefox", "Safari"])
def browser_setup(request):
    if request.param == "Chrome":
        '''Фикстура для запуска локально'''
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # chrome_options.page_load_strategy = "none"
        # chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
        browser.config.driver = driver

    elif request.param == "Firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        # В Firefox --start-maximized не работает. Нашла на каком-то форуме
        # options.add_argument("--kiosk")
        driver = webdriver.Firefox(options=options)
        browser.config.driver = driver

    elif request.param == "Safari":
        options = SafariOptions()
        driver = webdriver.Safari(options=options)
        # Safari не поддерживает аргументы запуска, максимизируем через драйвер
        # driver.maximize_window()
        browser.config.driver = driver

    yield driver
    browser.quit()


@pytest.fixture(scope="function", params=[(390, 844), (430, 932), (360, 740)], ids=["390*844", "430*932", "360*740"])
def browser_mobile(request):
    width, height = request.param
    chrome_options = Options()
    chrome_options.add_argument(f"--window-size={width},{height}")
    driver = webdriver.Chrome(options=chrome_options)
    browser.config.driver = driver
    yield driver
    browser.quit()


@pytest.fixture(scope="function", params=[(1920, 1080), (1270, 500), (1366, 768)],
                ids=["1920*1080", "1270*500", "1366*768"])
def browser_desktop(request):
    width, height = request.param
    chrome_options = Options()
    chrome_options.add_argument(f"--window-size={width},{height}")
    driver = webdriver.Chrome(options=chrome_options)
    browser.config.driver = driver
    yield driver
    browser.quit()


@pytest.fixture(scope="function", params=[(1920, 1080), (1270, 500), (390, 844), (430, 932)],
                ids=["1920*1080", "1270*500", "390*844", "430*932"])
def browser_desktop_and_mobile(request):
    width, height = request.param
    chrome_options = Options()
    chrome_options.add_argument(f"--window-size={width},{height}")
    driver = webdriver.Chrome(options=chrome_options)
    browser.config.driver = driver
    yield driver
    browser.quit()


@pytest.fixture(scope="function", params=[(1920, 1080), (1270, 500), (390, 844), (430, 932)],
                ids=["1920*1080", "1270*500", "390*844", "430*932"])
def browser_desktop_and_mobile_skip(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 900:
        chrome_options = Options()
        chrome_options.add_argument(f"--window-size={width},{height}")
        driver = webdriver.Chrome(options=chrome_options)
        browser.config.driver = driver
        yield 'desktop'
    else:
        chrome_options = Options()
        chrome_options.add_argument(f"--window-size={width},{height}")
        driver = webdriver.Chrome(options=chrome_options)
        browser.config.driver = driver
        yield 'mobile'
    browser.quit()
