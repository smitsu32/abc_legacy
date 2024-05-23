## 2-1 文字列(string)
# word1 = 'hallo'
# print(type(word1))
# word2 = '123'
# i = int(123)
# print(type(word2),type(i))
# print(len(word2))

# print(word1[4])

# print('hallo'[:5:2]) ## １文字おき
# print('1234567890'[3:9:3])
# print('1234567890'[3:-2:3])

# price = '1,980円'
# print(price.replace(',', ''))

# substr1 = 'la'
# word1 = 'hallo'
# print(substr1 not in word1)

# print('That\'s all.')       ## /' でシングルクオーテーションを記述

# print('Time\nis money\\')      ## \\ はスラッシュ, \n は改行

# str = '''Time
# is
# money.\\'''
# print(str)                  ## 文章中の開業は''' or """ でOK

# word1 = 'ha'
# word2 = 'llo'
# print(word1 + ' \n ' + word2)
# print(word1.replace('a','123'))         # a -> 123　となる(word1は変化しない)


# # 練習 remove_punctuations
# def remove_punctuations(str_engsentences):      # １個ずつ置き換え
#     str1 = str_engsentences.replace('.', '')
#     str1 = str1.replace(',', '')
#     str1 = str1.replace(':', '')
#     str1 = str1.replace(';', '')
#     str1 = str1.replace('!', '')
#     str1 = str1.replace('?', '')
    
#     return str1

# print(remove_punctuations('Quiet, uh, donations, you want me to make a donation to the coast guard youth auxiliary?') == 'Quiet uh donations you want me to make a donation to the coast guard youth auxiliary')

# # 練習 str_atgc
# def atgc_bppair(str_atgc):
#     str_pair = str_atgc.replace('A', 't')
#     str_pair = str_pair.replace('T', 'a')
#     str_pair = str_pair.replace('G', 'c')
#     str_pair = str_pair.replace('C', 'g')
#     str_pair = str_pair.upper()                 # .uuper で　アルファベットを大文字にしてAT, GCを交換
#     return str_pair

# print(atgc_bppair('AAGCCCCATGGTAA') == 'TTCGGGGTACCATT')

# word1 = 'hallo'
# print(word1.index('l'))                         # .index で最初のlは３番目なので２を返す
# print(word1.find('e'))                          # .index は 未定義 ＝ error, .find は -1 を返す


# 練習 swap_colon
# def swap_colon(str1):
#     colon = str1.find(':')
#     str2, str3 = str1[:colon], str1[colon+1:]     # hhh:aa なら colon = 3 なので str3は 4(５文字めのa)から出力
#     str4 = str3 + ':' + str2
#     return str4

# print(swap_colon('hello:world') == 'world:hello')

# word1 = 'hello'
# print(word1.count('l'))                     # .count = l の個数を数える


# 練習 atgc_count
# def atgc_count(str_atgc, str_bpname):
#     return str_atgc.count(str_bpname)

# print(atgc_count('AAGCCCCATGGTAA', 'A') == 5)

# upper_dna = 'DNA'
# print(upper_dna.lower())                    # lower = 全て小文字
# print('dna'.capitalize())                   # capitalize = 先頭大文字

# str1 = '  abcd  \n \t'
# print(str1.strip())                           # .strip = 文字列前後の空白、改行、タブ文字を削除
# print(str1.lstrip())                          # .lstrip = left only, .rsprit = right only
# print(str1.rstrip())


# 練習 check_lower
# def check_lower(str_engsentences):
#     str1 = str_engsentences.lower()
#     return str1 == str_engsentences

# print(check_lower('down down down') == True)
# print(check_lower('There were doors all round the hall, but they were all locked') == False)

# def func(str1):
#     return str1.upper()

# str2 = 'abc'
# print(func('str2'))                          # str2が大文字となる


# # 練習 remove_clause
# def remove_clause(str_engsentences):
#     colon_number = str_engsentences.find(',')
#     str_res = str_engsentences[colon_number+2:]             # カンマ＋空白　で　２こインデント進み
#     str_res = str_res.capitalize()
#     return str_res

# print(remove_clause("It's being seen, but you aren't observing.") == "But you aren't observing.")