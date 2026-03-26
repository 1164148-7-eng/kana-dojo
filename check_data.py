# -*- coding: utf-8 -*-
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Check themes
with open('community/content/community-themes.json', 'r', encoding='utf-8') as f:
    themes = json.load(f)
print('sakurajima-ash exists:', any('sakurajima-ash' in t.get('id','') for t in themes))
print('Total themes:', len(themes))

# Check etiquette
with open('community/content/japanese-cultural-etiquette.json', 'r', encoding='utf-8') as f:
    etiquette = json.load(f)
print('レジ会計 exists:', any('レジ会計' in e.get('situation','') for e in etiquette))
print('Total etiquette:', len(etiquette))

# Check proverbs
with open('community/content/japanese-proverbs.json', 'r', encoding='utf-8') as f:
    proverbs = json.load(f)
print('千里の道も一歩から exists:', any('千里の道も一歩から' in p.get('japanese','') for p in proverbs))
print('Total proverbs:', len(proverbs))
