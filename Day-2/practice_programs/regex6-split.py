#It will seperate the data or words at particular point provided
import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)

# second example

text1 = "apple banana orange grape"
pattern1 = r' '

split1 = re.split(pattern1,text1)
print('split result:',split1)