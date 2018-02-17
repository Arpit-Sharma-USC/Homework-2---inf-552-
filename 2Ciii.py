import scikits.bootstrap as bootstrap
# import 2Cii

min_data = 2cii.f_min_net
#     [6.51562407169,
# 0.0,
# 2.40872055483,
# 0.0,
# 4.28029876297,
# 0.0262173802034]
max_data = 2cii.f_max_net
#     [2.56192815232,
# 3.88072298016,
# 3.38089262879,
# 1.82927287927,
# 3.3823198048,
# 1.92387534411]
mean_data = 2cii.f_mean_net
#     [3.23227197338,
# 1.11362166938,
# 2.55635152353,
# 0.967510948022,
# 3.4742345875,
# 0.939652426485]
median_data = 2cii.f_median_net
    # = [3.35245027268,
# 0.95992089351,
# 2.51819498442,
# 0.95138220168,
# 3.58532073343,
# 0.874062722993]
std_data = = 2cii.f_std_net
#     [1.12536705831,
# 0.681276225331,
# 0.571370859196,
# 0.401493440186,
# 0.671594023992,
# 0.445455996043]
# compute 95% confidence intervals

CIs = bootstrap.ci(data=min_data,alpha=0.02)
print("Bootstrapped 98% confidence intervals of Min \nLow:", CIs[0], "\nHigh:", CIs[1])

CIs = bootstrap.ci(data=max_data,alpha=0.02)
print("Bootstrapped 98% confidence intervals of Max \nLow:", CIs[0], "\nHigh:", CIs[1])

CIs = bootstrap.ci(data=mean_data,alpha=0.02)
print("Bootstrapped 98% confidence intervals of Mean \nLow:", CIs[0], "\nHigh:", CIs[1])

CIs = bootstrap.ci(data=median_data,alpha=0.02)
print("Bootstrapped 98% confidence intervals of Median \nLow:", CIs[0], "\nHigh:", CIs[1])

CIs = bootstrap.ci(data=std_data,alpha=0.02)
print("Bootstrapped 98% confidence intervals of Standard Deviation \nLow:", CIs[0], "\nHigh:", CIs[1])
