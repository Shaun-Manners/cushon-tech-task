from selenium import webdriver


def chrome_browser():
    options = get_default_chrome_options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    driver.delete_all_cookies()
    driver.execute_script('window.localStorage.clear()')
    driver.execute_script('window.sessionStorage.clear()')
    return driver


def get_default_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument("--user-data-dir='/tmp/chrome_root_data'")

    # Docker container /dev/shm too small, so disable its use for now.
    # Another option is to add a mount, but not keen on this solution.
    options.add_argument("disable-dev-shm-usage")

    # Non standard window size, but means the whole page gets
    # shown in the screenshot. Great while debugging.
    options.add_argument("window-size=1920,1920")

    # Resolves a permissions issue.
    options.add_argument("user-data-dir=/tmp")

    # Docker doesn't have a display, so run in headless.
    options.add_argument("headless")
    options.add_argument("disable-gpu")

    # Incognito to prevent cache/cookies from crossing over between tests.
    options.add_argument("incognito")

    # Output chromedriver logs to logs directory
    options.add_argument("log-file=./logs/chromedriver.log")

    return options
