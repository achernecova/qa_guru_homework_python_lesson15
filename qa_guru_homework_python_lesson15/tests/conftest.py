import pytest


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
