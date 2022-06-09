import unittest
from all_functions import add_products, view_products, view_courier, add_products
from all_functions import Product, Couriers

from unittest.mock import patch, call


@patch('builtins.input', side_effect=['coke', '1.7', '25', ' '])
def test_add_products(mock_input):
    products_list = []
    product = Product(float('1.7'), 25, 'coke')
    expected = [product]

    actual = add_products(products_list)

    assert expected[0].__dict__ == actual[0].__dict__


@patch('builtins.input', side_effect=[' '])
@patch('builtins.print')
def test_view_products(mock_print, mock_input):
    products = [Product(float('1.7'), 25, 'coke'),
                Product(float('1'), 50, 'bottle')]
    ex_args1 = 'Product name: coke\nPrice: £1.7\nQuantity: 25\nIndex value: 0\n'
    ex_args2 = 'Product name: bottle\nPrice: £1.0\nQuantity: 50\nIndex value: 1\n'
    view_products(products)

    mock_print.assert_has_calls(
        [call(ex_args1), call(ex_args2)], any_order=True)


@patch('builtins.input', side_effect=[' '])
@patch('builtins.print')
def test_view_couriers(mock_print, mock_input):
    couriers = [Couriers('test1', 'test1_no', 'test1_delivery'), Couriers(
        'test2', 'test2_no', 'test2_delivery')]
    ex_args1 = 'Courier name: test1\nCourier phone number: test1_no\nCourier vehicle: test1_delivery\nIndex value: 0\n'
    ex_args2 = 'Courier name: test2\nCourier phone number: test2_no\nCourier vehicle: test2_delivery\nIndex value: 1\n'
    view_courier(couriers)

    mock_print.assert_has_calls(
        [call(ex_args1), call(ex_args2)], any_order=True)


@patch('builtins.input', side_effect=['name', '1.2', '10', ' '])
@patch('builtins.print')
def test_add_products_same(mock_print, mock_input):
    products = [Product(1.2, 12, 'name')]
    ex_args = '\nThis product already exists in your list\n'
    add_products(products)

    mock_print.assert_called_with(ex_args)



