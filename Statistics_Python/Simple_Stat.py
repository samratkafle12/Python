
class Stats():

    @staticmethod
    def sum(lst):
        return sum(lst)

    @staticmethod
    def sort(lst):
        return sorted(lst)
    
    @staticmethod
    def max(lst):
        return max(lst)

    @staticmethod
    def min (lst):
        return min(lst)

    @staticmethod
    def length (lst):
        return len(lst)

    def range(lst):
        return __class__.max(lst) - __class__.min(lst)
    


    @staticmethod
    def Average(lst):
        return __class__.sum(lst)/__class__.length(lst)  #it gives the average of given list

    
    @staticmethod
    def meanDevitation (lst):
        #to calculate the meandeviation from the given data 
        Average = __class__.Average(lst)
        mean_deviation = 0
        for i in lst:
            mean_deviation = mean_deviation + abs(Average-i)
            return mean_deviation/ __class__.length(lst)

    @staticmethod
    def Count (lst, value ):
        return lst.count(value) # it counts the occurance of value in the given data 

    @staticmethod
    def Variance(lst):
        #to calculate the variance from the givin data 

        Average = __class__.Average(lst)
        variance = 0
        for i in lst:
            variance = variance + ((Average-i)**2)
        return variance/ __class__.length(lst)

    def StandardDeviation(lst):
        return __class__.Variance(lst)**0.5

    def meadian(lst):
        lst = __class__.sort(lst)
        length = __class__.length(lst)
        mid = int (length / 2)

        if (length % 2 == 0):
            return (lst[mid]+lst[mid-1])/2
        return lst[mid]

    
        

