pack_pens = int(input())
pack_markers = int(input())
pack_preoarate = int(input())
percent_discount = int(input())

total_pens = pack_pens * 5.80
total_markers = pack_markers * 7.20
total_preoarate = pack_preoarate * 1.20

total_only = total_pens + total_preoarate + total_markers
discount = (percent_discount / 100) * total_only

grand_total = total_only - discount
print(grand_total)