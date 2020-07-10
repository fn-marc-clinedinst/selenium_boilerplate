import logging
import pytest
import requests

from datetime import datetime, timedelta
from random import choice
from selenium.webdriver.common.by import By
from time import sleep

from api import actions, authorization, current_user

from pages import ActionModal, ActionsPage, ConfirmationModal, HomePage, LoginPage, TopSearch
from utilities.validators import date_is_valid, time_is_valid
from utilities.wait import wait_for_element_to_be_visible


def delete_icon_by_action_summary(action_summary):
    return {
        'by': By.XPATH,
        'value': f'//p[text()="{action_summary}"]//ancestor::tr//i[@class="ion-trash-b"]'
    }


def new_action_summary(summary_text):
    return {
        'by': By.XPATH,
        'value': f'//td[contains(@class, "actions-row__summary-col")]//p[text()="{summary_text}"]'
    }


def get_random_number():
    return choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def get_date():
    date = datetime.now()

    return f'{date.month}/{date.day}/{date.year}'


def get_timestamp():
    date = datetime.now()

    return f'{date.hour}:{date.minute}:{date.second}'


def test_action_counts_for_empty_state(driver):
    login_page = LoginPage(driver)
    login_page.login('selenium.course@fiscalnote.com', 'not_my_real_password')

    home_page = HomePage(driver)
    assert "Welcome" in home_page.welcome_message

    actions_page = ActionsPage(driver)
    actions_page.navigate()

    assert actions_page.total_actions_count == 0
    assert actions_page.actions_this_week_count == 0
    assert actions_page.actions_this_month_count == 0

    assert "No actions yet." in actions_page.empty_state_help_text
    assert "Create one to record meetings, calls, and other actions to share past and future activity with your team." in actions_page.empty_state_help_text

    assert actions_page.empty_state_add_action_button.is_displayed()


def test_user_sees_correct_default_state_for_action_modal(driver):
    login_page = LoginPage(driver)
    login_page.login('selenium.course@fiscalnote.com', 'not_my_real_password')

    home_page = HomePage(driver)
    assert "Welcome" in home_page.welcome_message

    actions_page = ActionsPage(driver)
    actions_page.navigate()
    actions_page.click_empty_state_add_action_button()

    action_modal = ActionModal(driver)

    assert action_modal.is_displayed

    assert action_modal.modal_header_text == "Add Action"

    assert date_is_valid(action_modal.start_date_value)

    assert time_is_valid(action_modal.start_time_value)

    assert date_is_valid(action_modal.end_date_value)

    assert time_is_valid(action_modal.end_time_value)

    assert action_modal.selected_action_type == "Meeting"

    assert action_modal.added_attendees == ['Selenium Course']

    assert action_modal.added_linked_items == []

    assert action_modal.added_labels == []

    assert action_modal.added_issues == []

    assert action_modal.current_summary_text == ''


def test_user_can_open_actions_modal_with_empty_state_add_action_button_and_close_it_with_cancel_button(driver):
    login_page = LoginPage(driver)
    login_page.login('selenium.course@fiscalnote.com', 'not_my_real_password')

    home_page = HomePage(driver)
    assert "Welcome" in home_page.welcome_message

    actions_page = ActionsPage(driver)
    actions_page.navigate()
    actions_page.click_empty_state_add_action_button()

    action_modal = ActionModal(driver)
    action_modal.click_cancel_button()

    confirmation_modal = ConfirmationModal(driver)
    confirmation_modal.click_cancel_button()

    assert action_modal.is_displayed

    action_modal.click_cancel_button()
    confirmation_modal.click_confirm_button()

    assert action_modal.is_not_displayed


def test_user_can_open_actions_modal_with_main_add_action_button_and_close_it_with_x_icon(driver):
    login_page = LoginPage(driver)
    login_page.login('selenium.course@fiscalnote.com', 'not_my_real_password')

    home_page = HomePage(driver)

    welcome_message = "Welcome, Selenium"
    logging.info(f'Verifying that the text "{welcome_message}" appears in the welcome message on the Home Page.')
    assert welcome_message in home_page.welcome_message

    actions_page = ActionsPage(driver)
    actions_page.navigate()
    actions_page.click_add_action_button()

    action_modal = ActionModal(driver)

    logging.info('Verifying Action Modal is visible.')
    assert action_modal.is_displayed

    action_modal.click_close_icon()

    confirmation_modal = ConfirmationModal(driver)
    confirmation_modal.click_cancel_button()

    logging.info('Verifying Action Modal is still visible.')
    assert action_modal.is_displayed

    action_modal.click_close_icon()
    confirmation_modal.click_confirm_button()

    logging.info('Verifying Action Modal is no longer visible.')
    assert action_modal.is_not_displayed


def test_user_can_create_a_new_action(driver):
    login_page = LoginPage(driver)
    login_page.login('selenium.course@fiscalnote.com', 'not_my_real_password')

    home_page = HomePage(driver)
    assert "Welcome" in home_page.welcome_message

    actions_page = ActionsPage(driver)
    actions_page.navigate()
    actions_page.click_add_action_button()

    action_modal = ActionModal(driver)
    action_modal.enter_start_date('8/14/2019')
    action_modal.enter_start_time('6:00am')
    action_modal.enter_end_date('8/14/2019')
    action_modal.enter_end_time('5:00pm')
    action_modal.set_action_type('Phone Call')
    action_modal.add_linked_item('US HR 1478', 'US - HR 1478')
    action_modal.add_labels(('agriculture', 'farming', 'welfare'))
    action_modal.add_issue('Agriculture')

    action_summary_text = f'{get_date()} {get_timestamp()} - This is my summary text.'
    action_modal.add_summary(action_summary_text)

    action_modal.click_save_button()

    expected_action_1_start = "Mar 27, 2020 2:08 PM"
    logging.info(f'Verifying that the "Start" value for the action in position 1 equals "{expected_action_1_start}"')
    assert actions_page.get_action_start_by_position(1) == expected_action_1_start

    expected_action_1_end = "Mar 27, 2020 3:08 PM"
    logging.info(f'Verifying that the "End" value for the action in position 1 equals "{expected_action_1_end}"')
    assert actions_page.get_action_end_by_position(1) == expected_action_1_end

    expected_action_2_start = "Mar 27, 2020 2:08 PM"
    logging.info(f'Verifying that the "Start" value for the action in position 2 equals "{expected_action_2_start}"')
    assert actions_page.get_action_start_by_position(2) == expected_action_2_start

    expected_action_2_end = "Mar 27, 2020 3:08 PM"
    logging.info(f'Verifying that the "End" value for the action in position 2 equals "{expected_action_2_end}"')
    assert actions_page.get_action_end_by_position(2) == expected_action_2_end

    expected_action_3_start = "Mar 4, 2020 2:08 PM"
    logging.info(f'Verifying that the "Start" value for the action in position 3 equals "{expected_action_3_start}"')
    assert actions_page.get_action_start_by_position(3) == expected_action_3_start

    expected_action_3_end = "Mar 5, 2020 3:08 PM"
    logging.info(f'Verifying that the "End" value for the action in position 3 equals "{expected_action_3_end}"')
    assert actions_page.get_action_end_by_position(3) == expected_action_3_end

    expected_creator = 'Tem Automation'
    logging.info(f'Verifying that the "Creator" value for the action in position 1 equals "{expected_creator}"')
    assert actions_page.get_action_creator_by_position(1) == expected_creator

    expected_attendees = ['Herm Automation', 'Selenium Course', 'Tem Automation']
    logging.info(f'Verifying that the "Attendees" value for the action in position 1 equals "{expected_attendees}"')
    assert actions_page.get_action_attendees_by_position(1) == expected_attendees

    expected_issues = ['Agriculture', 'Farming', 'Welfare']
    logging.info(f'Verifying that the "Issues" value for the action in position 1 equals "{expected_issues}"')
    assert actions_page.get_action_issues_by_position(1) == expected_issues

    expected_summary = 'Edit summary and find the position'
    logging.info(f'Verifying that the "Summary" value for the action in position 1 equals "{expected_summary}"')
    assert actions_page.get_action_summary_by_position(1) == expected_summary


def test_user_can_delete_action(driver):
    auth_header = authorization.get_authorization_header('selenium.course@fiscalnote.com', 'not_my_real_password')
    actions.delete_all_actions(auth_header)
    actions.create_action(auth_header, summary='This action needs to be deleted.')

    login_page = LoginPage(driver)
    login_page.login('selenium.course@fiscalnote.com', 'June121!!!')

    home_page = HomePage(driver)
    assert "Welcome" in home_page.welcome_message

    actions_page = ActionsPage(driver)
    actions_page.navigate()

    expected_actions_count = 1
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    actions_page.click_delete_action_icon_by_position(1)

    confirmation_modal = ConfirmationModal(driver)

    logging.info('Verifying that the "Delete Action" modal is visible.')
    assert confirmation_modal.is_displayed
    assert confirmation_modal.modal_title == 'Delete Action'

    confirmation_modal.click_cancel_button()

    logging.info('Verifying that the "Delete Action" modal is not visible.')
    assert confirmation_modal.is_not_displayed

    logging.info('Verifying that the action in position 1 has a summary of "This action needs to be deleted."')
    assert actions_page.get_action_summary_by_position(1) == 'This action needs to be deleted.'

    actions_page.click_delete_action_icon_by_position(1)
    confirmation_modal.click_ok_button()

    expected_actions_count = 0
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count


def test_user_can_batch_delete_actions(driver):
    auth_header = authorization.get_authorization_header('selenium.course@fiscalnote.com', 'not_my_real_password')
    actions.delete_all_actions(auth_header)

    for number in range(1, 11):
        actions.create_action(auth_header, summary=f'Action #{number}')

    login_page = LoginPage(driver)
    login_page.login('selenium.course@fiscalnote.com', 'June121!!!')

    home_page = HomePage(driver)
    assert "Welcome" in home_page.welcome_message

    actions_page = ActionsPage(driver)
    actions_page.navigate()

    expected_actions_count = 10
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    actions_page.select_all_actions_on_current_page()

    logging.info('Verifying that 10 actions are selected.')
    assert actions_page.selected_count == '10 Selected'

    actions_page.click_delete_button()

    confirmation_modal = ConfirmationModal(driver)
    confirmation_modal.click_cancel_button()

    actions_page.click_delete_button()

    confirmation_modal.click_ok_button()

    expected_actions_count = 0
    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that the "Total Actions" count equals {expected_actions_count}.')
    assert expected_actions_count == actual_actions_count

    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    driver.refresh()

    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that the "Total Actions" count equals {expected_actions_count}.')
    assert expected_actions_count == actual_actions_count

    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count


def test_user_can_batch_delete_individual_actions(driver):
    auth_header = authorization.get_authorization_header('selenium.course@fiscalnote.com', 'not_my_real_password')
    actions.delete_all_actions(auth_header)

    for number in range(10, 0, -1):
        actions.create_action(auth_header, summary=f'Action #{number}')

    login_page = LoginPage(driver)
    login_page.login('selenium.course@fiscalnote.com', 'Meatball1!!')

    home_page = HomePage(driver)
    assert "Welcome" in home_page.welcome_message

    actions_page = ActionsPage(driver)
    actions_page.navigate()

    expected_actions_count = 10
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    positions = list(range(1, 11))
    deleted_action_positions = []

    for iteration in range(3):
        position = choice(positions)
        positions.remove(position)
        actions_page.select_action_by_position(position)
        deleted_action_positions.append(position)

    actions_page.click_delete_button()

    confirmation_modal = ConfirmationModal(driver)
    confirmation_modal.click_ok_button()

    expected_actions_count = 7
    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that the "Total Actions" count equals {expected_actions_count}.')
    assert expected_actions_count == actual_actions_count

    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    expected_action_summaries = [f'Action #{position}' for position in positions]
    logging.info(f'Verifying that the following actions are visible: {expected_action_summaries}')
    assert actions_page.visible_action_summaries == expected_action_summaries

    driver.refresh()

    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that the "Total Actions" count equals {expected_actions_count}.')
    assert expected_actions_count == actual_actions_count

    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    logging.info(f'Verifying that the following actions are visible: {expected_action_summaries}')
    assert actions_page.visible_action_summaries == expected_action_summaries


def test_user_can_search_for_actions_by_action_summary(driver):
    auth_header = authorization.get_authorization_header('selenium.course@fiscalnote.com', 'not_my_real_password')
    actions.delete_all_actions(auth_header)

    action_summaries = [
        'this action summary is unique',
        'this action summary is the same',
        'this action summary is the same'
    ]

    for action_summary in action_summaries:
        actions.create_action(auth_header, summary=action_summary)

    login_page = LoginPage(driver)
    login_page.login('selenium.course@fiscalnote.com', 'June121!!!')

    home_page = HomePage(driver)
    assert "Welcome" in home_page.welcome_message

    actions_page = ActionsPage(driver)
    actions_page.navigate()

    expected_actions_count = 3
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actions_page.visible_actions_count == expected_actions_count

    expected_visible_actions = list(reversed(action_summaries))
    logging.info(f'Verifying that the following actions are visible: {expected_visible_actions}')
    assert actions_page.visible_action_summaries == expected_visible_actions

    top_search = TopSearch(driver)
    top_search.perform_search('unique')

    expected_actions_count = 1
    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count

    expected_action_summaries = ['this action summary is unique']
    logging.info(f'Verifying that the following actions are visible: {expected_action_summaries}')
    assert actions_page.visible_action_summaries == expected_action_summaries

    top_search.perform_search('same')

    expected_actions_count = 2
    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count

    expected_action_summaries = [
        'this action summary is the same',
        'this action summary is the same'
    ]
    logging.info(f'Verifying that the following actions are visible: {expected_action_summaries}')
    assert actions_page.visible_action_summaries == expected_action_summaries

    top_search.perform_search('this_should_not_match_anything')

    expected_actions_count = 0
    actual_actions_count = actions_page.wait_for_total_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verifying that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count

    expected_action_summaries = []
    logging.info(f'Verifying that the following actions are visible: {expected_action_summaries}')
    assert actions_page.visible_action_summaries == expected_action_summaries


def test_user_can_open_actions_summary_modal(actions_page, actions_summary_modal, home_page, login_page):
    auth_header = authorization.get_authorization_header('selenium.course@fiscalnote.com', 'not_my_real_password')
    actions.delete_all_actions(auth_header)

    logging.info('Creating 5 past actions.')
    for number in range(5):
        actions.create_action(
            auth_header,
            end_date=datetime.now() - timedelta(days=7),
            start_date=datetime.now() - timedelta(days=7, hours=1),
            summary='past action'
        )

    logging.info('Creating 10 actions on current day.')
    for number in range(10):
        actions.create_action(auth_header, summary='current date')

    logging.info('Creating 5 future actions.')
    for number in range(5):
        actions.create_action(
            auth_header,
            end_date=datetime.now() + timedelta(days=7, hours=1),
            start_date=datetime.now() + timedelta(days=7),
            summary='future action'
        )

    login_page.login('selenium.course@fiscalnote.com', 'not_my_real_password')

    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()
    actions_page.click_see_actions_summary_link()

    expected_total_actions_count = 20
    logging.info(f'Verify that "Total Actions" equals {expected_total_actions_count}')
    assert actions_summary_modal.total_actions == expected_total_actions_count

    logging.info(f'Verify that "Total Actions" in the modal matches what is on the page.')
    assert actions_summary_modal.total_actions == actions_page.total_actions_count

    expected_actions_this_month = 20
    logging.info(f'Verify that "Actions This Month" equals {expected_actions_this_month}')
    assert actions_summary_modal.actions_this_month == expected_total_actions_count

    logging.info(f'Verify that "Actions This Month" in the modal matches what is on the page.')
    assert actions_summary_modal.actions_this_month == actions_page.actions_this_month_count

    expected_actions_this_week = 10
    logging.info(f'Verify that "Actions This Week" equals {expected_actions_this_week}')
    assert actions_summary_modal.actions_this_week == expected_actions_this_week

    logging.info(f'Verify that "Actions This Week" in the modal matches what is on the page.')
    assert actions_summary_modal.actions_this_week == actions_page.actions_this_week_count


def test_user_can_load_more_actions(actions_page, home_page, login_page):
    auth_header = authorization.get_authorization_header('selenium.course@fiscalnote.com', 'not_my_real_password')
    actions.delete_all_actions(auth_header)

    logging.info('Creating 40 actions.')
    for number in range(1, 41):
        actions.create_action(auth_header, summary=f'Summary #{number}')

    login_page.login('selenium.course@fiscalnote.com', 'not_my_real_password')

    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()

    expected_actions_count = 15
    actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count

    actions_page.load_more_actions()

    expected_actions_count = 30
    actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count

    actions_page.load_more_actions()

    expected_actions_count = 40
    actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count


@pytest.mark.homework_solution
def test_user_can_filter_by_start_and_end_date_to_find_past_actions(actions_page, home_page, login_page):
    auth_header = authorization.get_authorization_header('selenium.course@fiscalnote.com', 'July91!!!')
    actions.delete_all_actions(auth_header)

    logging.info('Creating 5 past actions.')
    for number in range(5):
        actions.create_action(
            auth_header,
            end_date=datetime.now() - timedelta(days=7),
            start_date=datetime.now() - timedelta(days=7, hours=1),
            summary='past action'
        )

    logging.info('Creating 10 actions on current day.')
    for number in range(10):
        actions.create_action(auth_header, summary='current date')

    logging.info('Creating 5 future actions.')
    for number in range(5):
        actions.create_action(
            auth_header,
            end_date=datetime.now() + timedelta(days=7, hours=1),
            start_date=datetime.now() + timedelta(days=7),
            summary='future action'
        )

    login_page.login('selenium.course@fiscalnote.com', 'July91!!!')

    assert "Welcome" in home_page.welcome_message

    actions_page.navigate()

    expected_actions_count = 15
    actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count

    actions_page.open_filter_by_filter_text("Start")
    # actions_page.move_calendar_widget_back('start')
    actions_page.click_date('start', '1')
    actions_page.click_date_filter_apply_button('start')

    actions_page.open_filter_by_filter_text("End")
    # actions_page.move_calendar_widget_back('end')
    actions_page.click_date('end', '4') # TODO: This line of code is occasionally flaky. Please fix.
    actions_page.click_date_filter_apply_button('end')

    expected_actions_count = 5
    actual_actions_count = actions_page.wait_for_visible_actions_count_to_equal(expected_actions_count)
    logging.info(f'Verify that {expected_actions_count} actions are visible.')
    assert actual_actions_count == expected_actions_count

    expected_action_summaries = ['past action', 'past action', 'past action', 'past action', 'past action']
    logging.info(f'Verify that the following action summaries are visible: {expected_action_summaries}')
    assert actions_page.visible_action_summaries == expected_action_summaries
