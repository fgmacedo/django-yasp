# coding: utf-8

import pytest

from yasp.models import FlatPage, Menu


@pytest.mark.django_db
def test_url_of_page_without_menu():
    page = FlatPage.objects.create(slug='vision', title='Vision')
    assert page.get_absolute_url() == "/vision"


@pytest.mark.django_db
def test_url_of_page_with_menu():
    menu = Menu.objects.create(name='About us', slug='about-us')
    page = FlatPage.objects.create(menu=menu, slug='vision', title='Vision')
    assert page.get_absolute_url() == "/about-us/vision"


@pytest.mark.django_db
def test_url_of_external_page_without_menu():
    page = FlatPage.objects.create(
        slug='google', link='http://google.com', title='Google')
    assert page.get_absolute_url() == "http://google.com"


@pytest.mark.django_db
def test_url_of_external_page_with_menu():
    menu = Menu.objects.create(name='About us', slug='about-us')
    page = FlatPage.objects.create(
        menu=menu, slug='google', link='http://google.com', title='Google')
    assert page.get_absolute_url() == "http://google.com"
