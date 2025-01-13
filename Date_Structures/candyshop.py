# Accidentally we added "2" and "false" to the list
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)
# Create a function called repair_sweets() which takes the list as a parameter
# Expected output: "Cupcake", "Croissant", "Brownie", "Ice cream"
def repair_sweets(list_):
  for i in  range(len(list_)):
    if list_[i] == False:
      list_[i] = "Ice cream"
    elif list_[i] == 2:
      list_[i] = "Croissant"
  return list_
if __name__ == "__main__":
  shop_items = ["Cupcake", 2, "Brownie", False]
  print(repair_sweets(shop_items))