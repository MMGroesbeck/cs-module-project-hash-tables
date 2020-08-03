# Use has_value % hash_data_size

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        cap = max(capacity, MIN_CAPACITY)
        self.data_store = [None] * cap
        self.capacity = cap
        self.entries = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # load factor is self.entries/self.capacity
        return self.entries/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        hash = 0xcbf29ce484222325
        fnv_prime = 0x100000001b3
        key_bytes = key.encode()
        for c in key_bytes:
            hash = hash * fnv_prime
            hash = hash ^ c
        return hash & 0xffffffffffffffff


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here



    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value, resizing=False):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        key_hash = self.hash_index(key)
        if self.data_store[key_hash]:
            list_item = self.data_store[key_hash]
            while list_item.next != None and list_item.key != key:
                list_item = list_item.next
            if list_item.key == key:
                list_item.value = value
                return
            else:
                self.entries += 1
                list_item.next = HashTableEntry(key,value)
                if resizing == False:
                    self.resize_check()
                return
        else:
            self.entries += 1
            self.data_store[key_hash] = HashTableEntry(key,value)
            if resizing == False:
                self.resize_check()
            return


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        key_hash = self.hash_index(key)
        if self.data_store[key_hash]:
            list_item = self.data_store[key_hash]
            if list_item.key == key:
                self.data_store[key_hash] = list_item.next
                self.entries -= 1
                self.resize_check()
                return
            else:
                searching = True
                while searching:
                    if list_item.next == None:
                        searching = False
                    elif list_item.next.key == key:
                        list_item.next = list_item.next.next
                        self.entries -= 1
                        self.resize_check()
                        return
                    else:
                        list_item = list_item.next
                print("Key not found.")
                return
        else:
            print("Key not found!")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        key_hash = self.hash_index(key)
        if self.data_store[key_hash]:
            list_item = self.data_store[key_hash]
            while list_item.next != None and list_item.key != key:
                list_item = list_item.next
            if list_item.key == key:
                return list_item.value
            else:
                return None
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        new_table = HashTable(new_capacity)
        for i in range(self.capacity):
            if self.data_store[i]:
                list_item = self.data_store[i]
                while list_item:
                    new_table.put(list_item.key, list_item.value, True)
                    list_item = list_item.next
        self.data_store = new_table.data_store
        self.capacity = new_capacity
    
    def resize_check(self):
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
            return
        elif self.get_load_factor() < 0.2 and self.capacity > MIN_CAPACITY:
            self.resize(max(int(self.capacity / 2), MIN_CAPACITY))

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
