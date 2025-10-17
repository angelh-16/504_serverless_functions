import json
import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Expects JSON with fasting glucose (or query params as fallback).
    Returns a JSON classification of fasting glucose.
    """
    # Prefer JSON body; fall back to query parameters for convenience
    data = request.get_json(silent=True) or {}
    args = request.args or {}

    fasting_glucose = data.get("fasting glucose", args.get("fasting glucose"))

    # Presence check
    if fasting_glucose is None:
        return (
            json.dumps({"error": "Fasting glucose' is required."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Type/convert check
    try:
        fg_val = float(fasting_glucose)
    except (TypeError, ValueError):
        return (
            json.dumps({"error": "'Fasting glucose' must be numbers."}),
            400,
            {"Content-Type": "application/json"},
        )

    status = "normal" if (fg_val < 100) else "abnormal"

    if fg_val < 100:
        category = "Normal (< 100 mg/dL)"
    elif (fg_val >= 100 and fg_val <= 125):
        category = "Prediabetes (100 to 125 mg/dL)"
    elif fg_val >= 126:
        category = "Diabetes 126 mg/dL or above"
    else:
        category = "abnormal"

    payload = {
        "fasting glucose": fg_val,
        "status": status,
        "category": category,
    }

    return json.dumps(payload), 200, {"Content-Type": "application/json"}