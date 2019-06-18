class MyXpaths():
    catalog_xpaths = {
        'smart/telephone': '//li[@class = "level0 nav-1 level-top first"]//a[@href="//allo.ua/ru/mobilnye-telefony-i-sredstva-svyazi/"]',
        'tv': '//li[@class = "level0 nav-2 level-top"]//a[@href = "//allo.ua/ru/televizory-i-mediapleery/"]',
        'acoustics': '//li[@class = "level0 nav-3 level-top"]//a[@href="//allo.ua/ru/naushniki-i-akustika/"]',
        'tablets': '//li[@class = "level0 nav-4 level-top"]//a[@href="//allo.ua/ru/planshety-i-gadzhety/"]',
        'apple': '//li[@class = "level0 nav-5 level-top"]//a[@href="//allo.ua/ru/aksessuary-apple/"]',
        'xiaomi': '//li[@class = "level0 nav-6 level-top"]//a[@href="//allo.ua/ru/xiaomi-page/"]',
        'gadgets': '//li[@class = "level0 nav-7 level-top"]//a[@href="//allo.ua/ru/gadzhety/"]',
        'appliances': '//li[@class = "level0 nav-8 level-top"//a[@href="//allo.ua/ru/bytovaya-tehnika/"]',
        'sports and health': '//li[@class = "level0 nav-9 level-top"]//a[@href="//allo.ua/ru/sport-i-zdorov-e/"]',
        'tourism and fishing': '//li[@class = "level0 nav-10 level-top"]//a[@href=//allo.ua/ru/turizm-i-rybalka/"]',
        'plumbing and repairs': '//li[@class = "level0 nav-11 level-top"]//a[@href="//allo.ua/ru/santehnika-i-remont/"]',
        'house and garden': '//li[@class = "level0 nav-12 level-top"]//a[@href="//allo.ua/ru/dom-sad-remont/"]',
        "childen's goods": '//li[@class = "level0 nav-13 level-top"]//a[@href="//allo.ua/ru/tovary-dlja-detej/"]',
        'auto': '//li[@class = "level0 nav-14 level-top"]//a[@href="//allo.ua/ru/avtotovary/"]',
        'pjw': '//li[@class = "level0 nav-15 level-top"]//a[@href="//allo.ua/ru/chasy-i-ukrashenija/"]',
        'events and discounts': '//li[@class = "level0 nav-16 level-top"]//a[@href="//allo.ua/ru/events-and-discounts/"]'
    }
    def test_smart(self):
        a = '//li[@class = "level0 nav-1 level-top first"]//a[@href="//allo.ua/ru/mobilnye-telefony-i-sredstva-svyazi/"]'
        assert self.catalog_xpaths.get('smart/telephone') == a, 'Xpath incorrect'

    def test_tv(self):
        a = '//li[@class = "level0 nav-2 level-top"]//a[@href = "//allo.ua/ru/televizory-i-mediapleery/"]'
        assert self.catalog_xpaths.get('tv') == a, 'Xpath incorrect'

    def test_acoustics(self):
        a = '//li[@class = "level0 nav-3 level-top"]//a[@href="//allo.ua/ru/naushniki-i-akustika/"]'
        assert self.catalog_xpaths.get('acoustics') == a, 'Xpath incorrect'

    def test_tablets(self):
        a = '//li[@class = "level0 nav-4 level-top"]//a[@href="//allo.ua/ru/planshety-i-gadzhety/"]'
        assert self.catalog_xpaths.get('tablets') == a, 'Xpath incorrect'

    def test_apple(self):
        a = '//li[@class = "level0 nav-5 level-top"]//a[@href="//allo.ua/ru/aksessuary-apple/"]'
        assert self.catalog_xpaths.get('apple') == a, 'Xpath incorrect'

    def test_xiaomi(self):
        a = '//li[@class = "level0 nav-6 level-top"]//a[@href="//allo.ua/ru/xiaomi-page/"]'
        assert self.catalog_xpaths.get('xiaomi') == a, 'Xpath incorrect'

    def test_gadgets(self):
        a = '//li[@class = "level0 nav-7 level-top"]//a[@href="//allo.ua/ru/gadzhety/"]'
        assert self.catalog_xpaths.get('gadgets') == a, 'Xpath incorrect'

    def test_appliance(self):
        a = '//li[@class = "level0 nav-8 level-top"//a[@href="//allo.ua/ru/bytovaya-tehnika/"]'
        assert self.catalog_xpaths.get('appliances') == a, 'Xpath incorrect'

    def test_s_and_h(self):
        a = '//li[@class = "level0 nav-9 level-top"]//a[@href="//allo.ua/ru/sport-i-zdorov-e/"]'
        assert self.catalog_xpaths.get('sports and health') == a, 'Xpath incorrect'

    def test_t_and_f(self):
        a = '//li[@class = "level0 nav-10 level-top"]//a[@href=//allo.ua/ru/turizm-i-rybalka/"]'
        assert self.catalog_xpaths.get('tourism and fishing') == a, 'Xpath incorrect'

    def test_p_and_r(self):
        a = '//li[@class = "level0 nav-11 level-top"]//a[@href="//allo.ua/ru/santehnika-i-remont/"]'
        assert self.catalog_xpaths.get('plumbing and repairs') == a, 'Xpath incorrect'

    def test_h_and_g(self):
        a = '//li[@class = "level0 nav-12 level-top"]//a[@href="//allo.ua/ru/dom-sad-remont/"]'
        assert self.catalog_xpaths.get('house and garden') == a, 'Xpath incorrect'

    def test_cd(self):
        a = '//li[@class = "level0 nav-13 level-top"]//a[@href="//allo.ua/ru/tovary-dlja-detej/"]'
        assert self.catalog_xpaths.get("childen's goods") == a, 'Xpath incorrect'

    def test_automob(self):
        a = '//li[@class = "level0 nav-14 level-top"]//a[@href="//allo.ua/ru/avtotovary/"]'
        assert self.catalog_xpaths.get('auto') == a, 'Xpath incorrect'

    def test_pjw(self):
        a = '//li[@class = "level0 nav-15 level-top"]//a[@href="//allo.ua/ru/chasy-i-ukrashenija/"]'
        assert self.catalog_xpaths.get('pjw') == a, 'Xpath incorrect'

    def test_e_and_d(self):
        a = '//li[@class = "level0 nav-16 level-top"]//a[@href="//allo.ua/ru/events-and-discounts/"]'
        assert self.catalog_xpaths.get('events and discounts') == a, 'Xpath incorrect'


test = MyXpaths()
print(test.test_smart())
print(test.test_acoustics())
print(test.test_apple())
print(test.test_appliance())
print(test.test_automob())
print(test.test_cd())
print(test.test_e_and_d())
print(test.test_h_and_g())
print(test.test_p_and_r())
print(test.test_pjw())
print(test.test_tablets())
print(test.test_gadgets())
print(test.test_s_and_h())
print(test.test_t_and_f())
print(test.test_tv())
print(test.test_xiaomi())
