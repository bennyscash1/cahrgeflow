import time
from typing import Optional
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError


class WeblocatoreFunction:
    DEFAULT_TIMEOUT_SECONDS = 20.0  # seconds
    DEFAULT_RETRIES = 3
    DEFAULT_RETRY_DELAY_SECONDS = 0.5

    def __init__(self, page: Page, timeout_seconds: Optional[float] = None):
        self.page = page
        if timeout_seconds is not None:
            self.DEFAULT_TIMEOUT_SECONDS = float(timeout_seconds)

    def _timeout_ms(self) -> int:
        return int(self.DEFAULT_TIMEOUT_SECONDS * 1000)

    def is_element_found(self, selector: str) -> bool:
        try:
            visible = self.page.is_visible(selector, timeout=self._timeout_ms())
            if not visible:
                print(f"Element '{selector}' found in the DOM but not visible.")
            return visible
        except PlaywrightTimeoutError:
            print(f"Element '{selector}' not found within {self.DEFAULT_TIMEOUT_SECONDS} seconds")
            return False

    def wait_for_element_visibility(
        self,
        selector: str,
        retries: int = DEFAULT_RETRIES,
        delay_seconds: float = DEFAULT_RETRY_DELAY_SECONDS
    ) -> bool:
        for attempt in range(1, retries + 1):
            if self.is_element_found(selector):
                return True

            if attempt < retries:
                print(f"Retry {attempt}/{retries} for element '{selector}'")
                time.sleep(delay_seconds)

        print(f"Element '{selector}' not visible after {retries} retries")
        return False

    def click(self, selector: str) -> None:
        if self.wait_for_element_visibility(selector):
            self.page.click(selector)
            return

        raise AssertionError(
            f"Click failed: element '{selector}' not visible within "
            f"{self.DEFAULT_TIMEOUT_SECONDS}s (retries={self.DEFAULT_RETRIES})"
        )

    def fill_text(self, selector: str, text: str) -> None:
        if self.wait_for_element_visibility(selector):
            self.page.fill(selector, text)
            return

        raise AssertionError(
            f"Fill failed: element '{selector}' not visible within "
            f"{self.DEFAULT_TIMEOUT_SECONDS}s (retries={self.DEFAULT_RETRIES})"
        )

    def switch_to_frame(self, frame_selector: str):
        frame = self.page.frame_locator(frame_selector)
        return frame  # caller uses returned frame.locator(...)

    def is_displayed(self, selector: str) -> bool:
        return self.wait_for_element_visibility(selector)

    def alert_ok(self) -> None:
        self.page.on("dialog", lambda dialog: dialog.accept())

    def get_text_from_at(self, selector: str, attribute: str):
        if not self.wait_for_element_visibility(selector):
            raise AssertionError(
                f"get_attribute failed: element '{selector}' not visible within {self.DEFAULT_TIMEOUT_SECONDS}s"
            )
        return self.page.get_attribute(selector, attribute)
