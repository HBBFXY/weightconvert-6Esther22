initial_weight = 50  
moon_ratio = 0.165  
for year in range(1, 11):
    earth_weight = initial_weight + year * 0.5
    moon_weight = earth_weight * moon_ratio
    print(f"第{year}年，地球上的体重：{earth_weight:.2f}kg，月球上的体重：{moon_weight:.2f}kg")
