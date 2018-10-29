msg_parser
==========

.. image:: https://img.shields.io/pypi/v/msg_parser.svg
        :target: https://pypi.python.org/pypi/msg_parser

.. image:: https://img.shields.io/travis/vikramarsid/msg_parser.svg
        :target: https://travis-ci.org/vikramarsid/msg_parser

.. image:: https://readthedocs.org/projects/msg-parser/badge/?version=latest
        :target: https://msg-parser.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/vikramarsid/msg_parser/shield.svg
     :target: https://pyup.io/repos/github/vikramarsid/msg_parser/
     :alt: Updates

Python module for parsing outlook msg files.


* Free software: BSD license
* Documentation: https://msg-parser.readthedocs.io.


Features
--------

* Parse MSG file.
* Convert MSG file to EML file.
* Output MSG file as JSON string.
* Handles nested MSG/EML attachments.
* Works 100% on Linux machines, do not require any windows libraries.

Installation
------------

* Basic installation

  .. code-block:: bash

 	 pip install msg_parser

* With RTF decompression

  .. code-block:: bash

 	 pip install msg_parser[rtf]


Usage
-----

* Run CLI command

   .. code-block:: bash

       $ msg_parser --help
         usage: msg_parser [-h] -i FILE [-j] [-e EML_FILE]

        Microsoft Message Parser

        optional arguments:
            -h, --help            show this help message and exit
            -i FILE, --input FILE
                                  msg file path
            -j, --json            output parsed msg as json to console
            -e EML_FILE, --eml EML_FILE
                                  provide email file path to save as eml file.


 * Import in python modules

   .. code-block:: python

        from msg_parser import MsOxMessage

        msg_obj = MsOxMessage(msg_file_path)

        json_string = msg_obj.get_message_as_json()

        msg_properties_dict = msg_obj.get_properties()

        saved_path = msg_obj.save_email_file(output_eml_file_path)

