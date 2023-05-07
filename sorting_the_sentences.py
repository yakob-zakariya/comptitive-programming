class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        my_string_list = s.split(' ')
        result = [0] * len(my_string_list)
        for i in range(len(my_string_list)):
            j = int(my_string_list[i][-1]) 
            result[j-1] = my_string_list[i][:-1]
        str_result = ' '.join(result)
        return str_result
