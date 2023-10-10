import json

# Data to be stored as JSON
data = {
  "History": {
    "Familaran,Ivan": {
      "Oct 2 2023": {
        "4:12 PM": "Facial Login"
      }
    },
    "Lisboa,Art": {
      "Aug 11 2023": {
        "4:06 PM": "Facial Login",
        "4:07 PM": "pincode Login",
        "6:32 PM": "Facial Login",
        "6:34 PM": "pincode Login"
      },
      "Aug 14 2023": {
        "3:08 PM": "Facial Login",
        "3:10 PM": "Facial Login"
      },
      "Aug 9 2023": {
        "12:58 AM": "Access Granted",
        "1:00 AM": "Access Granted",
        "1:01 AM": "Access Granted",
        "1:27 PM": "Access Granted",
        "2:12 PM": "Access Granted",
        "3:04 PM": "pincode Login",
        "3:09 PM": "pincode Login"
      },
      "Oct 10 2023": {
        "1:51 PM": "Facial Login",
        "1:54 PM": "Facial Login",
        "1:55 PM": "Facial Login",
        "1:56 PM": "Facial Login"
      },
      "Oct 3 2023": {
        "12:41 PM": "Facial Login",
        "4:01 PM": "Facial Login",
        "4:06 PM": "Facial Login",
        "9:00 AM": "Facial Login",
        "9:01 AM": "Facial Login"
      },
      "Oct 7 2023": {
        "10:28 AM": "Facial Login",
        "10:29 AM": "Facial Login",
        "4:09 PM": "Facial Login",
        "4:10 PM": "Facial Login",
        "4:45 PM": "Facial Login"
      },
      "Oct 8 2023": {
        "11:39 AM": "Facial Login",
        "11:41 AM": "Facial Login",
        "11:42 AM": "Facial Login",
        "11:46 AM": "Facial Login",
        "12:03 PM": "Facial Login",
        "12:05 PM": "Facial Login",
        "12:06 PM": "Facial Login",
        "12:18 PM": "Facial Login",
        "12:19 PM": "Facial Login",
        "12:22 PM": "Facial Login",
        "12:25 PM": "Facial Login",
        "12:26 PM": "Facial Login",
        "12:27 PM": "Facial Login",
        "12:28 PM": "Facial Login",
        "12:47 PM": "Facial Login",
        "12:48 PM": "Facial Login",
        "12:52 PM": "Facial Login",
        "12:56 PM": "Facial Login",
        "12:59 PM": "Facial Login",
        "1:00 PM": "Facial Login",
        "1:45 PM": "Facial Login",
        "1:59 PM": "Facial Login",
        "2:02 PM": "Facial Login",
        "2:03 PM": "Facial Login",
        "2:16 PM": "Facial Login",
        "2:17 PM": "Facial Login",
        "2:24 PM": "Facial Login",
        "2:25 PM": "Facial Login",
        "2:27 PM": "Facial Login",
        "2:28 PM": "Facial Login",
        "2:30 PM": "Facial Login",
        "2:32 PM": "Facial Login",
        "2:34 PM": "Facial Login",
        "2:35 PM": "Facial Login",
        "2:36 PM": "Facial Login",
        "2:39 PM": "Facial Login",
        "2:40 PM": "Facial Login",
        "3:19 PM": "Facial Login",
        "3:20 PM": "Facial Login",
        "3:21 PM": "Facial Login"
      },
      "Sep 18 2023": {
        "8:32 AM": "Facial Login"
      },
      "Sep 29 2023": {
        "5:20 PM": "Facial Login",
        "5:21 PM": "Facial Login"
      },
      "Sep 3 2023": {
        "9:33 AM": "Facial Login",
        "9:34 AM": "Facial Login",
        "9:35 AM": "Facial Login"
      },
      "Sep 30 2023": {
        "11:33 AM": "Facial Login",
        "11:37 AM": "Facial Login",
        "7:53 AM": "Facial Login",
        "8:02 AM": "Facial Login",
        "8:11 AM": "Facial Login",
        "8:13 AM": "Facial Login",
        "8:14 AM": "Facial Login",
        "8:15 AM": "Facial Login",
        "8:25 AM": "Facial Login",
        "8:32 AM": "Facial Login"
      },
      "Sep 9 2023": {
        "3:05 PM": "Facial Login",
        "3:06 PM": "Facial Login",
        "3:07 PM": "Facial Login"
      }
    },
    "No match detected": {
      "Aug 12 2023": {
        "5:16 PM": "Access Denied"
      },
      "Aug 9 2023": {
        "3:03 PM": "Access Denied pincode",
        "3:09 PM": "Access Denied pincode"
      },
      "Oct 1 2023": {
        "1:58 PM": "Access Denied",
        "1:59 PM": "Access Denied",
        "2:00 PM": "Access Denied",
        "2:02 PM": "Access Denied",
        "2:05 PM": "Access Denied",
        "2:08 PM": "Access Denied",
        "2:09 PM": "Access Denied",
        "2:16 PM": "Access Denied",
        "2:19 PM": "Access Denied",
        "2:24 PM": "Access Denied",
        "2:25 PM": "Access Denied",
        "5:39 PM": "Access Denied",
        "5:40 PM": "Access Denied",
        "5:41 PM": "Access Denied",
        "5:46 PM": "Access Denied",
        "5:47 PM": "Access Denied",
        "6:30 PM": "Access Denied",
        "7:01 PM": "Access Denied",
        "7:02 PM": "Access Denied",
        "7:05 PM": "Access Denied",
        "7:13 PM": "Access Denied"
      },
      "Oct 10 2023": {
        "2:15 PM": "Access Denied",
        "2:16 PM": "Access Denied",
        "2:18 PM": "Access Denied",
        "2:19 PM": "Access Denied"
      },
      "Oct 2 2023": {
        "1:04 PM": "Access Denied",
        "1:06 PM": "Access Denied",
        "1:07 PM": "Access Denied",
        "1:08 PM": "Access Denied",
        "4:06 PM": "Access Denied",
        "4:11 PM": "Access Denied",
        "4:12 PM": "Access Denied",
        "4:31 PM": "Access Denied",
        "4:40 PM": "Access Denied",
        "4:44 PM": "Access Denied",
        "4:45 PM": "Access Denied",
        "4:51 PM": "Access Denied",
        "4:58 PM": "Access Denied",
        "4:59 PM": "Access Denied",
        "5:23 PM": "Access Denied",
        "5:24 PM": "Access Denied",
        "5:28 PM": "Access Denied",
        "5:30 PM": "Access Denied",
        "5:35 PM": "Access Denied",
        "5:44 PM": "Access Denied",
        "5:46 PM": "Access Denied",
        "5:47 PM": "Access Denied",
        "5:49 PM": "Access Denied",
        "5:51 PM": "Access Denied",
        "5:55 PM": "Access Denied",
        "5:56 PM": "Access Denied",
        "6:04 PM": "Access Denied",
        "6:05 PM": "Access Denied",
        "6:12 PM": "Access Denied",
        "6:14 PM": "Access Denied",
        "6:18 PM": "Access Denied",
        "6:19 PM": "Access Denied",
        "6:20 PM": "Access Denied",
        "6:22 PM": "Access Denied",
        "6:35 PM": "Access Denied",
        "6:36 PM": "Access Denied",
        "7:29 PM": "Access Denied",
        "7:32 PM": "Access Denied",
        "7:33 PM": "Access Denied"
      },
      "Oct 3 2023": {
        "8:28 AM": "Access Denied",
        "8:32 AM": "Access Denied",
        "8:34 AM": "Access Denied",
        "8:36 AM": "Access Denied",
        "8:48 AM": "Access Denied",
        "8:50 AM": "Access Denied",
        "8:54 AM": "Access Denied",
        "8:55 AM": "Access Denied"
      },
      "Sep 30 2023": {
        "3:47 PM": "Access Denied",
        "3:51 PM": "Access Denied",
        "3:52 PM": "Access Denied",
        "3:53 PM": "Access Denied",
        "4:29 PM": "Access Denied",
        "4:30 PM": "Access Denied",
        "4:33 PM": "Access Denied",
        "4:41 PM": "Access Denied",
        "4:44 PM": "Access Denied",
        "4:46 PM": "Access Denied",
        "4:47 PM": "Access Denied"
      }
    }
  },
}

# Writing data to a JSON file
with open("Firebase/Firebase.json", "w") as json_file:
    json.dump(data, json_file)

# Reading data from a JSON file
with open("Firebase/Firebase.json", "r") as json_file:
    loaded_data = json.load(json_file)

# Now, loaded_data contains the data from the JSON file
print(loaded_data)
