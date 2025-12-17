import time

import pytest



# @pytest.mark.parametrize("browser, version",
#                          [("Chrome", "94-rci1:build385043541"), ("Firefox", 85), ("Safari", 13.2)],
#                          ids=["Chrome", "Firefox", "Safari"]
#                          )
# @pytest.mark.parametrize("test_role",['manager', 'guest', 'admin'])
# def test_parameters(browser, version, test_role):
#     assert browser in ["Chrome", "Firefox", "Safari"]


# @pytest.mark.parametrize("browser",
#                          [
#                           pytest.param("Firefox"),
#                           pytest.param("Chrome", id='Chrome'),
#                           pytest.param("Safari", marks=[pytest.mark.xfail(reason="Need to fix this")]),
#                           ]
#                          )
# def test_parameters_new(browser):
#     assert browser in ["Chrome", "Firefox", "Safari"]






@pytest.mark.parametrize("browser_setup", ["Firefox", "Chrome"], indirect=True)
def test_123(browser_setup):
    pass



@pytest.fixture(scope='session')
def user_():
    time.sleep(5)

# @pytest.mark.slow
# def test_first(browser):
#     time.sleep(5)


# @pytest.mark.fast
# def test_second(browser):
#     time.sleep(1)
#
# @pytest.mark.skip(reason="TASK-123 тест нестабилен. Время от времени не хватает таймаута")
# def test_user():
#     user1 = random.randint(0, 100)
#     user2 = random.randint(0, 100)
#     user3 = random.randint(0, 100)
#     user4 = random.randint(0, 100)
#     assert user1 == user2
