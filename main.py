import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
user = input("Enter words\n")


def classify(text):
    key = "2978bbc0-238a-11ec-a6d4-6788970fe8aa3daaf3c7-a450-434a-b841-abdf01d754e1"
    url = "https://machinelearningforkids.co.uk/api/scratch/" + key + "/classify"

    response = requests.get(url, params={"data": text})

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
demo = classify(user)

label = demo["class_name"]
confidence = demo["confidence"]

# CHANGE THIS to do something different with the result
print("result: '%s' with %d%% confidence" % (label, confidence))
