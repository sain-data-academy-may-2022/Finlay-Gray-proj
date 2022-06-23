from dataclasses import dataclass
import unittest
import Productfile
import database
from unittest.mock import patch, call, Mock

@patch('builtins.input',side_effect=[' '])
def test_product_menu_func_if_no_option(mock_input):
    expected = True
    con =''
    product_menu_text = ''
    prod_update_menu_text = ''
    actual = Productfile.product_menu_func(con,product_menu_text, prod_update_menu_text)

    assert actual == expected

@patch('builtins.input',side_effect=['0'])
def test_product_menu_func_if_exit(mock_input):
    expected = False
    con =''
    product_menu_text = ''
    prod_update_menu_text = ''
    actual = Productfile.product_menu_func(con,product_menu_text, prod_update_menu_text)

    assert actual == expected


@patch('builtins.input',side_effect=['1'])
@patch('Productfile.view_products')
def test_product_menu_func_choice_1(mock_view_product,mock_input):
    expected = True
    con =''
    product_menu_text = ''
    prod_update_menu_text = ''
    actual = Productfile.product_menu_func(con,product_menu_text, prod_update_menu_text)
    assert actual == expected
    mock_view_product.assert_called_with(con)

@patch('builtins.input',side_effect=['2'])
@patch('Productfile.add_products')
def test_product_menu_func_choice_2(mock_add_products,mock_input):
    expected = True
    con =''
    product_menu_text = ''
    prod_update_menu_text = ''
    actual = Productfile.product_menu_func(con,product_menu_text, prod_update_menu_text)
    assert actual == expected
    mock_add_products.assert_called_with(con)

@patch('builtins.input',side_effect=['3'])
@patch('Productfile.update_products')
def test_product_menu_func_choice_3(mock_update_products,mock_input):
    expected = True
    con =''
    product_menu_text = ''
    prod_update_menu_text = ''
    actual = Productfile.product_menu_func(con,product_menu_text, prod_update_menu_text)
    assert actual == expected
    mock_update_products.assert_called_with(con,prod_update_menu_text)


@patch('builtins.input',side_effect=['4'])
@patch('Productfile.delete_products')
def test_product_menu_func_choice_4(mock_delete_products,mock_input):
    expected = True
    con =''
    product_menu_text = ''
    prod_update_menu_text = ''
    actual = Productfile.product_menu_func(con,product_menu_text, prod_update_menu_text)
    assert actual == expected
    mock_delete_products.assert_called_with(con)


@patch('builtins.input',side_effect=['test','12','12',' '])
@patch('database.sql_statement')
def test_add_products(mock_sql_statement,mock_input):
    con = Mock()
    Productfile.add_products(con)
    mock_sql_statement.assert_called_with(con.cursor(),"INSERT INTO Product (name,price,quantity) VALUES ('test',12.0,12)")

