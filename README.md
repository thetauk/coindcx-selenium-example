# CoinDCX Sample Selenium Tests

Note: Tests works only with `python >= 3.0`



## Prerequisites

Install the Chromedriver version to correspond to the latest version of Chrome. On macOS you can conveniently install Chromedriver through homebrew:

```bash
brew install --cask chromedriver
```

 

## Running the example test

```bash
# Install the dependencies
pip install -r src/test/python/requirements.txt

# Run the tests
python -m unittest src.test.python.tests.Tests
```
