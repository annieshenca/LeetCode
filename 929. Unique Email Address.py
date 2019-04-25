class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        dic = set()
        
        for email in emails:
            name, adrs = email.split('@')
            
            # Remove everything after the '+' in name
            if '+' in name:
                name = name.split('+')[0]
                
            # Remove the '.' in strings
            name = name.replace('.', '')
            cleaned = name+'@'+adrs
            dic.add(cleaned)
            
        # return count
        return len(dic)
