from pyzenvia.enums import APIVersion

URLS = {
    APIVersion.V1: {
        "debug": {
            "send": ''
        },
        "production": {
            "send": 'https://api-http.zenvia.com/GatewayIntegration/msgSms.do?dispatch=send'
        }
    },
    APIVersion.V2: {
        "debug": {
            "send": ''
        },
        "production": {
            "send": ''
        }
    }
}
