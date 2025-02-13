import json

with open('sample-data.json') as f:
    data = json.load(f)

print("Interface Status")
print("="*80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<4}")
print("-" * 80)

for vesh in data['imdata']:
    interface = vesh['l1PhysIf']['attributes']
    dn = interface['dn']
    description = interface.get('descr', 'N/A') or 'empty'
    speed = interface.get('speed', 'empty')
    mtu = interface.get('mtu', 'N/A')

    print(f"{dn:<50} {description:<20} {speed:<6} {mtu:<4}")

# print(data.keys())
# print(data['imdata'])
# print(data['imdata'][13]['l1PhysIf']['attributes']['layer'])