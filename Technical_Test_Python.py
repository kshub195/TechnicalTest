#Question 1
import time
from datetime import datetime

#Dictionary for member/non-member
user_types = {
    'nonmember': {'last_download': None},
    'member': {'last_download': None, 'count': 0}
}

#Function
def checkDownload(userType):
    current_time = time.time()
    current_datetime = datetime.now().strftime("%H:%M:%S")
    user = user_types[userType]

    successMessage = current_datetime + "-Your download is starting..."
    failureMessage = current_datetime + "-Too many downloads"

    if user['last_download'] is None:
        # First download
        user['last_download'] = current_time
        if userType == 'member':
            user['count'] = 1
        return successMessage
    
    time_since_last_download = current_time - user['last_download']

    if userType == 'nonmember':
        if time_since_last_download < 5:
            return failureMessage
        else:
            user['last_download'] = current_time
            return successMessage
    
    elif userType == 'member':
        if user['count'] < 2:
            user['last_download'] = current_time
            user['count'] += 1
            return successMessage
        else:
            if time_since_last_download < 5:
                return failureMessage
            else:
                user['last_download'] = current_time
                user['count'] = 1
                return successMessage

#Non-member download
print("Non-members:")
print(checkDownload('nonmember')) 
time.sleep(3)
print(checkDownload('nonmember'))  

#Member download
print("Members:")
print(checkDownload('member'))  
time.sleep(3)
print(checkDownload('member'))  
time.sleep(3)
print(checkDownload('member'))  

#Question 2
#Function
def checkDiscount(purchaseValue): 
    discount = None 

    if purchaseValue > 500 :
        discount = 10

    elif 100 <= purchaseValue < 500 :
        discount = 5

    if discount != None:
        return "Purchase Value is " + str(purchaseValue) + " , discount is " + str(discount) + "%"
    else:
        return "Purchase Value is " + str(purchaseValue) + " , there are no discount"

#Outcomes
print(checkDiscount(300))
print(checkDiscount(80))

#Question 4
import random

#Tier list
item_tier_rarity = [1,2,3,4,5]
vip_ranks = ['v1','v2','v3','v4','v5']

#Function to determine probabilities based on vip rank
def generate_probabilities(vip_rank, item_tier_rarity):

    total_tiers = len(item_tier_rarity)
    vip_rank_index = vip_ranks.index(vip_rank) + 1

    #Calculate base weight
    base_weights = [total_tiers - i for i in range(total_tiers)]
    
    #Adjust probabilities according to vip rank
    adjusted_weights = []
    for i in range(total_tiers):
        if vip_rank_index < 4:
            if i <= vip_rank_index:
                adjusted_weights.append(base_weights[i] * 2) 
            else:
                adjusted_weights.append(base_weights[i])
        else:
            if i <= vip_rank_index and i < total_tiers - 2:
                adjusted_weights.append(base_weights[i] * 2) 
            else:
                adjusted_weights.append(base_weights[i] * vip_rank_index)

    #Normalize probabilities
    total_weight = sum(adjusted_weights)
    probabilities = [w/total_weight for w in adjusted_weights]

    return probabilities

#Function to roll items
def roll_item(vip_rank):
    probabilities = generate_probabilities(vip_rank, item_tier_rarity)
    item = random.choices(item_tier_rarity, probabilities)[0]
    return item

#Function to simulate rolls and generate results
def generate_results(num_rolls):
    print("Array")
    print("(")
    for vip_rank in vip_ranks[:3]:
        print(f"    [{vip_rank}] => Array")
        print("    (")
        
        #Initialize tier counts for all tiers to 0
        tier_counts = {tier: 0 for tier in item_tier_rarity}
        
        #Count occurrences of each tier
        rolls = [roll_item(vip_rank) for _ in range(num_rolls)]
        for roll in rolls:
            tier_counts[roll] += 1
            
        #Print tier counts in ascending order
        for tier in sorted(tier_counts.keys()):
            print(f"         [{tier}] => {tier_counts[tier]}")
            
        print("    )")
    print(")")

#Outcome
generate_results(100)

#Check probability list for all vip_ranks
# for i in vip_ranks:
#     generate_probabilities(i, item_tier_rarity)

#Issues:
#Probability list for each item tiers will be the same from Vip rank 4 onwards, making higher Vip ranks pointless

#Solution:
#Adjustments was made to instead multiply the base weights of a higher rarity (ex: item tier 4, item tier 5) based on vip_rank_index
#The logic can be modified in the generate_probabilities function to accommodate any changes like adding new tiers for item/vip



