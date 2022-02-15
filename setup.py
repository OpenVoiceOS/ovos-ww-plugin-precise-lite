#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'ovos-precise-lite=ovos_ww_plugin_precise_lite:PreciseLiteHotwordPlugin'
setup(
    name='ovos-ww-plugin-precise-lite',
    version='0.1.1',
    description='A wake word plugin for OpenVoiceOS',
    url='https://github.com/OpenVoiceOS/ovos-ww-plugin-precise-lite',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['ovos_ww_plugin_precise_lite'],
    install_requires=["precise_lite_runner~=0.4",
                      "ovos-utils~=0.0.14a7",
                      "ovos-plugin-manager~=0.0.4a2"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mycroft ovos plugin wake word',
    entry_points={'mycroft.plugin.wake_word': PLUGIN_ENTRY_POINT}
)
