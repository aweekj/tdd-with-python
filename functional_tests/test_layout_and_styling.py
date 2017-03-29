from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Edith visits to main page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She notice that the input box is at the middle of the window
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
