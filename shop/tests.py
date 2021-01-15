from django.test import TestCase
import os
# Create your tests here.
x = None
for root, dir, files in os.walk('.'):
    for file in files:
        if (file.endswith(".txt") and file == "product_categories.txt"):
            print("Your File : ", os.path.join(root, file))
            x = os.path.join(root, file)
            break
            
f = open(x,'r')
print(f.read())
