import datetime
from django.test import TestCase

from example.widgets.models import Widget
from example.customers.models import Customer
from example.purchases.models import Purchase


class WidgetTests(TestCase):

    def setUp(self):
        basic_obj = Widget(name='testwidget',
                           color='Black',
                           size='Small',
                           shape='Rectangle')
        basic_obj.save()
        dummy_obj = Widget(name='dummywidget',
                           color='Green',
                           size='Medium',
                           shape='Ellipse')
        dummy_obj.save()

    def test_get_name(self):
        obj = Widget.objects.get(name='testwidget')
        self.assertEqual(obj.name, 'testwidget')
        self.assertEqual(str(obj), 'testwidget')


class PurchaseTests(TestCase):

    def setUp(self):
        widg1 = Widget(name='testwidget',
                       color='Black',
                       size='Small',
                       shape='Rectangle')
        widg1.save()
        widg2 = Widget(name='dummywidget',
                       color='Green',
                       size='Medium',
                       shape='Ellipse')
        widg2.save()
        cust = Customer.objects.create(full_name='testcust',
                                       state='Florida',
                                       gender='M',
                                       age='29')
        purch1 = Purchase(customer=cust)
        purch1.save()
        purch1.items.add(widg1)
        purch1.items.add(widg2)
        purch1.save()

    def test_customer_methods(self):
        cust = Customer.search('testcust').first()
        pur = Purchase.objects.first()
        self.assertEqual(cust.purchase_set.first(), pur)

        self.assertEqual(cust.full_name, 'testcust')
        self.assertEqual(cust.state, 'Florida')
        self.assertEqual(cust.gender, 'M')
        self.assertEqual(cust.age, 29)
