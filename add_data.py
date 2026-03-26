import json

# 追加 etiquette tips (#10282, #10252)
with open('community/content/japanese-cultural-etiquette.json', 'r', encoding='utf-8') as f:
    etiquette = json.load(f)

new_tips = [
    {'situation': 'レジ会計 3', 'do': 'トレーで受け渡す', 'dont': '現金を投げるように渡す', 'note': '丁寧で非接触な受け渡し。'},
    {'situation': '写真撮影（寺社） 6', 'do': '撮影可否表示を確認する', 'dont': '禁止場所で撮影する', 'note': '御本尊周辺は撮影不可が多い。'}
]
existing_situations = [e['situation'] for e in etiquette]
for tip in new_tips:
    if tip['situation'] not in existing_situations:
        etiquette.append(tip)

with open('community/content/japanese-cultural-etiquette.json', 'w', encoding='utf-8') as f:
    json.dump(etiquette, f, ensure_ascii=False, indent=2)

# 追加 proverb (#10257)
with open('community/content/japanese-proverbs.json', 'r', encoding='utf-8') as f:
    proverbs = json.load(f)

new_proverb = {'japanese': '千里の道も一歩から', 'romaji': 'Senri no michi mo ippo kara', 'english': 'A journey of a thousand miles begins with a single step', 'meaning': 'Start small to reach big goals'}
existing_jp = [p['japanese'] for p in proverbs]
if new_proverb['japanese'] not in existing_jp:
    proverbs.append(new_proverb)

with open('community/content/japanese-proverbs.json', 'w', encoding='utf-8') as f:
    json.dump(proverbs, f, ensure_ascii=False, indent=2)
