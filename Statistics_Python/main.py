
import Simple_Stat

lst = [6, 6, 10, 15 , 9 , 8, 17, 5]
Stats = Simple_Stat.Stats

print("Average\t", Stats.Average(lst))
print("MD\t", Stats.meanDevitation(lst))
print("Count 7\t", Stats.Count(lst, 7))
print("Length\t", Stats.length(lst))
print("Max\t", Stats.max(lst))
print("Min\t", Stats.min(lst))
print("Range\t", Stats.range(lst))
print("Sum\t", Stats.sum(lst))
print("Sort\t", Stats.sort(lst))
print("Variance", Stats.Variance(lst))
print("SD\t", Stats.StandardDeviation(lst))
print("Median\t", Stats.meadian(lst))