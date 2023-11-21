.. _examples:

Examples
========

This section provides practical examples of how to use the `anbima_calendar` library. These examples cover common use cases and demonstrate the library's functionality.

Checking Business Days
----------------------

To determine if a specific date is a business day in Brazil:

.. code-block:: python

    from anbima_calendar import is_business_day

    # Check if a date is a business day
    if is_business_day('2023-04-21'):
        print('April 21, 2023, is a business day.')
    else:
        print('April 21, 2023, is not a business day.')  # Tiradentes' Day

Adding Business Days
--------------------

To add a number of business days to a given date:

.. code-block:: python

    from anbima_calendar import add_business_days

    # Add 5 business days to April 18, 2023
    new_date = add_business_days(5, '2023-04-18')
    print('New date:', new_date)

Identifying Holidays
---------------------

To find out if a date is a holiday and retrieve its name:

.. code-block:: python

    from anbima_calendar import get_holiday

    holiday_name = get_holiday('2023-05-01')
    if holiday_name:
        print('May 1, 2023, is a holiday:', holiday_name)  # Labor Day
    else:
        print('May 1, 2023, is not a holiday.')

Calculating Due Dates
---------------------

To calculate a due date considering only business days:

.. code-block:: python

    from anbima_calendar import add_business_days

    # Calculate a due date 10 business days from December 20, 2023
    due_date = add_business_days(10, '2023-12-20')
    print('Due date:', due_date)

These examples are intended to help you quickly understand and utilize the `anbima_calendar` library in your projects. For more detailed information, refer to the API reference section of this documentation.
