def f5(packet):
     try:
        if (packet['TCP']['dstport'] == 6667): #request
            comando = packet['IRC']['request'].split(" ")[0]
            print ("comando: ",comando)
            if (comando == "PART"):
               packet["IRC"]["request"] = packet["IRC"]["request"].replace("PART","QUIT")
        return packet
     except:
        print ("except")
        return None
