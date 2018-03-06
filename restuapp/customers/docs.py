from coreapi import Link, Field


BASE_URL = '/api/v1/'
CUSTOMERS_BASE_URL = BASE_URL + 'customers/'

CUSTOMERS = {
    'list': Link(
        url=CUSTOMERS_BASE_URL,
        action='get',
        description="""
            List Customers

            Lists all customers in the system
        """,
    ),
    'create': Link(
        url=CUSTOMERS_BASE_URL,
        action='post',
        description="""
            Create New Customer

            Creates a new customer object
        """,
        fields=[
            Field(
                name='name',
                required=True,
                location='formData',
            ),
            Field(
                name='phone',
                required=True,
                location='formData',
            ),
            Field(
                name='address',
                required=True,
                location='formData',
            ),
        ]
    ),
    'update': Link(
        url=CUSTOMERS_BASE_URL + '{pk}/',
        action='patch',
        description="""
            Update Existing Customer

            Updates an existing customer provided his/her id
        """,
        fields=[
            Field(
                name='pk',
                required=True,
                location='path',
            ),
            Field(
                name='name',
                required=False,
                location='formData',
            ),
            Field(
                name='phone',
                required=False,
                location='formData',
            ),
            Field(
                name='address',
                required=False,
                location='formData',
            ),
        ]
    ),
}
