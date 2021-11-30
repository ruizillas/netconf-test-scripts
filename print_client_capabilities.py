from ncclient import manager

eos=manager.connect(host="ceos1", port="830", timeout=30, username="admin", password="xxxx", hostkey_verify=False)

for item in eos.client_capabilities:
    print (item)

eos.close_session()
