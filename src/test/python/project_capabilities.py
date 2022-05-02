class ProjectCapabilities:

    @staticmethod
    def base_capabilities(browser) -> dict:
        base_caps = {"newCommandTimeout": 1800,
                     "browserName": browser,
                     "screenResolution": "1024x768"}
        return base_caps
