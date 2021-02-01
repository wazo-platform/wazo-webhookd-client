# -*- coding: utf-8 -*-
# Copyright 2017-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


from wazo_webhookd_client.command import WebhookdCommand


class ConfigCommand(WebhookdCommand):

    resource = 'config'
    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def get(self):
        r = self.session.get(self.base_url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def patch(self, config_patch):
        r = self.session.patch(
            self.base_url, headers=self._rw_headers, json=config_patch
        )
        self.raise_from_response(r)
        return r.json()
