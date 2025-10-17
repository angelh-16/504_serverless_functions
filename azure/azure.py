import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger1")
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        req_body = {}
    fg = req.params.get('fasting-glucose')
    if not fg:
        fg = req_body.get('fasting-glucose')

    results = "Please provide a 'fasting-glucose' value."
    status_code = 200

    if fg is not None:
        try:
            fg_val = float(fg)
            if fg_val < 100:
                results = "fasting-glucose: " + fg + " status: Normal category: Normal (< 100 mg/dL)"
            elif 100 <= fg_val <= 125:
                results = "fasting-glucose: " + fg + " status: Abnormal category: Prediabetes (100 to 125 mg/dL)"
            elif fg_val >= 126:
                results = "fasting-glucose: " + fg + " status: Abnormal category: Diabetes (126 mg/dL or above)"
        except ValueError:
            results = f"Invalid input provided for fasting-glucose."
            status_code = 400

    return func.HttpResponse(
         f"{results}",
         status_code=status_code
    )
