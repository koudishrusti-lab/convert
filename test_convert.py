from convert import converted_values

def test_convert_km_to_miles():
 assert converted_values(5.6,"km") == 3.4796776
 assert converted_values(7.8,"km") ==  4.8466938

def test_convert_miles_to_km():
 assert converted_values(3.61,"miles") == 5.80972101
 assert converted_values(8.34,"miles") ==  13.421903939999998
 
def test_converted_zero_value():
 assert converted_values(0.0,"km") == 0.0
    