import unittest
import Ordersfile
from unittest.mock import patch, call

@patch('builtins.input',side_effect=[' '])
def test_order_menu_func_if_no_option(mock_input):
    expected = True
    con =''
    order_menu_text = ''
    order_update_menu_text = ''
    status_list = ''
    actual = Ordersfile.order_menu_func(con,order_update_menu_text, status_list, order_menu_text)

    assert actual == expected

@patch('builtins.input',side_effect=['0'])
def test_order_menu_func_if_exit(mock_input):
    expected = False
    con =''
    order_menu_text = ''
    order_update_menu_text = ''
    status_list = ''
    actual = Ordersfile.order_menu_func(con,order_update_menu_text, status_list, order_menu_text)

    assert actual == expected


@patch('builtins.input',side_effect=['1'])
@patch('Ordersfile.view_orders')
def test_order_menu_func_choice_1(mock_view_orders,mock_input):
    expected = True
    con =''
    order_menu_text = ''
    order_update_menu_text = ''
    status_list = ''
    actual = Ordersfile.order_menu_func(con,order_update_menu_text, status_list, order_menu_text)
    assert actual == expected
    mock_view_orders.assert_called_with(con)

@patch('builtins.input',side_effect=['2'])
@patch('Ordersfile.add_orders')
def test_orders_menu_func_choice_2(mock_add_orders,mock_input):
    expected = True
    con =''
    order_menu_text = ''
    order_update_menu_text = ''
    status_list = ''
    actual = Ordersfile.order_menu_func(con,order_update_menu_text, status_list, order_menu_text)
    assert actual == expected
    mock_add_orders.assert_called_with(con)



@patch('builtins.input',side_effect=['3'])
@patch('Ordersfile.update_order_status')
def test_order_menu_func_choice_3(mock_update_order_status,mock_input):
    expected = True
    con =''
    order_menu_text = ''
    order_update_menu_text = ''
    status_list = ''
    actual = Ordersfile.order_menu_func(con,order_update_menu_text, status_list, order_menu_text)
    assert actual == expected
    mock_update_order_status.assert_called_with(con,status_list)





@patch('builtins.input',side_effect=['4'])
@patch('Ordersfile.update_order')
def test_order_menu_func_choice_4(mock_update_orders,mock_input):
    expected = True
    con =''
    order_menu_text = ''
    order_update_menu_text = ''
    status_list = ''
    actual = Ordersfile.order_menu_func(con,order_update_menu_text, status_list, order_menu_text)
    assert actual == expected
    mock_update_orders.assert_called_with(con,order_update_menu_text)


@patch('builtins.input',side_effect=['5'])
@patch('Ordersfile.add_prod_to_order')
def test_order_menu_func_choice_5(mock_add_prod_to_order,mock_input):
    expected = True
    con =''
    order_menu_text = ''
    order_update_menu_text = ''
    status_list = ''
    actual = Ordersfile.order_menu_func(con,order_update_menu_text, status_list, order_menu_text)
    assert actual == expected
    mock_add_prod_to_order.assert_called_with(con)


@patch('builtins.input',side_effect=['6'])
@patch('Ordersfile.rem_prod_to_order')
def test_order_menu_func_choice_6(mock_rem_prod_to_order,mock_input):
    expected = True
    con =''
    order_menu_text = ''
    order_update_menu_text = ''
    status_list = ''
    actual = Ordersfile.order_menu_func(con,order_update_menu_text, status_list, order_menu_text)
    assert actual == expected
    mock_rem_prod_to_order.assert_called_with(con)





@patch('builtins.input',side_effect=['7'])
@patch('Ordersfile.delete_order')
def test_order_menu_func_choice_7(mock_delete_orders,mock_input):
    expected = True
    con =''
    order_menu_text = ''
    order_update_menu_text = ''
    status_list = ''
    actual = Ordersfile.order_menu_func(con,order_update_menu_text, status_list, order_menu_text)
    assert actual == expected
    mock_delete_orders.assert_called_with(con)