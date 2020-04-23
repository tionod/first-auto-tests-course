link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_the_basket_button(browser):
    browser.get(link)
    # time.sleep(30)
    basket_btn = browser.find_element_by_css_selector("#add_to_basket_form > button")
    assert basket_btn.text, "Element not found"
    print(f'Найдена кнопка, "{basket_btn.text}"')
