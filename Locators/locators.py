class ElementLocators:

    chrome_driver = ".\\Driver\\chromedriver.exe"

    # login page
    login_xpath = "//a[@id='nav-link-accountList']"
    email_field = "email"
    continue_button = "a-button-inner"
    password_field = "password"
    warning_xpath = "//div[@class='a-box-inner a-alert-container']//h4[@class='a-alert-heading']"

    # Homepage
    logo_xpath = "//a[@class='a-link-nav-icon']"
    search_id = "twotabsearchtextbox"
    search_term = " Home Gardeners’ Guide Indian Garden Flowers "
    search_button_id = "nav-search-submit-text"
    product_xpath = "Indian Garden Flowers"

    # pdp
    # price_xpath = "//span[@class='a-size-base a-color-price a-color-price']"
    price_xpath = "//span[@class='a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P' or @class = 'a-size-medium a-color-base sc-price sc-white-space-nowrap sc-product-price a-text-bold']"
    add_to_cart_xpath = "//input[@title='Add to Shopping Cart']"
    stock_xpath = "//span[@class='a-size-medium a-color-success']"
    # product_title_xpath = "(//span[contains(text(),'Indian Garden Flowers')])[1]"
    mini_cart_id = "nav-cart"
    product_title_xpath = "(//span[contains(text(),'Indian Garden Flowers')])[1or @class='a-size-medium a-color-base sc-price sc-white-space-nowrap sc-product-price a-text-bold'][1]"
