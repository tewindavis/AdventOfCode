from math import log


class part1():

    def __init__(self):
        pass
        self.ranges = []


    def _read_input(self):
        with open("./input.csv", 'r') as f:
            in_str = f.readlines()[0]

        
        num_list = in_str.split(',')
        list_list = [ i.split('-') for i in num_list]
        num_list_list = [ ( int(j[0].strip()), int(j[1].strip()) ) for j in list_list]
        

        self.ranges = num_list_list


    def _test_number_string(self, string):
        half_index = len(string) // 2
        return string[:half_index] == string[half_index:]


    def _find_repeats(self):
        
        running_sum = 0       
        for (min_num, max_num) in self.ranges:
            max_num_str = str(max_num)
            half_length = len( str(max_num) ) // 2
            
            left_min = min_num // 10**half_length
            # bases to be repeated
            for i in range( left_min, 10**half_length):
                num_to_check = i * (1 + 10**half_length) 
                               
                if min_num <= num_to_check <= max_num:
                    if len( str( num_to_check ) ) % 2 == 0:
                        running_sum += num_to_check

        print( f"The answer to part 1 is {running_sum}")

    def run_all(self):
        self._read_input()
        self._find_repeats()



class part2(part1):
    def __init__(self):
        super().__init__()
        
    def _find_repeats(self):
        running_sum = 0
        
        for min_num, max_num in self.ranges:
            print( min_num, max_num )
            
            max_num_str = str(max_num)
            length = len( max_num_str ) 

            # bases to be repeated
            for i in range( 1, 10**(length//2):
                
                places = int( log( i, 10 ) // 1 + 1 )

                
                multiplicand = sum( [ (10**(places * j)) for j in range(  half_length // places  * 2)] )
                num_to_check = i * multiplicand
                
                print( '\t', i, places, multiplicand, num_to_check )
                
                # print( num_to_check )
                if min_num <= num_to_check <= max_num:
                    print( '\t', multiplicand, num_to_check )
                    running_sum += num_to_check

        print( f"The answer to part 2 is {running_sum}")


if __name__ == "__main__":
    part1().run_all()
    part2().run_all()
