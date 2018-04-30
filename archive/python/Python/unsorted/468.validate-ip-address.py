class Solution(object):
    hexset = set(list('1234567890abcdefABCDEF'))

    def is_hex(self, ip):
        for char in ip:
            if char not in self.hexset:
                return False
        return True

    def isIpv4(self, ip_address):
        if not ip_address or len(ip_address.split('.')) != 4:
            return False

        def valid_part(s):
            return s.isdigit() and str(int(s)) == s and int(s) <= 255

        return all([valid_part(part) for part in ip_address.split('.')])

    def validIPAddress(self, IP):
        if len(IP.split('.')) == 4:
            if self.isIpv4(IP):
                return 'IPv4'
            return 'Neither'
        elif len(IP.split(':')) == 8:
            ip_list = IP.split(':')
            for part in ip_list:
                if len(part) == 0 or not self.is_hex(part) or len(part) > 4:
                    return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'


# if __name__ == '__main__':
#     a = Solution()
#     print(a.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
