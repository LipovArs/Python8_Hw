import csv

class Phone:
  number = None
  _incoming_call = 0
  
  def set_number(self, number):
    self.number = number

  
  def get_call(self):
    return self._incoming_call

  
  def recive_calls(self):
    self._incoming_call += 1

  def get_call_list(self):
    with open('call_list.csv', 'a') as file:
      write = csv.writer(file)
      write.writerow([self.number, self._incoming_call])
      
    print(f'{self.number} - {self._incoming_call}\n')
    
first_phone = Phone()
second_phone = Phone()
thrid_phone = Phone()

first_phone.set_number('+308956438912')
second_phone.set_number('+380993847109')
thrid_phone.set_number('+380559302840')

for n in range(3):
  first_phone.recive_calls()

for n in range(7):
  second_phone.recive_calls()

for n in range(5):
  thrid_phone.recive_calls()

phone_lists = [first_phone, second_phone, thrid_phone]

for n in phone_lists:
  n.get_call_list()
  