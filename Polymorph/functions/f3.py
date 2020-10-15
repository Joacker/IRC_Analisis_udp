def f3(packet):
    try:
        if (packet['TCP']['dstport'] == 6667): #request
            comando = packet['IRC']['request'].split(" ")[0]
            if(packet['IRC']['request'].split(" ")[0]=='PRIVMSG'):
                print (packet["IRC"]["request"])
                packet["IRC"]["request"] = packet['IRC']['request'].replace(':claro',":solar")
                print (packet["IRC"]["request"])
            return packet
    except:
        print ("except")
        return None
