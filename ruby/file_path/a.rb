# ファイルではなく実行時のディレクトリからの相対パス
# なのでこれはa.rbのディレクトリでしか動かない
# p File.read('baz.txt')
# p File.read('./hoge/foo.txt')

# 逆にこうしておけばb.rbからは動くがからは動かない
p File.read('../baz.text')
p File.read('../hoge/foo.txt')