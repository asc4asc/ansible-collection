from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = r'''
---
module: hello
short_description: A simple hello world module
description:
    - This module says hello to a person.
options:
    name:
        description:
            - The name of the person to say hello to.
        type: str
        required: true
author:
    - your name (@asc4asc)
'''

EXAMPLES = r'''
- name: Say hello
  asc4asc.show_collection.hello:
    name: "Rovo"
'''

RETURN = r'''
msg:
    description: The hello message.
    returned: always
    type: str
    sample: "Hello Rovo"
'''

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True)
        )
    )

    name = module.params['name']

    module.exit_json(
        changed=False,
        msg=f"Hello {name}"
    )

if __name__ == '__main__':
    main()