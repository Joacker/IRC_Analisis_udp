def f2(packet):
    try:
        if (packet['TCP']['dstport'] == 6667): #request
            comando = packet['IRC']['request'].split(" ")[0]
            print ("comando: ",comando)
            if (comando == 'NICK'):
                print ("Se reemplaza nick")
                packet['IRC']['request'] = packet['IRC']['request'].replace('usuario','baduser')
                print (packet['IRC']['request'])
            if (comando == 'USER'):
                print ("Se reemplaza user")
                packet['IRC']['request'] = packet['IRC']['request'].replace('usuario','baduser')
                print (packet['IRC']['request'])
            return packet
    except:
        print ("except")
        return None
