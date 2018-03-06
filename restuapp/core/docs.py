from coreapi import Document

from restuapp.customers.docs import CUSTOMERS


BASE_URL = '/api/v1/'

SCHEMA = Document(
    title='restuapp.someplace.com API',
    description="""
        RestuApp, a resturant app that's app about testing REST APIs.
    """,
    content={
        'customers': CUSTOMERS,
    }
)
