from coapthon.client.helperclient import HelperClient

host = "127.0.0.1"
port = 5683
path ="test"

client = HelperClient(server=(host, port))
response = client.get(path)
print (response.pretty_print())
client.stop()

# coap://127.0.0.1:5683/big