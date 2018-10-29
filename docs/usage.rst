=====
Usage
=====

To use msg_parser in a project::

    from msg_parser import MsOxMessage

    msg_obj = MsOxMessage(msg_file_path)

    json_string = msg_obj.get_message_as_json()

    msg_properties_dict = msg_obj.get_properties()

    saved_path = msg_obj.save_email_file(output_eml_file_path)
