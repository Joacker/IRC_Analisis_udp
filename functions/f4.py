def f4(packet):
     try:
        if (packet['TCP']['dstport'] == 6667): #request
            comando = packet['IRC']['request'].split(" ")[0]
            if (comando == "JOIN"):
               packet["IRC"]["request"] = packet["IRC"]["request"].replace("1","2")
        return packet
     except:
        print ("except")
        return None
