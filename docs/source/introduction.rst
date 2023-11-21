Introduction
------------
**Anbima Calendar** is a Python library designed to simplify handling banking holidays specific to Brazil. **ANBIMA (Associação Brasileira das Entidades dos Mercados Financeiro e de Capitais)**, the Brazilian Financial and Capital Markets Association, plays a crucial role in the development of financial markets in Brazil. This library provides a robust set of tools for determining business days, calculating due dates, and identifying holidays based on the official holiday calendar published by ANBIMA.

The holiday data used in **Anbima Calendar** is sourced directly from ANBIMA's official website: `https://www.anbima.com.br/feriados/feriados.asp <https://www.anbima.com.br/feriados/feriados.asp>`_. This ensures that the library stays up-to-date with the most accurate and relevant holiday information, making it an invaluable resource for financial applications, scheduling systems, and any software dealing with date calculations in the Brazilian context.

Whether you're developing a finance-related application, a scheduling tool, or simply need to be aware of Brazilian banking holidays, Anbima Calendar offers a straightforward and efficient solution to navigate through the complexities of holiday scheduling in Brazil's financial markets.

Features
--------
- **Identify Business Days**: Quickly determine if a specific date is a business day in Brazil.
- **Calculate Due Dates**: Accurately calculate due dates taking into account weekends and holidays.
- **Discover Holidays**: Retrieve information about specific Brazilian holidays.
- **Add Business Days**: Add a specified number of business days to a given date.

Installation
------------
Install Anbima Calendar using pip:

.. code-block:: bash

    pip install anbima_calendar

Quickstart
----------
Here's a quick example to get you started with Anbima Calendar:

.. code-block:: python

    from anbima_calendar import is_business_day, add_business_days, get_holiday

    # Check if a date is a business day
    print(is_business_day('2023-04-21'))  # False, as it's Tiradentes' Day

    # Add business days to a date
    new_date = add_business_days(5, '2023-04-18')
