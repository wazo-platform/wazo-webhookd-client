# -*- coding: utf-8 -*-
# Copyright 2017-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_webhookd_client.command import WebhookdCommand


class SubscriptionsCommand(WebhookdCommand):

    resource = 'subscriptions'
    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create(self, subscription):
        r = self.session.post(
            self.base_url, json=subscription, headers=self._rw_headers
        )
        self.raise_from_response(r)
        return r.json()

    def create_as_user(self, subscription):
        url = self._client.url('users', 'me', self.resource)
        r = self.session.post(url, json=subscription, headers=self._rw_headers)
        self.raise_from_response(r)
        return r.json()

    def list(self, search_metadata=None, recurse=False):
        params = {}
        if search_metadata:
            params['search_metadata'] = self._metadata_params(search_metadata)
        if recurse:
            params['recurse'] = True
        r = self.session.get(self.base_url, params=params, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def list_as_user(self, search_metadata=None):
        params = {}
        if search_metadata:
            params['search_metadata'] = self._metadata_params(search_metadata)
        url = self._client.url('users', 'me', self.resource)
        r = self.session.get(url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, subscription_uuid):
        r = self.session.get(
            '{base}/{id}'.format(base=self.base_url, id=subscription_uuid),
            headers=self._ro_headers,
        )
        self.raise_from_response(r)
        return r.json()

    def get_as_user(self, subscription_uuid):
        url = self._client.url('users', 'me', self.resource, subscription_uuid)
        r = self.session.get(url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def update(self, subscription_uuid, subscription):
        r = self.session.put(
            '{base}/{id}'.format(base=self.base_url, id=subscription_uuid),
            json=subscription,
            headers=self._rw_headers,
        )
        self.raise_from_response(r)
        return r.json()

    def update_as_user(self, subscription_uuid, subscription):
        url = self._client.url('users', 'me', self.resource, subscription_uuid)
        r = self.session.put(url, json=subscription, headers=self._rw_headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, subscription_uuid):
        r = self.session.delete(
            '{base}/{id}'.format(base=self.base_url, id=subscription_uuid),
            headers=self._ro_headers,
        )
        self.raise_from_response(r)

    def delete_as_user(self, subscription_uuid):
        url = self._client.url('users', 'me', self.resource, subscription_uuid)
        r = self.session.delete(url, headers=self._ro_headers)
        self.raise_from_response(r)

    def list_services(self):
        r = self.session.get(
            '{base}/services'.format(base=self.base_url), headers=self._ro_headers
        )
        self.raise_from_response(r)
        return r.json()

    def _metadata_params(self, search_metadata):
        return ['{}:{}'.format(key, value) for key, value in search_metadata.items()]

    def get_logs(self, subscription_uuid, direction=None, order=None,
                 limit=None, offset=None, from_date=None):
        params = {}
        if direction is not None:
            params['direction'] = direction
        if order is not None:
            params['order'] = order
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        if from_date is not None:
            params['from_date'] = from_date
        url = self._client.url(self.resource, subscription_uuid, 'logs')
        r = self.session.get(url, headers=self._ro_headers, params=params)
        self.raise_from_response(r)
        return r.json()
