protective_nylon_sqr_m = int(input())
litres_of_paint = int(input())
litres_of_paint_thinner = int(input())
working_hours = int(input())

#He wants 10% additional paint of the planned quantity, and 2 more sqr.m. protective nylon. Also, 0.40 is going to be for nylon bags.

price_for_nylon = (protective_nylon_sqr_m + 2)* 1.50
price_for_paint = (litres_of_paint + 1.1) * 14.50
price_for_thinner = litres_of_paint_thinner * 5.00


price_for_materials = price_for_paint + price_for_thinner + price_for_nylon + 0.40
price_for_work_per_hour = (0.30 * price_for_materials)
price_for_work = price_for_work_per_hour * working_hours


total_price = price_for_work + price_for_materials
print(f'All total: {total_price}')
