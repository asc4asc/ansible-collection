## Simple start for a collection
----

ansible-galaxy collection install git+https://github.com/asc4asc/ansible-collection.git

ansible-galaxy collection install -r requirements.yml # alternative 

ansible-galaxy collection list

ansible-playbook --connection=local --inventory=localhost, -v 
