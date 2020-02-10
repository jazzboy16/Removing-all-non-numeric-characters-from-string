#leave only nymber in a string $123,456,789 and convert it to integer

import re
wierd_symbol = '$123,456,789'
pure_number = re.sub('[^0-9]','', wierd_symbol)
int_number=int(pure_number)
