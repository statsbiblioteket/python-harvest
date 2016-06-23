from statsbiblioteket.harvest.rest import Rest


class Invoices(Rest):
    # Invoices

    def invoices(self, start_date=None, end_date=None,
                 updated_since=None, client_id=None,
                 status_enum=None):
        """
        Get all the invoices, optionally filtered by:
        - start and end dates
        - client_id
        - status
        - updated since date
        http://help.getharvest.com/api/invoices-api/invoices/show-invoices/#show-recently-created-invoices
        """

        if client_id:
            params = {'client': client_id}
        elif start_date or end_date:
            params = {'from': start_date, 'to': end_date}
        elif status_enum:
            params = {'status':status_enum}
        elif updated_since:
            params = {'updated_since':updated_since}
        else:
            params = {}
        return self._get('/invoices', params=params)

    def get_invoice(self, invoice_id):
        """
        Get an invoice by `invoice_id`
        http://help.getharvest.com/api/invoices-api/invoices/show-invoices/#show-a-single-invoice
        """
        url = '/invoices/{0}'.format(invoice_id)
        return self._get(url)

    def delete_invoice(self, invoice_id):
        """
        Delete an existing invoice by `invoice_id`
        http://help.getharvest.com/api/invoices-api/invoices/show-invoices/#delete-existing-invoice
        """
        url = '/invoices/{0}'.format(invoice_id)
        return self._delete(url)

    def update_invoice(self, invoice_id, data):
        """
        Update an existing invoice by `invoice_id`
        http://help.getharvest.com/api/invoices-api/invoices/show-invoices/#update-existing-invoice
        """
        url = '/invoices/{0}'.format(invoice_id)
        return self._put(url, data)

    def add_invoice(self, data):
        """
        Create a new invoice
        http://help.getharvest.com/api/invoices-api/invoices/create-an-invoice/
        """
        return self._post('/invoices', data)
