"""
Этот модуль отвечает за шифрование входящих банных
и за расшифровывания входящх данных шифром AES256

По итогу он возвращает str строку даных
"""
import cryptocode

class CriptingInformation ():

    def cript (self,get_data):
        self.get_data = get_data
        encrypted_information = cryptocode.encrypt(get_data,"password")
        return encrypted_information





obj = CriptingInformation()
data_for_cript = "example"
print(obj.cript(data_for_cript))





"""str_encoded = cryptocode.encrypt("I am okay","wow")
print(str_encoded)
## And then to decode it:
str_decoded = cryptocode.decrypt(str_encoded, "wow")
print(str_decoded)"""