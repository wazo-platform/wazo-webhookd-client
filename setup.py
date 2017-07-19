#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


from setuptools import setup
from setuptools import find_packages

setup(
    name='wazo_webhookd_client',
    version='1.0',

    description='a simple client library for the wazo webhookd HTTP interface',

    author='Wazo Authors',
    author_email='dev@wazo.community',

    url='http://wazo.community',

    packages=find_packages(),

    entry_points={
        'wazo_webhookd_client.commands': [
            'config = wazo_webhookd_client.commands.config:ConfigCommand',
            'subscriptions = wazo_webhookd_client.commands.subscriptions:SubscriptionsCommand',
        ],
    }
)
