import json
from guides.pytest.basic_pytest_check_data.report_data import GeneratingReport


def test_report_data():
    GeneratingReport.generate_report("2024-4-20 12-37-9",
                                     "Passed",
                                     "TC-001 Covering Our test case example")
    with open('report.json') as file:
        data = json.load(file)
        assert type(data) == dict
        assert len(data) == 3
def test_report_data_key():
    GeneratingReport.generate_report("2024-4-20 12-37-9",
                                     "Passed",
                                     "TC-001 Covering Our test case example")
    with open('report.json') as file:
        data = json.load(file)
        assert "timeStamp" in data
        assert "status" in data

def test_report_data_value():
    GeneratingReport.generate_report("2024-4-20 12-37-9",
                                     "Passed",
                                     "TC-001 Covering Our test case example")
    with open('report.json') as file:
        data = json.load(file)
        assert "Passed" ==  data["status"]
        assert "2024-4-20 12-37-9" == data["timeStamp"]