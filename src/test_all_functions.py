import unittest
from all_functions import add_products,view_products
from all_functions import Product

from unittest.mock import patch, call

@patch('builtins.input',side_effect=['coke','1.7','25', ' '])
def test_add_products(mock_input):
    products_list = []
    product = Product(float('1.7'),25,'coke')
    expected = [product]

    actual = add_products(products_list)
    
    


    assert expected[0].__dict__ == actual[0].__dict__


@patch('builtins.input', side_effect=[' '])
@patch('builtins.print')
def test_view_products(mock_print, mock_input):
    products = [Product(float('1.7'),25,'coke'),Product(float('1'),50,'bottle')]
    ex_args1 = 'Product name: coke\nPrice: £1.7\nQuantity: 25\nIndex value: 0\n'
    ex_args2 = 'Product name: bottle\nPrice: £1.0\nQuantity: 50\nIndex value: 1\n'
    view_products(products)

    mock_print.assert_has_calls([call(ex_args1), call(ex_args2)], any_order=True)
