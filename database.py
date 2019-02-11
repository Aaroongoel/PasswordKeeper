from firebase import firebase

firebase = firebase.FirebaseApplication('https://password-keeper-948c2.firebaseio.com/',)

class DataBase:

    def getData(self):
        result = firebase.get('User',None)
        return result

    def updateData(self,dir,value,key):
        firebase.put(dir,value,key)

    def deleteData(self,dir,value):
        firebase.delete(dir,value)

# obj = DataBase()
# print (obj.getData())
# obj.updateData('User','aditya14','am')
# obj.updateData('User','aditya15','ama')
# obj.deleteData('User','aditya15')