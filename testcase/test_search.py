from page.app import App


class TestSearch:
    def setup(self):
        self.search = App().start().main().goto_market().goto_search()

    def test_Search(self):
        self.search.search("阿里巴巴-SW")
        assert self.search.is_choose("阿里巴巴-SW")
