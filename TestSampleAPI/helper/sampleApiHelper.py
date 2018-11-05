import pytest
import jsonschema
from TestSampleAPI.contract import apiContract

def verify_name(data):
    """ This function verifies if the name is Carbon Credits or not
    @param data - JSON Response of the API
    """
    assert data['Name'] == "Carbon credits", "Name is Incorrect"

def verify_relist(data):
    """ This function verifies if Can Relist is True or False
    @param data - JSON Response of the API
    """
    assert data['CanRelist'], "Can Relist value is not True"

def verify_description(data):
    """ This function verifies the "Promotions" element with Name = "Gallery" has a Description 
    that contains the text "2x larger image"
    @param data - JSON Response of the API
    """
    description = data['Promotions']
    for item in description:
        if item["Name"] == "Gallery":
            assert item["Description"].index("2x larger image"), "2x larger imae text not found in description"

def verify_contract(data,statusCode):
    """ This function verifies if contract of the API response is valid or not
    @param data - JSON Response of the API
    @param statusCode - Status Code of the API response
    """
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