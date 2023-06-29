import os
import yaml

path = "Z:\\VM\\archive-2023-06-29T150326Z"

for filename in os.listdir(path):
    if filename.endswith('.yml'):
        with open(os.path.join(path, filename), 'r') as f:
            doc = yaml.load(f, Loader=yaml.FullLoader)
            doc['events']['EnderDragonEvent']['enabled'] = True
            doc['events']['EnderDragonEvent']['repeatable'] = True
            doc['events']['EnderDragonEvent']['makeDragonInvulnerable'] = False

            doc['events']['CrateDropEvent']['enabled'] = True
            doc['events']['CrateDropEvent']['repeatable'] = True

            doc['events']['ShrinkingBorderEvent']['enabled'] = True
            doc['events']['ShrinkingBorderEvent']['repeatable'] = True

            doc['events']['GhastEvent']['enabled'] = True
            doc['events']['GhastEvent']['repeatable'] = True

            doc['events']['ChestRefillEvent']['enabled'] = True
            doc['events']['ChestRefillEvent']['repeatable'] = True

        with open(os.path.join(path, filename), 'w') as f:
            yaml.dump(doc,f, allow_unicode=True, sort_keys=False)