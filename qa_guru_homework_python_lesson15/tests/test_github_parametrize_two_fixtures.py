import pytest
from selene import browser, be
from selenium.webdriver.common.by import By

base_url = "https://github.com/"
mobile_locator = (By.XPATH, "//*[contains(@class, 'HeaderMenu-link HeaderMenu-button ')]")
desktop_locator = (By.XPATH, "//*[contains(@class, 'HeaderMenu-link--sign-in')]")


def test_parametrize_window_mobile(browser_mobile):
    browser.open(base_url)
    browser.element(mobile_locator).should(be.visible).click()


def test_parametrize_window_desktop(browser_desktop):
    browser.open(base_url)
    browser.element(desktop_locator).should(be.visible).click()


@pytest.mark.parametrize("browser_desktop_and_mobile", [(1920, 1080), (1270, 500)], indirect=True,
                         ids=["1920*1080", "1270*500"])
def test_parametrize_window_general_fixture_desktop(browser_desktop_and_mobile):
    browser.open(base_url)
    browser.element(desktop_locator).should(be.visible).click()


@pytest.mark.parametrize("browser_desktop_and_mobile", [(390, 844), (430, 932)], indirect=True,
                         ids=["390*844", "430*932"])
def test_parametrize_window_general_fixture_mobile(browser_desktop_and_mobile):
    browser.open(base_url)
    browser.element(mobile_locator).should(be.visible).click()


def test_parametrize_desktop_skip(browser_desktop_and_mobile_skip):
    if browser_desktop_and_mobile_skip == 'desktop':
        pytest.skip(reason="Это десктопное расширение, скипаем тест")

    browser.open(base_url)
    browser.element(mobile_locator).should(be.visible).click()


def test_parametrize_mobile_skip(browser_desktop_and_mobile_skip):
    if browser_desktop_and_mobile_skip == 'mobile':
        pytest.skip(reason="Это мобильное расширение, скипаем тест")
    else:
        browser.open(base_url)
        browser.element(desktop_locator).should(be.visible).click()

