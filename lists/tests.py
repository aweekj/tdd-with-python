import re
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from lists.views import home_page
from lists.models import Item


class HomePageTest(TestCase):

    def remove_csrf(self, origin):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex, '', origin)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = self.remove_csrf(render_to_string('home.html'))
        response_decode = self.remove_csrf(response.content.decode())

        self.assertEqual(response_decode, expected_html)



    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

    def test_saving_a_post_request(self):
        self.client.post(
            '/list/new',
            data={'item_text': 'A new item'}
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item')

    def test_redirects_after_post(self):
        response = self.client.post(
            '/list/new',
            data={'item_text': 'A new item'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['location'],
            '/lists/the-only-list-in-the-world/'
        )


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'First item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Second item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'First item')
        self.assertEqual(second_saved_item.text, 'Second item')