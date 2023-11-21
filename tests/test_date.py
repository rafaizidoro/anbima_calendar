import pytest
from datetime import date
from anbima_calendar import add_business_days, is_past_due, is_business_day, get_holiday


def test_add_business_days():
    nov_friday = "25/11/2022"
    prev_independency_day = "06/09/2022"

    next_nov_friday = add_business_days(1, nov_friday)
    next_independency_day = add_business_days(1, prev_independency_day)
    three_independency_day = add_business_days(3, prev_independency_day)

    assert next_nov_friday == date(2022, 11, 28)
    assert next_independency_day == date(2022, 9, 8)
    assert three_independency_day == date(2022, 9, 12)


def test_is_business_day():
    biz_day1 = "2022-03-11"
    biz_day2 = "18/04/2022"
    holiday1 = date(2022, 11, 2)
    holiday2 = date(2023, 12, 25)
    weekend1 = "17/04/2022"
    weekend2 = "2021-10-16"

    assert is_business_day(biz_day1)
    assert is_business_day(biz_day2)
    assert not is_business_day(holiday1)
    assert not is_business_day(holiday2)
    assert not is_business_day(weekend1)
    assert not is_business_day(weekend2)


def test_is_past_due():
    due_sunday = "10/07/2022"
    current_monday = "11/07/2022"

    due_thursday = "24/11/2022"
    current_friday = "25/11/2022"

    assert not is_past_due(due_sunday, current_monday)
    assert is_past_due(due_thursday, current_friday)


def test_get_holiday():
    christmas = get_holiday("25/12/2022")
    carnival1 = get_holiday("20/02/2023")
    carnival2 = get_holiday(date(2024, 2, 13))
    bizday = get_holiday("2022-11-22")

    assert christmas == "Natal"
    assert carnival1 == "Carnaval"
    assert carnival2 == "Carnaval 2"
    assert bizday is None


def test_add_business_days_carnival():
    start_date = "15/02/2022"
    added_days = 10
    expected_date = date(2022, 3, 3)
    assert add_business_days(added_days, start_date) == expected_date


def test_get_holiday_edge_cases():
    new_year = get_holiday("01/01/2022")
    christmas = get_holiday("25/12/2022")
    assert new_year == "Confraternização Universal"
    assert christmas == "Natal"


def test_business_day_near_holiday():
    day_before_carnival = "28/02/2022"
    day_after_carnival = "02/03/2022"
    assert not is_business_day(day_before_carnival)
    assert is_business_day(day_after_carnival)


def test_is_past_due_around_holidays():
    due_date = "24/12/2024"
    current_date = "26/12/2024"
    check = is_past_due(due_date, current_date)
    assert check
