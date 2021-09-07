# Your imports go here
import logging
import os

logger = logging.getLogger(__name__)

'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''
def extract_amount(dirpath: str) -> float:

    logger.info('extract_amount called for dir %s', dirpath)
    # your logic goes here
    ocr_file =os.path.join(dirpath,'ocr.json')
    # Intialisation of the variable
    text_data = []
    amt = 0.0
    act_amt = 0.0

    # Reading of the json file in the particular OCR file
    with open(ocr_file, mode='r', encoding="utf-8") as f:
        data = (json.load(f)).get("Blocks")

    # We have all our Required Data in the Text so we will take only that Part from the data
    for i in data:
        # Since it's possible that Text might not be present in everywhere use try and except to avoid errors
        try:
            text_data.append(i['Text'].upper()) # Conversion to upper because Python is case sensitive
        except KeyError:
            continue


    # To extract the amount from the JSON File
    for dt in text_data:
        # In case amount consist of amount like 2,000,000 we are converting it to 2000000
        if "," in dt:
            dt = dt.replace(",",'')

        # Value is the variable which take integer part from the data
        value =repr.findall(r"[+-]?\d+\.\d+", dt)

        # We want the total price and in every bill the maximum float value will the amount
        if len(value) > 0:
            amt = float(value[0])
            act_amt = max(act_amt,amt)
    return act_amt

    return 0.0

print(extract_amount("data\receipt19\expected.json"))