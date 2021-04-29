import pytest

from animal.wikipedia.api import AnimalDataProcessing


@pytest.fixture()
def scrape_cat():
    return AnimalDataProcessing('cat')


@pytest.fixture()
def scrape_dog():
    return AnimalDataProcessing('dog')


def test_scrape_cat(scrape_cat):
    assert len(scrape_cat.scraper()) > 0


def test_scrape_dog(scrape_dog):
    print(scrape_dog.scraper())
    assert len(scrape_dog.scraper()) > 0
