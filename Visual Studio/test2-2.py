## 2-2 リスト(list)
# numbers = [2, 1, 3, 4, 'five']
# print(len(numbers))
# print(numbers[:4:2])            # 0(１番目の２)から4(５番目のfive)まで1つおきに
# print(numbers[1:4])             # 1(２番目の1)から4 (５番目のfive)の直前まで
# print(type(numbers))


# # 練習 偶数番目を取り出す
# def remove_evenindex(ln):
#     return ln[1::2]             # 2番目からラストまで１つおき

# print(remove_evenindex(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == ['b', 'd', 'f'] )
# print(remove_evenindex([1, 2, 3, 4, 5]) == [2, 4])


#　多重リスト
# lns = [[1, 2, 3], ['one', 'two', 'three']]
# print(lns[1][2])                                # ２番目の行列の３番目を表示
# lns2 = [lns, [0, 1, [4, 3, 2]], [2, 1, 0]]
# print(lns2[0])                                  # lns を出力

# charactors = ['a', 'n', 'z']
# numbers = [1, 3, 10]
# print(max(charactors))
# print(min(numbers))                             # max min
# print(charactors + numbers)

# print(sum(numbers*3))                             # sum

# zero10 = [[0, 0], [0, 0]] * 10
# print(zero10)                                   # 0行列のつくりかた

# x = [[0, 1], [2, 3]]
# y = x*3
# print(y)

# x[0][0] = 100
# print(y)                                        # xの要素を変えるとyも変化する

# print([2, 3] in x)

# al = 1
# print (al in [1, 3, 5])                     # 1　は 1 or 3 or 5　の中にあるか？

# numbers =[0, 10, 20, 30, 40, 50, 60]
# print(11 not in numbers)
# print(numbers.index(30))                       # .index !! リストでは.findは使用不可

# all20 = [20]*4
# print(all20.count(20))

# numbers = [1, 7, 5, 2]
# numbers.sort()                  # .sort で　小さい順に(in-place)
# print(numbers)

# numbers.sort(reverse = True)    # reverse = True で　大きい順に
# print(numbers)

# print(sorted(numbers))              # sorted -> 元の関数は変更しない 
# print(sorted(numbers, reverse = True))

# numbers = [1, -7, 5, 2]
# numbers.append(12)                  # .append　要素
# numbers.extend([-10, 0, -2])        # .extend リスト追加
# print(numbers)

# positives = []
# positives.append(numbers[0])
# positives.append(numbers[2])
# positives.append(numbers[3])
# positives.append(numbers[4])
# print(positives)

# numbers = [1, -7, 5, 2]
# numbers.insert(2, 1000)             # .insert ３番目に1000追加
# print(numbers)

# numbers.remove(5)                   # .remove 削除したい要素名を記入
# print(numbers)                        # 範囲外はエラー

# numbers = [1, -7, 5, 2]
# print(numbers.pop(3))                         # .pop 取り出したいインデックスを記入
# print(numbers)                         #なくなる

# numbers = [1, -7, 5, 2]
# del numbers[2]                          # del 削除したいインデックス
# print(numbers)

# numbers = [1, -7, 5, 2]
# del numbers[:2]                     # 範囲も可
# print(numbers)

# numbers = [1, -7, 5, 2]
# numbers.reverse()                      #. reverse リストを逆順に
# print(numbers)

# numbers = [1, -7, 5, 2]
# numbers2 = numbers.copy()           #.copy リストをコピー
# numbers.pop(2)                        # number2 = number とすると変化する
# print(numbers, numbers2)

# print(list('abcdef'))               # list() 文字単位に区切る
# print('bnanana'.split('n'))          # .split n単位に区切る
# print('A B \nC '.split())

# str1 = ''.join(['a', 'b', 'c', '1'])    #　.join() 左の引数でくっつける
# print(str1)


## 練習　ドメイン置き換え
# def change_domain(email, domain):
#     return '@'.join([email.split('@')[0], domain])      # emailの　@　前　＋（@）＋　ドメイン　
# print(change_domain('spam@utokyo-ipp.org', 'ipp.u-tokyo.ac.jp') == 'spam@ipp.u-tokyo.ac.jp')
# print(change_domain('spam@utokyo-ipp.org', 'ipp.u-tokyo.ac.jp'))


# タプル
