test = [['TEST', ['ip', ['"1.1.1.0"'], 'mask', [None], 'type', ['ip_mask']], 'id']]
test2 = ['ip', ['"172.16.0.0"'], 'mask', ['12'], 'type', ['ip_mask']]
test3 = [['TEST', ['ip', [None], 'mask', ['24'], 'type', ['ip_mask']], 'id']]
test4 = [['TEST', ['ip', ['"1.1.1.0"'], 'mask', [None], 'type', ['ip_mask']], 'id']]
test5 = [['TEST', ['ip', ['"not.an.ip.address"'], 'mask', ['24'], 'type', ['ip_mask']], 'id']]
test6 = ['TEST', 'parent', [], 'uuid', '"khk-yyas4h-323223-wewe-343er-3434-www"', 'display_name',\
    '"services"', 'IPV4', [['ip', ['"192.168.1.0"'], 'mask', ['24'], 'type', ['ip_mask']], ['ip', ['"10.0.0.0"'],\
        'mask', ['8'], 'type', ['ip_mask']]]]
test7 = [['TEST', ['parent', [], 'uuid', ['"khk-yyas4h-323223-wewe-343er-3434-www"'], 'display_name', ['"services"'],\
    'IPV4', [[['ip', ['"1.1.1.0"'], 'mask', ['20'], 'type', ['ip_mask']], ['ip', ['"2.2.2.2"'], 'mask', ['32'], 'type',\
        ['ip_mask']]]]]]]


def recursive_list_access(data, info=[]):
    for d in data:
        if isinstance(d, list):
            recursive_list_access(d,info)
        else:
            d = d.replace('"', '') if d != None else d
            info.append(d)
        
    
    return info


def extract_ipv4(data):
    """
    Given a nested list of data return a list of IPv4 address information that can be extracted
    """
    data = recursive_list_access(data)
    ip_list = []

    for i in range(len(data)-1):
        try:
            if data[i] == 'ip' or data[i] == 'mask' and data[i+1][0].isdigit():
                ip_list.append(data[i+1])
        
        except TypeError:
            pass
    
    print(ip_list)
    return [(ip_list[i], ip_list[i+1]) for i in range(0,len(ip_list)-1,2) if ip_list[i]\
           != None and ip_list[i] != 'not.an.ip.address']

    
print(extract_ipv4(test7))
#print(recursive_list_access(test7, []))