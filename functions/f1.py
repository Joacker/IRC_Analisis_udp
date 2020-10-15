def f1(packet):
     try:
        if (packet['TCP']['dstport'] == 6667): #request
            comando = packet['IRC']['request'].split(" ")[0]
            print ("comando: ",comando)
            if (comando == "PART"):
               packet["IRC"]["request"] = packet["IRC"]["request"].replace("PART","JOIN")
            if (comando == "JOIN"):
               packet["IRC"]["request"] = packet["IRC"]["request"].replace("JOIN","PART")
        return packet
     except:
        print ("except")
        return None
