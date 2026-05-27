import tempfile
from log_analyzer import analyze_log

def test_log_analysis_counts():
    log_content = """INFO Start
WARNING Low memory
ERROR Crash
INFO End
"""

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_log:
        temp_log.write(log_content)
        temp_log_path = temp_log.name

    result = analyze_log(temp_log_path)

    assert result["INFO"] == 2
    assert result["WARNING"] == 1
    assert result["ERROR"] == 1
