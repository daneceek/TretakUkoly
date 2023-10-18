input = 4732
metr = input // 1000
metr_zb = input % 1000
centimetr = metr_zb // 10
milimetr = metr_zb % 10
print(f"Délka se skládá z {metr} metrů, {centimetr} centimetrů a {milimetr} milimetrů")
