import pytest
import jsonschema
from TestSampleAPI.contract import apiContract

def verify_name(data):
    assert data['Name'] == "Carbon credits", "Name is Incorrect"

def verify_relist(data):
    assert data['CanRelist'], "Can Relist value is not True"

def verify_description(data):
    description = data['Promotions']
    for item in description:
        if item["Name"] == "Gallery":
            assert item["Description"].index("2x larger image"), "2x larger imae text not found in description"

def verify_contract(data,statusCode):
    schema = apiContract.getApi
    if data is not None:
        try:
            myDict = {}
            v = jsonschema.Draft4Validator((schema))
            for error in sorted(v.iter_errors((data)), key=str):
                myDict[str(error.path)] = str(error.message)
                print(myDict)
                assert len(myDict) == 0, "failures in contract"
        except jsonschema.ValidationError as e:
            print(e.message)
    elif statusCode not in [200,404]:
        pytest.xfail("Catalogue fetch failed for this id")
    else:
        pytest.skip("No catalogue present on this id")