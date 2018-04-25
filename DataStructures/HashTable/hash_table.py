import linked_list as ll

'''
Today I went over hash tables and implement my own. I used the asci value of each of the characters in the name summed 
together with a modulus operation with the size of the list to determine the index value. I used chaining to handle 
collisions. I used the linked list class I created earlier to handle the chaining. I'll go in more detail in the readme
file for data structures. 
'''
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

class HashTable(object):
    def __init__(self, size=20):
        self.table = [None]*size
        self.size = size

    def get_size(self):
        return self.size

    def insert(self, person):
        asci_code = self.get_asci(person.get_name())
        index = asci_code % self.size
        if self.table[index] is None:
            self.table[index] = ll.LinkedList(person)
        else:
            self.table[index].append(person)


    def get_asci(self, name):
        asci_numbers = [ord(val) for val in name]
        sum_of_nums = sum(asci_numbers)
        return sum_of_nums

    def display_talbe(self):
        for index, info in enumerate(self.table):
            if info is not None:
                print(index)
                info.display()
            else:
                print(index)
                print(info)

    def lookup(self, name):
        index = self.get_asci(name) % self.size
        if self.table[index] is None:
            print("Data couldn't be found")
        elif self.table[index].get_length() == 1:
            self.table[index].display()
        else:
            while self.table[index].head is not None:
                if self.table[index].head.get_data.get_name() == name:
                    print('Name: ' + name + ' | ' + str(self.table[index].head.get_data.get_age()))
                    break
                self.table[index] = self.table[index].head.get_next_link()


if __name__ == '__main__':
    print('Welcome to my hash table tester.')
    input_name = None
    input_age = None
    my_hash_talbe = HashTable(5)
    while True:
        try:
            name_is_good = False
            while name_is_good == False:
                input_name = input("What is your name? ")
                if len(input_name) < 1:
                    print('Your name must be more than 4 character long')
                else:
                    break
        except:
            print("something went wrong. Try again")
            continue

        while True:
            try:
                input_age = int(input('How old are you? '))
                break
            except ValueError:
                print("Your age must be an integer. Pleas input a numeric value for your age. ")

        my_hash_talbe.insert(Person(input_name, input_age))

        if input('Would you like to add another person? press y to add more or anything else to quit: ') != 'y':
            break

    while True:

        my_hash_talbe.lookup(input("Enter a name to search for: "))

        if input("Search again? (y/n) ") != 'y':
            break



