import unittest
import Couriersfile
from unittest.mock import patch, call

@patch('builtins.input',side_effect=[' '])
def test_courier_menu_func_if_no_option(mock_input):
    expected = True
    con =''
    courier_menu_text = ''
    courier_update_menu_text = ''
    actual = Couriersfile.courier_menu_func(con,courier_menu_text, courier_update_menu_text)

    assert actual == expected

@patch('builtins.input',side_effect=['0'])
def test_courier_menu_func_if_exit(mock_input):
    expected = False
    con =''
    courier_menu_text = ''
    courier_update_menu_text = ''
    actual = Couriersfile.courier_menu_func(con,courier_menu_text, courier_update_menu_text)

    assert actual == expected


@patch('builtins.input',side_effect=['1'])
@patch('Couriersfile.view_courier')
def test_courier_menu_func_choice_1(mock_view_product,mock_input):
    expected = True
    con =''
    courier_menu_text = ''
    courier_update_menu_text = ''
    actual = Couriersfile.courier_menu_func(con,courier_menu_text, courier_update_menu_text)
    assert actual == expected
    mock_view_product.assert_called_with(con)

@patch('builtins.input',side_effect=['2'])
@patch('Couriersfile.add_courier')
def test_courier_menu_func_choice_2(mock_add_products,mock_input):
    expected = True
    con =''
    courier_menu_text = ''
    courier_update_menu_text = ''
    actual = Couriersfile.courier_menu_func(con,courier_menu_text, courier_update_menu_text)
    assert actual == expected
    mock_add_products.assert_called_with(con)

@patch('builtins.input',side_effect=['3'])
@patch('Couriersfile.update_courier')
def test_courier_menu_func_choice_3(mock_update_products,mock_input):
    expected = True
    con =''
    courier_menu_text = ''
    courier_update_menu_text = ''
    actual = Couriersfile.courier_menu_func(con,courier_menu_text, courier_update_menu_text)
    assert actual == expected
    mock_update_products.assert_called_with(con,courier_update_menu_text)


@patch('builtins.input',side_effect=['4'])
@patch('Couriersfile.delete_courier')
def test_courier_menu_func_choice_4(mock_delete_products,mock_input):
    expected = True
    con =''
    courier_menu_text = ''
    courier_update_menu_text = ''
    actual = Couriersfile.courier_menu_func(con,courier_menu_text, courier_update_menu_text)
    assert actual == expected
    mock_delete_products.assert_called_with(con)
