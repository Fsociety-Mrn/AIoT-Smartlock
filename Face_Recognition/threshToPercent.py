# face_match = 0.5  # threshold bias
# threshold = 0.4   # threshold result

# # formula
# range = 1 - face_match 

# percentage = (1 - threshold) / (range * 2)
# percentage = percentage * 100

# print(f"Percentage value: {int(percentage)}%")

import math

def face_distance_to_conf(face_distance, face_match_threshold=0.6):
    if face_distance > face_match_threshold:
        range = (1.0 - face_match_threshold)
        linear_val = (1.0 - face_distance) / (range * 2.0)
        return linear_val
    else:
        range = face_match_threshold
        linear_val = 1.0 - (face_distance / (range * 2.0))
        return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))
    
        # range = face_match_threshold
        # linear_val = 1.0 - (face_distance / (range * 2.0))
        # return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))
def printLoop(threshhold):
    result = face_distance_to_conf(face_distance=threshhold)
    result = int(result * 100)

    print(f"Percentage value: {result}%")

loop = [
    0.59,
    0.55,
    0.52,
    0.54,
    0.55,
    0.00
]

for each in loop:
    printLoop(each)