from ..data import DataBun


class TestBun:

    def test_get_name_success(self, get_bun):
        bun = get_bun
        assert bun.get_name() == DataBun.BUN_NAME

    def test_get_price_success(self, get_bun):
        bun = get_bun
        assert bun.get_price() == DataBun.BUN_PRICE
