# -*- coding: utf-8 -*-
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# ===== TASK 1: Trivia Question 99 =====
trivia = {
  "question": "What is the traditional Japanese tea ceremony called? (Community variation 19)",
  "difficulty": "medium",
  "answers": ["Sado", "Judo", "Kendo", "Shodo"],
  "correctIndex": 0
}

with open('community/content/japan-trivia-medium.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
# Check if exists
exists = any(t.get('question','').startswith('What is the traditional Japanese tea ceremony') for t in data)
if not exists:
    data.append(trivia)
    with open('community/content/japan-trivia-medium.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Added Trivia #99")
else:
    print("Trivia #99 already exists")

# ===== TASK 2: Japan Fact 91 =====
fact = "There's a Japanese word 'shinpai' (心配) that describes worry with a sense of caring - unlike English, it's not purely negative."

with open('community/content/japan-facts.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
if fact not in data:
    data.append(fact)
    with open('community/content/japan-facts.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Added Japan Fact #91")
else:
    print("Japan Fact #91 already exists")

# ===== TASK 3: Etiquette Tip 108 (温泉 6) =====
etiquette = {
  "situation": "温泉 6",
  "do": "湯船前に体を洗う",
  "dont": "タオルを湯船に入れる",
  "note": "共同浴場の基本ルール。"
}

with open('community/content/japanese-cultural-etiquette.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
exists = any(e.get('situation','') == '温泉 6' for e in data)
if not exists:
    data.append(etiquette)
    with open('community/content/japanese-cultural-etiquette.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Added Etiquette #108")
else:
    print("Etiquette #108 already exists")

# ===== TASK 4: Anime Quote 47 (Hunter x Hunter) =====
anime_quote = {
  "japanese": "僕はもう逃げない!",
  "romaji": "Boku wa mou nigenai!",
  "english": "I won't run away anymore!",
  "anime": "Hunter x Hunter",
  "character": "Gon Freecss"
}

with open('community/content/anime-quotes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
exists = any(q.get('english','') == "I won't run away anymore!" for q in data)
if not exists:
    data.append(anime_quote)
    with open('community/content/anime-quotes.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Added Anime Quote #47")
else:
    print("Anime Quote #47 already exists")

# ===== TASK 5: Theme Street Lantern =====
theme = {
  "id": "street-lantern",
  "backgroundColor": "oklch(19.0% 0.038 40.0 / 1)",
  "mainColor": "oklch(85.0% 0.135 55.0 / 1)",
  "secondaryColor": "oklch(68.0% 0.165 30.0 / 1)"
}

with open('community/content/community-themes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
exists = any(t.get('id','') == 'street-lantern' for t in data)
if not exists:
    data.append(theme)
    with open('community/content/community-themes.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Added Theme street-lantern")
else:
    print("Theme street-lantern already exists")

# ===== TASK 6: Haiku 4 (Kobayashi Issa) =====
haiku = {
  "japanese": "名月を\n取ってくれろと\n泣く子かな",
  "romaji": "Meigetsu o / totte kurero to / naku ko kana",
  "english": "A child cries, asking me to fetch the harvest moon.",
  "poet": "Kobayashi Issa",
  "season": "Autumn",
  "kigo": "Harvest moon (meigetsu)",
  "notes": "Captures innocent longing through a domestic scene."
}

with open('community/content/japanese-haiku.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
exists = any(h.get('poet','') == "Kobayashi Issa" and "meigetsu" in h.get('kigo','').lower() for h in data)
if not exists:
    data.append(haiku)
    with open('community/content/japanese-haiku.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Added Haiku #4")
else:
    print("Haiku #4 already exists")

print("\nAll data additions complete!")
