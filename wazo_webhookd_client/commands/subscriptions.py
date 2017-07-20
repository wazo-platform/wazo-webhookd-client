# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_webhookd_client.command import WebhookdCommand


class SubscriptionsCommand(WebhookdCommand):

    resource = 'subscriptions'
    _headers = {'Accept': 'application/json'}

    def create(self, subscription):
        r = self.session.post(self.base_url, json=subscription, headers=self._headers)
        self.raise_from_response(r)
        return r.json()

    def list(self):
        r = self.session.get(self.base_url, headers=self._headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, subscription_uuid):
        r = self.session.get('{base}/{id}'.format(base=self.base_url, id=subscription_uuid), headers=self._headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, subscription_uuid):
        r = self.session.delete('{base}/{id}'.format(base=self.base_url, id=subscription_uuid), headers=self._headers)
        self.raise_from_response(r)

