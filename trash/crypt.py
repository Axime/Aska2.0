"""
Этот модуль отвечает за шифрование входящих банных
и за расшифровывания входящх данных шифром AES256

По итогу он возвращает str строку даных
"""
import cryptocode


class CriptingInformation:

    def cript(self, data_for_cript, password):
        self.get_data = data_for_cript
        encrypted_information = cryptocode.encrypt(data_for_cript, str(password))
        return encrypted_information

    def decript(self,data_for_decript, password):
        self.data_for_decript = data_for_decript
        decrypt_inpormation = cryptocode.decrypt(data_for_decript, str(password))
        return decrypt_inpormation


obj = CriptingInformation()
data_for_cript = "example"
password = "test"

crypting_information = obj.cript(data_for_cript, password)
print(obj.decript(crypting_information, password))

"""str_encoded = cryptocode.encrypt("I am okay","wow")
print(str_encoded)
## And then to decode it:
str_decoded = cryptocode.decrypt(str_encoded, "wow")
print(str_decoded)"""
